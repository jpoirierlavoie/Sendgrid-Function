# Sendgrid Cloud Function

This is a python script designed to be run on Google Cloud's server-less cloud functions. It relies on Sengrid Mail API to send emails. An account and API key are required prior to using.

## Requirements
-   Sendgrid account;
-   Google Cloud platform account; and
-   A domain with access to DNS records (CNAME and TXT).

## Instructions
gcloud kms encrypt --keyring=envvars --key=cloud-function --plaintext-file=envvars.decrypted --ciphertext-file=envvars.encrypted --location=northamerica-northeast1
