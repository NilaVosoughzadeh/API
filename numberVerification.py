import requests

print("Ex. 0098xxxxxxxxxx")
phone = input("Enter your phone number : ")

url = f"https://api.apilayer.com/number_verification/validate?number={phone}"

payload = {}
headers= {
  "apikey": "GM0YJz7bD3XGfvK7r0RfQRqf0JMsChnA"
}

response = requests.request("GET", url, headers=headers, data = payload)

# result = response.text

#فرمت انتقال اطلاعات بین API
result = response.json()

print(result)
print("------------------------------------------------------------------------------------------------------------------------------------------------------")
print(result['valid'])
print(result['number'])
print(result['local_format'])
print(result['international_format'])
print(result['country_prefix'])
print(result['country_code'])
print(result['country_name'])
print(result['carrier'])