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

