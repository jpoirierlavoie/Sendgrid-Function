import os
import json
import sendgrid
from flask import Flask, request

def sendgrid_function(request):
#if request.method == "POST":
        message = {
            "personalizations": [
                {
                    "to": [
                        {
                            "email": os.environ["TO_ADDRESS"],
                            "name": os.environ["TO_NAME"]
                        }
                    ],
                    "subject": os.environ["SUBJECT"] 
                }
            ],
            "from": {
                "email": os.environ["FROM_ADDRESS"],
                "name": request.form["name"]
            },
            "reply_to": {
                "email": request.form["email"],
                "name": request.form["name"]
            },
            "content": [
                {
                    "type": "text/plain",
                    "value": request.form["message"]
                }
            ]
        }
        sg = sendgrid.SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
        response = sg.send(message)
        if response.status_code == 202:
            return "Email sent successfully"
        else:
            return "Status Code: " + str(response.status_code)
#else:
#        error = "Invalid Method. Only POST methods are accepted."