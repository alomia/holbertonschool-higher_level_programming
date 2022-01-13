#!/usr/bin/python3
"""What's my status? #1"""

if __name__ == "__main__":
    import requests
    response = requests.get("https://intranet.hbtn.io/status")
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
