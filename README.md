# Microservice
Project for microservice

Marie Knapp
CS 361 – Summer 2022


README- Microservice for ACT Subtest Grading

A.	Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.

1)	You’ll need to save the student answers as a list.  Each item in the list should be a string with the letter of the student answer.  Indices are number of the test item - 1.  There should be 60 items in the list.  Questions left unanswered can be entered as ‘X’.

Example:

Student responses:
Question 1 – A
Question 2 – C
Question 3- no response
Question 4- E

student_response_example = [‘A’,  ‘C’,  ‘X’ , ‘E’, …] 
2)	The following imports are needed:
import flask
from flask import request, jsonify
import requests
import json

3)	Set the URL to the following:
# api-endpoint
URL = "http://127.0.0.1:5000/grade

4)	Create a dictionary with the type of test set to Math73F and the list of student answers.

Example:
ans = {
    "test_type": "Math73F",
    "student_answers": student_response_example
    }

5)	Send the request in this format:
# get request and response (r)
r = requests.get(url = URL, params= ans)
  

6)	Begin running the microservice by saving the microservice.py file and running it from the command line with:

python3  microservice.py

B.	Clear instructions for how to RECEIVE data from the microservice you implemented
Send the get request and then convert the scores to a json format.  From there, you can parse the JSON file to get the needed data:

#get scores as a json file
scores = r.json()
print(scores)
Start a new process, and save and run this file (while the microservice.py file runs in a separate process). 
Return example:
{'correct_answer_count': 54, 'incorrect_answer_count': 6, 'percent_correct': 90.0, 'scaled_projection': 32, 'test_type': 'Math73F'}

JSON contains:
‘correct_answer_count’ = number of correctly answered questions
‘incorrect_answer_count’ = number of incorrect or unanswered questions
‘percent_correct’ = percent of correct answers out of all questions
‘scaled_projection’ = projected ACT scaled score
‘test_type’ = name of subtest sent for grading

C.	UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand


![image](https://user-images.githubusercontent.com/2553846/180666405-d2030dc6-dd50-4f90-87f6-4e90b0b8fcf1.png)
