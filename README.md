# Continuous_Soccer_Pass_Detection

This work champions the application of SML approaches to the ACM DEBS 2013 Grand Challenge data source. Specifically, data collected from sensors in players’ shoes and the ball during a soccer match is used to create balanced and imbalanced datasets, focusing on pass classification based exclusively on leg movement. The main contributions of the project include:

• Presenting a performance comparison between traditional Machine Learning and SML classification algorithms using a balanced dataset to classify soccer passes by analyzing only the leg movement and demonstrating that the results achieved are comparable.

• Evaluating the generalization abilities of the algorithms with imbalanced test sets to investigate if the performance remains unchanged.

• Showing that SML outperforms traditional ML in the same performance comparison using larger rebalanced datasets generated synthetically through static and dynamic methods.

• Confirming the performance results within the rebalanced datasets using statistical tests.

In this repository there are the main files containing the datasets and the code to compute the results obtained.

The **data** folder contains all the main datasets and csv files used for the project. They are divided into various folders for clarity.

The **lowPass.py** file contains the code to detect soccer passes that occur during the match.

The **stats.ipynb** notebook contains the code with the computation of the various features for the creation of the initial datasets.

The **passML1000.ipynb** notebook contains the code to compute the performance metrics using various ML algorithms. As an example, the results of the initial dataset consisting of 1000 tuples are shown. The computations are similar for the other datasets by modifying the size_train, size_val, and size_test variables based on the size of the dataset to be analyzed.

The **passSML1000.ipynb** notebook contains the code to compute the performance metrics using various SML algorithms. As an example, the results of the initial dataset consisting of 1000 tuples are shown. The computations are similar for the other datasets by modifying the 'batch_size' variable based on the size of the dataset to be analyzed.
