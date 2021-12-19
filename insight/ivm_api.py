from json.encoder import JSONEncoder
import os
from typing import Dict
import requests
import json
from dotenv import load_dotenv
from sys import exit
import base64

# Global Variables
DEBUG = True # set to True if you want a little more output for troubleshooting purposes

# get the credentials from a different file, don't store in the code
# retrieve via .env file
load_dotenv()
USER = os.getenv("USER_NAME")
PASS = os.getenv("PASS")
URL = os.getenv("URL")

##### BEGIN==== Function definitions

def encode_auth_header() -> json:

    encode_string = "{}:{}".format(USER,PASS)

    encode_string_bytes = encode_string.encode("ascii")

    base64_bytes = base64.b64encode(encode_string_bytes)
    base64_string = base64_bytes.decode("ascii")


    if DEBUG:
        print(f"Encoded string: {base64_string}")

    # Authorization URL give us an AUTH_TOKEN
    header = {"Content-Type": "application/json; charset=utf-8", "Authorization": "Basic {}".format(base64_string)}

    resp = requests.get(URL, headers=header, verify=False)
    print(f'http_status_code for auth/: {str(resp.status_code)}')

    return header

# helper function to dump data
# expects a json object
def print_results(resp: json) -> None:
    data = json.loads(resp.text)
    print(json.dumps(data, indent=4, sort_keys=True))

##### END==== Function definitions


############################################## Script begins here ###################################
# uncomment the function you want to run - please read the function def for required parameters
def main():

    print("Running...")
    # Lets get a token for use in all our api calls
    header = encode_auth_header()
    if DEBUG:
        print(header)

    print("Completed....")

if __name__ == "__main__":
    main()