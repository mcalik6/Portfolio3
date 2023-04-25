
## PC Service call

Pc Service call - is mainly for thew customer point of view, where thru the terminal customer can put his details answer for 3 questions which might help to solve the problem if that wouldnot help customer would be informed about which in the queue  he is 






## How It Works 
Customer contacting service has to provide his Name, Surname and NUmber (which has to be a number)
than he is answering for 3 simple questions guiding him to fix the problem himself
if the problem is not fixed after 3 questions he will get a service call
![image](https://user-images.githubusercontent.com/116521971/234255625-089ceb62-9aaa-4ec6-958b-dd4bf7d10f24.png)


## Features 

program is sening information to pending sheet in google sheets
if all of the answers are Yes - it means that turning computer of and on solved the problem
otherwise costomer will have to get a call - in that case he will be getting call asap or if there is a queue 
he will get a number saying which number he is in the queue 

I am assuming that on the other side would be somebody eho can have an access to spredsheet and after a call to change his status from 0 to 1

## Future features

while customer is using the first app and service team is using spreadsheet
there can be the ather app created for the service team getting the first details of the customer and by terminating the program it will change customer status in pending from 1 to 0 

so two apps would be using the same spreadsheet one would be adding 1 if its needed the other one would be changing that to 0 

## Data Model

There is a couple of simple functions sending info to spreadsheet
one test - which result gives 0 or 1 to the spreadsheet get_pending - with if function
and based on result customer would be serviced or there is no need for service 

## Testing

I passed the code thru pep8 - and I got a lot of mistakes related to white spaces, blank lines and lines to long 
a removed white spaces and I removed lines to long by adding \n 

![image](https://user-images.githubusercontent.com/116521971/234256834-abfbab71-c144-4210-a919-bc64ba0fff7d.png)

## Deployement

Project was doployed on heroku





![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
