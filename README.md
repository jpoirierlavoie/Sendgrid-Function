# Sendgrid Cloud Function

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/82c15ca64036429690a6eb14d9695539)](https://app.codacy.com/manual/jason_46/sendgrid-cloud-function?utm_source=github.com&utm_medium=referral&utm_content=jpoirierlavoie/sendgrid-cloud-function&utm_campaign=Badge_Grade_Dashboard)
[![CodeFactor](https://www.codefactor.io/repository/github/jpoirierlavoie/sendgrid-cloud-function/badge)](https://www.codefactor.io/repository/github/jpoirierlavoie/sendgrid-cloud-function)
[![Known Vulnerabilities](https://snyk.io/test/github/jpoirierlavoie/sendgrid-cloud-function/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/jpoirierlavoie/sendgrid-cloud-function?targetFile=requirements.txt)

This is a python script designed to be run on Google Cloud's server-less cloud functions. It relies on Sengrid Mail API to send emails. An account and API key are required prior to using.

## Requirements
-   Sendgrid account;
-   Google Cloud platform account; and
-   A domain with access to DNS records (CNAME and TXT).

## Instructions
gcloud kms encrypt --keyring=global --key=envvars --plaintext-file=envvars.decrypted --ciphertext-file=envvars.encrypted --location=global
