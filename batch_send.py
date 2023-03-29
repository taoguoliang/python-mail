# import requests

url = 'https://lift-api.vfsglobal.com/user/registration'
# wd = input('enter something of English:')
data = {
    "emailid": "abc12345@taoz.xyz",
    "password": "Abc#12345",
    "confirmPassword": "Abc#12345",
    "instructionAgreed": 'true',
    "missioncode": "deu",
    "countrycode": "chn",
    "url": "https://visa.vfsglobal.com/chn/en/deu/activateemail?q=",
    "cultureCode": "en-US"
}

from curl_cffi import requests

# 注意 impersonate 这个参数
# r = requests.get("https://tls.browserleaks.com/json", impersonate="chrome110")
#
# print(r.json())

headers = {
    'origin': 'https://visa.vfsglobal.com',
    'authority': 'lift-api.vfsglobal.com',
    'content-type': 'application/json;charset=UTF-8',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

response = requests.post(url=url,json=data,headers=headers, impersonate="chrome101")
print(response.status_code)
print(response.json())


