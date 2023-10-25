# makes a request for blood drive information from Magen David Adom's website
# saves the data relevant for today's blood drive as a csv file

import json
from datetime import datetime, date
import requests

from utils import url, request_data, headers, cookies, save_data_to_csv


def get_blood_drive_data(required_date):
    # Send the POST request with data, headers, and cookies
    response = requests.post(url, json=request_data, headers=headers, cookies=cookies)
    # Check the response status code and content
    if response.status_code == 200:
        response_data = response.json()
        result_data = json.loads(response_data["Result"])

        res = list()

        for blood_drive in result_data:
            date_string = blood_drive['DateDonation']

            # Parse the date-time string into a datetime object
            date_time = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")

            # Compare the date part of the parsed date-time with the requested date
            if date_time.date() == required_date:
                res.append(blood_drive)

        return res

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

        return []


if __name__ == '__main__':
    # today's date
    today = date.today()

    blood_drives_today = get_blood_drive_data(required_date=today)
    filename = f'blood_donations_for_{today}.csv'
    save_data_to_csv(data=blood_drives_today, filename=filename)
