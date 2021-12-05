import requests

if __name__ == "__main__":
    resp = requests.get("https://www.myfitnesspal.com/")
    print(resp.text)
