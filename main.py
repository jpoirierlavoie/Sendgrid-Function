import sendgrid
import os
from flask import Flask, request

sg = sendgrid.SendGridAPIClient(os.environ["SENDGRID_API_KEY"])

def sendgrid_function(request):
    if request.method == "POST":
        data = {
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
            ],
            "personalizations": [
                {
                    "to": [
                        {
                            "email": os.environ["ADMIN_ADDRESS"],
                            "name": os.environ["ADMIN_NAME"]
                        }
                    ],
                    "subject": os.environ["SUBJECT"]  + request.form["subject"]
                }
            ]
        }

        response = sg.client.mail.send.post(request_body=data)
        if response.status_code == 202:
            return ("Email sent successfully.", 200, headers)
        return ("Something went wrong. Status Code: " + str(response.status_code), headers)
    return "Invalid Method. Only POST methods are accepted."
