import requests
import json


def main():
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    r = requests.get(url)
    print("Status code :", r.status_code)
    response_dicts = r.json()
    json_dicts = json.dumps(response_dicts, indent=4, ensure_ascii = False)
    print(json_dicts)


if __name__ == "__main__":
    main()