import os
import sendgrid
import json
from urllib.parse import urlencode
from urllib.request import urlopen

def recaptcha_validation(request):

    recaptchaURI = "https://www.google.com/recaptcha/api/siteverify"
    recaptcha_response = request.form.get("recaptcha_response", None)
    recaptcha_secret = os.environ["RECAPTCHA_SECRET"]
    remote_ip = request.remote_addr
    params = urlencode({
        "secret": recaptcha_secret,
        "response": recaptcha_response,
        "remote_ip": remote_ip,
        })
    data = urlopen(recaptchaURI, params.encode("utf-8")).read()
    result = json.loads(data)
    success = result.get("success", None)

    if success is True:
        return "Recaptcha passed."
    return "Recaptcha failed."

def sendgrid_function(request):

    if request.method == "POST":
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
            return "Email sent successfully."
        return "Status Code: " + str(response.status_code)
    return "Invalid Method. Only POST methods are accepted."
