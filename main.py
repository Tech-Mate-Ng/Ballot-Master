import base64
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)


def download_data_url(url, filename):
    header, data = url.split(",", 1)
    file_data = base64.b64decode(data)
    with open(filename, "wb") as file:
        file.write(file_data)
    print(f"Downloaded {filename}")


def get_credentials(i):
    return os.getenv(f"USER{i}_USERNAME"), os.getenv(f"USER{i}_PASSWORD")


number_of_users = os.getenv("NUMBER_OF_USERS")

for i in range(1, int(number_of_users) + 1):
    username, password = get_credentials(i)
    with requests.Session() as s:
        url = "http://studentportalbeta.unilag.edu.ng/users/login"

        response = s.get(url)
        response = s.post(url, data={"MatricNo": username, "Password": password})
        # Set the '_auth' key sessionStorage to json response
        s.cookies["_auth"] = response.text
        general_header = {
            "Authorization": f"Bearer {json.loads(response.text)['Data']['Token']}",
            "Content-Type": "application/json",
            "Host": "studentportalbeta.unilag.edu.ng",
            "Referer": "http://studentportal.unilag.edu.ng/",
        }
        # Get the payment status
        # response = s.get(
        #     url="http://studentportalbeta.unilag.edu.ng/payments/refereshStatus",
        #     data={
        #         "Authorization": f"Bearer {json.loads(response.text)['Data']['Token']}"
        #     },
        #     headers=general_header,
        # )
        # print(response.text)
        response = s.get(
            "http://studentportalbeta.unilag.edu.ng/payments/reciept",
            data={
                "Authorization": f"Bearer {json.loads(response.text)['Data']['Token']}"
            },
            headers=general_header,
        )
        res = json.loads(response.text)
        if res["Success"]:
            download_data_url(
                f"data:application/octet-stream;base64,{res['Data']['Data']}",
                res["Data"]["Name"],
            )
