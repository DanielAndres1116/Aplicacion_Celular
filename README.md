# 1. App purchase prediction: will your users become customers of an app?

## 1.1. Dataset Description

For our analysis, we make use of the data from a company that operates a mobile application, where their services can be obtained. The database contains two files.

The first file, a CSV file whose name is “appdata10.csv” holds the information of the users who have accessed the application. The information includes the day and time of the installation of the App, as well as the behavior they had within the application and the pages they visited. The data collected is only from the first 24 hours after the application has been installed. This is because the company provides full access to all its options, including the paid ones, during the first 24 hours of installation. After this time, access to these options is blocked unless the customer subscribes to the paid version.

This first CSV database (appdata10.csv) contains the following features:

1.	user: a unique identifier for each user
2.	first_open: the date and time of the user’s first app open
3.	dayofweek: the day of the week the user opened the app for the first time
4.	hour: the hour of the day the user opened the app for the first time
5.	age: the user’s age
6.	screen_list: a comma-separated list of screens that the user visited
7.	numscreens: the number of screens visited by the user
8.	minigame: whether the user played a minigame (0 for no, 1 for yes)
9.	used_premium_feature: whether the user used a premium feature (0 for no, 1 for yes)
10.	enrolled: whether the user enrolled in a program (0 for no, 1 for yes)
11.	enrolled_date: the date and time the user enrolled in a program (if applicable)
12.	liked: whether the user liked the app (0 for no, 1 for yes)

The second file has the names of the most visited pages and those that are of interest to us for our analysis. In this file, we can observe which pages are the most popular among the users and how they interact with the application. This information is crucial in understanding the behavior of users within the application and can be used to improve their experience and increase engagement.

## 1.2. Project Objectives

Many companies offer their services through mobile apps. Sometimes, some of these services are free, with the intention of allowing users to see what the company offers before purchasing the paid membership. Therefore, with this project, we aimed to predict which users are likely to purchase a paid subscription based on their app usage behavior.

During the process, important data from both tables was combined to create a more valuable dataset. Some variables were unified to make it less extensive and clearer. Various charts were also used to better understand user behavior and trends, for example, some of the interesting analyses performed here included examining the hours when the most users were active, observing the predominant ages of users, and also examining the elapsed time between the user’s subscription and when the app was opened.

Next, we will use a set of histograms that will allow us to visualize interesting aspects of the data to better understand the behavior of users. A histogram is a graphical representation of data that shows the frequency distribution of a set of continuous or discrete data. It is a bar graph that groups data into different ranges, or bins, and displays the number of data points in each bin. The height of each bar represents the frequency of data points within that bin.

![image](https://user-images.githubusercontent.com/43154438/229923369-9954d7ef-d6a5-4d30-a6bd-0a05b454a9d4.png)

Figure 1: histogram of the number of views according to the ages of the users

We can note that the users whose ages vary from 22 years old and 28 years old are those who see a greater number of times the screens of the services provided by the company. But there are an interesting range of ages between 20 and 38 where the users check an important number of times those screens. This can be useful to steer the company’s campaign efforts to people of these ages.

![image](https://user-images.githubusercontent.com/43154438/229923487-3c04f60d-1c91-4532-8b34-57c25f67ea24.png)

Figure 2: histogram representing the hours of the day (X-axis) and the average amount of time users use the company’s online platform (Y-axis)

We can see that the hours (twenty-four hours format) where there is more engagement by the users are: 0 to 2 (12 a.m to 2 a.m in twelve hours format) and 15 to 23 (3 p.m to 11 p.m in twelve hours format). It gives us an idea about the right hours range where company should aim the campaign marketing efforts.

![image](https://user-images.githubusercontent.com/43154438/229923575-01ec6060-e96e-4f5b-bf41-bba408ce4d28.png)

Figure 3: histogram representing the time elapsed between the last time users open the free version of the app and subscribe to the paid version

We can see that If a user has been more than 10 hours since they last opened the paid version of the app, they are unlikely to sign up for the paid version. It means that could be necessary bring the attention back of that user who carry more than 10 hours without subscribing by using other marketing means or campaign efforts.

We can see how by using histograms, researchers and analysts can gain insights into the distribution of data and make more informed decisions based on their findings. They are a valuable tool for data visualization and can be used to inform a variety of decisions, from identifying areas for improvement to making predictions about future trends.

## 1.3. Model Predictor Used

At the end, a Logistic Regression Model was applied to make the prediction. Logistic Regression is a statistical method used in machine learning and data analysis to predict a binary outcome (yes/no, 0/1, true/false) based on a set of independent variables. It is widely used in areas such as finance, marketing, and medicine, to name a few.

In simpler terms, Logistic Regression models the relationship between the dependent variable (the outcome we are trying to predict) and one or more independent variables (also known as predictor variables or features) by using a logistic function. The logistic function outputs a probability value between 0 and 1, which can be interpreted as the likelihood that the dependent variable is equal to 1. Based on this probability, a threshold is set to classify the outcome as either 0 or 1.

## 1.4. Programming Code Explanation

This code performs data analysis and modeling on two datasets, appdata10.csv and top_screens.csv. The main steps performed in this code are:

1.	Importing Libraries: The code imports the required libraries, including pandas for data manipulation, matplotlib.pyplot for visualizations, and seaborn for additional visualizations.
2.	Importing Data: The datasets are loaded into the code using pd.read_csv() and stored in the variables data and paginas.
3.	Data Preparation: The data is then manipulated to create new features, clean the data, and remove any unnecessary columns. This includes:

  •	Merging the two datasets
  •	Replacing the data in the screen_list column with the names of the pages visited
  •	Summing up the similar columns
  •	Grouping the data into categories (e.g. saving screens, credit screens, loan screens)
  
4.	Data Analysis: The code analyzes the data to gain insight into the data. This includes:

  •	Understanding the data format
  •	Checking for missing data
  •	Converting the hour column into an integer data type
  •	Visualizing the distribution of user ages
  •	Visualizing the hours of connection
•	Visualizing the time elapsed between subscription and opening the app

5.	Modeling: Finally, the code performs a logistic regression to predict whether a user will enroll or not based on the data. This includes:

  •	Defining the dependent and independent variables
  •	Splitting the data into training and testing sets
  •	Fitting the logistic regression model
  •	Evaluating the model’s performance using accuracy and precision scores

The code then drops some unnecessary columns and ends.

## 1.5. Conclusions

The project aimed to predict which users are likely to purchase a paid subscription based on their behavior in a mobile application. The results showed a precision of 77.66% and an accuracy of 73.75%. These findings provide valuable insights for the company to focus its attention on specific users and to explore new ways to engage those who are less likely to make a purchase. By using a machine learning model fed with the right data, it is possible to improve the processes of a company and make data-driven decisions. Overall, this project highlights the potential of using data analytics and machine learning to enhance business operations.

