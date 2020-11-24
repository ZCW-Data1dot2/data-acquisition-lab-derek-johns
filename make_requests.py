import time
import requests
import os
import json
from requests.exceptions import HTTPError

URL = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations'
TOKEN = os.environ.get('NOAA_KEY')


def url_to_json(url):
    """
    Function will make a call to NOAA api and save data to json file
    :param url: str representing url to request data from
    :return: None
    """
    for i in range(39):
        try:
            offset_url = f'{url}?offset={i * 1000 + 1}&limit=1000'
            response = requests.get(offset_url,
                                    headers={
                                        'token': TOKEN
                                    })
            r = response.json()
            f_name = f'locations_{i}.json'
            with open(f_name, 'w') as f:
                json.dump(r, f)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Success!')
        time.sleep(3)


def main():
    url_to_json(URL)


if __name__ == '__main__':
    main()

