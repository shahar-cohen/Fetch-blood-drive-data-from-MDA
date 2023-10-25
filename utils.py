import csv
from datetime import date

# POST request params for blood donation info:
# URL and headers
url = "https://www.mdais.org/umbraco/api/invoker/execute"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "he",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.mdais.org/blood-donation",
    "Origin": "https://www.mdais.org",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}

# data payload
request_data = {
    "RequestHeader": {
        "Application": 101,
        "Module": "BloodBank",
        "Function": "GetAllDetailsDonations",
        "Token": "",
    },
    "RequestData": "",
}

# cookies
cookies = {
    "GCLB": "CIHqosus677UTg",
    "rbzid": "WU+SClwF++SKT8eqetr6gBEfI6nmhzMBmRKA5iYCoxg29VpphFLwjnKNYNUSGRvsnUaohyJHgmeLzY2QGjhsrTkUV/d1JOI0yVN/2zHpSqtDYaM7mRFhSv0QD+/7zYFwJw7jc1iiEuQRe7TBBjlalsjXfGtnSHwFKC4UKyrjtWcVUcEbI4UjnIC97+BsYgt9",
    "rbzsessionid": "c0541fd67af4d9a2423850c36d522f88",
    "_gcl_au": "1.1.1705533538.1698159629",
    "_ga_DKP4FMJYBL": "GS1.1.1698164234.2.1.1698164238.56.0.0",
    "_ga": "GA1.2.1445825577.1698159629",
    "_gid": "GA1.2.586909759.1698159630",
    "_tt_enable_cookie": "1",
    "_ttp": "SuUD8-0OT9ZF-Ona4R0t63t4M4K",
}


# write json data to csv
def save_data_to_csv(data, filename='data.csv'):
    # Write the data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header (field names)
        header = data[0].keys()
        csv_writer.writerow(header)

        # Write the data
        for row in data:
            csv_writer.writerow(row.values())
