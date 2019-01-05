
# Authentication
import requests
from requests.auth import HTTPBasicAuth



# Authentication
consumer_key = "L22MJEJV73t5eGHqwN2U9xzAtAnUvMpF"
consumer_secret = "QDAge4n5C8Wd6GAG"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print (r.text)

#HTTP Header Parameters
