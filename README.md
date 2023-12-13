# Continuous_Soccer_Pass_Detection

This work champions the application of SML approaches to the ACM DEBS 2013 Grand Challenge data source. Specifically, data collected from sensors in players’ shoes and the ball during a soccer match is used to create balanced and imbalanced datasets, focusing on pass classification based exclusively on leg movement. The main contributions of the project include:

• Presenting a performance comparison between traditional Machine Learning and SML classification algorithms using a balanced dataset to classify soccer passes by analyzing only the leg movement and demonstrating that the results achieved are comparable.

• Evaluating the generalization abilities of the algorithms with imbalanced test sets to investigate if the performance remains unchanged.

• Showing that SML outperforms traditional ML in the same performance comparison using larger rebalanced datasets generated synthetically through static and dynamic methods.

• Confirming the performance results within the rebalanced datasets using statistical tests.

In this repository there are the main files containing the datasets and the code to compute the results obtained.

Raw sensor data (dataset used during the code as "full-game.csv") can be downloaded from: https://www.iis.fraunhofer.de/en/ff/lv/dataanalytics/ek/download.html

The **data** folder contains all the main datasets and csv files used for the project. They are divided into various folders for clarity.

The **lowPass.py** file contains the code to detect soccer passes that occur during the match.

The **datasetComputation.ipynb** and **stats.ipynb** notebooks contain the code with the computation of the various features for the creation of the balanced and imbalanced datasets.

The **passML1000.ipynb** notebook contains the code to compute the performance metrics using various ML algorithms. As an example, the results of the initial dataset consisting of 1000 tuples are shown. The computations are similar for the other datasets by modifying the size_train, size_val, and size_test variables based on the size of the dataset to be analyzed.

The **passSML1000.ipynb** notebook contains the code to compute the performance metrics using various SML algorithms. As an example, the results of the initial dataset consisting of 1000 tuples are shown. The computations are similar for the other datasets by modifying the 'batch_size' variable based on the size of the dataset to be analyzed.

The **resampling.ipynb** notebook contains the code to generate the various synthetic datasets rebalanced using SMOTE and Borderline SMOTE. Moreover, it graphically shows the distribution of the datasets (even those generated with C-SMOTE).

The **moa.jar** and **sizeofag-1.0.4.jar** are the files necessary to synthetically generate the datasets through C-SMOTE. In particular, the command line to execute is:

java -Xmx15g -Xss50M -cp moa.jar -javaagent:sizeofag-1.0.4.jar moa.DoTask "EvaluatePrequentialSMOTE -l (meta.imbalanced.CSMOTESaveInstance -e 1 -m 45) -s (ArffFileStream -f dataset1500_moa.arff) -d dataset_2910_moa_1500.csv", where 'e' indicates the seed and for this work it is incremented by 1 for each subsequent dataset (e.g. dataset2500_moa.arff has -e 2).

The **statisticalTest.ipynb** notebook contains the code for applying the statistical tests (t-test and Nemenyi test).
