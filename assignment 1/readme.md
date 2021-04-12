# Assignment 1

## About the project
In this project, we have been asked to create a sleep log with sleep hours and active hours as the columns. And based on that we have to train the model to predict the active
hours.

### trainingdata.py
Using this, we are creating the sleep log (trainingdata.txt). We will be making a 300 points dataset.<br />

#### Our Approach
We assume that for 20 days in a month, Amit sleeps once a day and rest 10 days (8 days on weekends plus weekdays), he sleeps twice a day.
Days sleeping once= 20/30*100 = 66.66%
So, we will make the sleep log in two steps-:
1. 66.66% of 300 data points i.e.200, Amit will sleep once.
2. Rest 50 days he will sleep twice. (2*50=100)<br />
Total = 300 data points (250 days of sleep logs)<br /><br />
Considering Amit has a job and he tries to live a healthy lifestyle(6 to 8 hours of sleep is enough), we divided his sleeping hours for the first step into the following distribution-:<br />
4  hours ------- 1  percent
5  hours ------- 5  percent<br />
6  hours ------- 30 percent<br />
7  hours ------- 30 percent<br />
8  hours ------- 30 percent<br />
9  hours ------- 3  percent<br />
10 hours ------- 1  percent<br />
<br />
So his active hours will be essentially 24 - sleeping hours+(some random negative integer (-2,0)).<br /><br />


Moving on to the second step (Days when he slept twice), Considering Amit sleeps twice (if he needs), we divided his sleeping hours(night) into the following distribution-:<br />
2 hours ------- 6   percent
3 hours ------- 20  percent<br />
4 hours ------- 44  percent<br />
5 hours ------- 30  percent<br />

The amount of time he will sleep in the afternoon and his active hours before that will be highly related to the above-mentioned sleeping hours(night). <br />
For eg., if he slept only 2 hours at night, he will probably remain active for 5 to 6 hours and then will take a nap of 3 to 4 hours. Similarly, we can code for others too.
<br />
Then, we will combine both the dataset to produce "trainingdata.txt" (sleep log).

### model.py
In this, we will fit our model on the "trainingdata.py". Here, I have used Linear regression based on the simplicity of the dataset.
And the trained model will be saved as "model.pkl" and will be directly used in the app.py file. 

### app.py
Use this to run the server.

Note: I had developed an environment for that.

![image](https://user-images.githubusercontent.com/65654054/114436461-f9281580-9be2-11eb-82e3-845fa9799363.png)
