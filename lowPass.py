import pandas as pd
import math
from csv import writer


df = pd.read_csv("data/full-game.csv",  names=['sid', 'ts', 'x', 'y', 'z', '|v|', '|a|', 'vx', 'vy', 'vz', 'ax', 'ay', 'az'])


def acc_i(a, ai):
    acc = a * ai * 1e-10
    return acc


# pass if acceleration > 300 (variable)
def hit_acc_pass(acx, acy):
    hit = acx > 300 or acx < -300 or acy > 300 or acy < -300
    return hit


# rec if acceleration > 55 (variable)
def hit_acc_rec(acx, acy):
    hit = acx > 55 or acx < -55 or acy > 55 or acy < -55
    return hit


def data_ball(ball):
    ball_id = ball == 4 or ball == 8 or ball == 10 or ball == 12
    return ball_id


def data_team1r(p1r):
    player_id1r = p1r == 14 or p1r == 16 or p1r == 88 or p1r == 52 or p1r == 54 or p1r == 24 or p1r == 58 or p1r == 28
    return player_id1r


def data_team1l(p1l):
    player_id1l = p1l == 13 or p1l == 47 or p1l == 49 or p1l == 19 or p1l == 53 or p1l == 23 or p1l == 57 or p1l == 59
    return player_id1l


def data_team2r(p2r):
    player_id2r = p2r == 62 or p2r == 64 or p2r == 66 or p2r == 68 or p2r == 38 or p2r == 40 or p2r == 74 or p2r == 44
    return player_id2r


def data_team2l(p2l):
    player_id2l = p2l == 61 or p2l == 63 or p2l == 65 or p2l == 67 or p2l == 69 or p2l == 71 or p2l == 73 or p2l == 75
    return player_id2l


def dist(x1, y1, x2, y2):
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return distance/1000

# Example: passes inside the window (start_pass and end_pass)
breakVar = False
indexCheck = -1
start_pass = 12429295377548981
end_pass = 12444295055052679

'''
# CODE TO FIND THE SOCCER PASSES IN A CONTINUOUS MANNER
# (Anyway, for computational reasons, we found the passes through small selected windows (start_ts and end_ts))
nRows = df.shape[0]
dimShift = math.ceil((nRows * 5)/300)
iterations = math.ceil(nRows/dimShift) - 1
start = 10753295594424116 # (start first time)
timeWindow = 10 * 1e12
timeShift = 5 * 1e12

for z in range(iterations):
    print(z + 1)
    dataWindow = df[(df['ts'] >= start) & (df['ts'] < start + timeWindow)]
'''

dataWindow = df[(df['ts'] >= start_pass) & (df['ts'] < end_pass)]
for i, row in dataWindow.iterrows():
    if breakVar and i <= indexCheck:
        continue
    else:
        breakVar = False
        sid = row['sid']
        if data_team1r(sid): # right or left foot selection depending on video match observation
            currentX = row['x']
            currentY = row['y']
            currentTs = row['ts']
            dataCheckTs = df[(df['ts'] >= currentTs - 1 * 1e11) & (df['ts'] < currentTs + 1 * 1e11)]
            for j, row2 in dataCheckTs.iterrows():
                ballSid = row2['sid']
                if data_ball(ballSid):
                    ballX = row2['x']
                    ballY = row2['y']
                    ax = row2['ax']
                    ay = row2['ay']
                    ac = row2['|a|']
                    acc_x = acc_i(ac, ax)
                    acc_y = acc_i(ac, ay)
                    newTs = row2['ts']
                    if hit_acc_pass(acc_x, acc_y) and dist(currentX, currentY, ballX, ballY) < 0.3:
                        dataCheckPass = df[(df['ts'] >= newTs) & (df['ts'] < newTs + 4 * 1e12)]
                        for k, row3 in dataCheckPass.iterrows():
                            newBallSid = row3['sid']
                            if data_ball(newBallSid) and newBallSid == ballSid:
                                newBallX = row3['x']
                                newBallY = row3['y']
                                axNew = row3['ax']
                                ayNew = row3['ay']
                                acNew = row3['|a|']
                                passTs = row3['ts']
                                acc_x_new = acc_i(acNew, axNew)
                                acc_y_new = acc_i(acNew, ayNew)
                                if hit_acc_rec(acc_x_new, acc_y_new):
                                    dataLastCheck = df[(df['ts'] >= passTs - 1 * 1e11) & (df['ts'] < passTs + 1 * 1e11)]
                                    for h, row4 in dataLastCheck.iterrows():
                                        newSid = row4['sid']
                                        if data_team1r(newSid) and newSid != sid:
                                            newX = row4['x']
                                            newY = row4['y']
                                            recTs = row4['ts']
                                            if dist(newX, newY, newBallX, newBallY) < 0.5:
                                                List = [newTs, sid, passTs , newSid]
                                                with open('data/passList.csv', 'a') as f_object:
                                                   writer_object = writer(f_object)
                                                   writer_object.writerow(List)
                                                   f_object.close()
                                                indexCheck = h
                                                breakVar = True
                                                break
                                    if breakVar:
                                        break
                        if breakVar:
                            break

