
# Fake News Detection using NLP



## Objective
This case study requires to develop a Machine Learning model,Deep learning model which predicts whether the news that appeared in the article is Fake or real(genuine)   

## Data Description

The dataset consists of a total 20799 news from different articles along with the classification whether the news is Geuine or Fake 

## Data:

Use the below link to download the Data Set:

URL : https://www.kaggle.com/c/fake-news/data
## Approach:
* Data Description
  * We will be using the Fake News classification data set present in the Kaggle Repository. This Data set is satisfying our data requirement. 

* Data Preprocessing
 * ML Approcah
   * As part of data preprocessing I have removed the stopwords in the data and then applied porter stemmer to convert a word into its root form and then applied the     TfidfVectorizer.
 * Deep Learning Approach
   *   As part of data preprocessing I have removed the stopwords in the data and then applied porter stemmer to convert a word into its root form and then applied the one hot encoding and then applied padding.

* Model Training
 * ML Approach
   * We trained various models in our notebook and Passive Aggressive Classifier Algorithm was a good fit.
 * DL Approach
   * I have trained the model with LSTM,BI-Directional LSTM and stacked LSTM but the best accuracy was about 93%. so I have used the ML model for deployment.
  
* Model Evaluation
  * We have used accuracy score, F1-score to decide the number of clusters

* Model Saving
  * we will save our model so that we can use them for prediction purpose.

* Push to app
  * We had created a streamlit app to deploy our model 

* Data from client side for prediction purpose
  * Now our application on cloud is ready for doing prediction. The prediction data which we receive from client side based on the data given the model will classify whether the news is genuine or Fake.

Screenshots
====================================
**Homepage interface:**

![Homepage](https://user-images.githubusercontent.com/24864663/156895292-e1e41060-494f-4e08-ba12-db18c21d4c7c.PNG)

**Prediction Interface**
![Predictionpage](https://user-images.githubusercontent.com/24864663/156895294-af0330a2-4bc0-4804-892f-6a5ecab0864f.PNG)

## Summary for the Prediction

Output will be the classification whether the news is genuine or Fake

##Accuracy of the Model
- 95% accuracy on the test data

## Algorithms used :
In this dataset I have used three clustering algorithm to perform segmentation.These algorithms are given below.
- [Multinomial Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB)
- [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [Passive Aggressive Classifier Algorithm](https://www.geeksforgeeks.org/passive-aggressive-classifiers/)
 
