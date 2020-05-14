import os
import sendgrid
import json
from flask import Flask, request
from urllib.parse import urlencode
from urllib.request import urlopen

def sendgrid_function(request):
    if request.method == "OPTIONS":
        headers = {
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)
    if request.method == "POST":
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600"
        }
        message = {
            "personalizations": [
                {
                    "to": [
                        {
                            "email": os.environ["TO_ADDRESS"],
                            "name": os.environ["TO_NAME"]
                        }
                    ],
                    "subject": os.environ["SUBJECT"]  + request.form["subject"]
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
            return ("Email sent successfully.", 200, headers)
        return ("Something went wrong. Status Code: " + str(response.status_code), headers)
    return "Invalid Method. Only POST methods are accepted."
