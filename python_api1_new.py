import requests
import json
import os
#from dotenv import load_dotenv
import datadogapi_metrics   #importing datadogapi metrics python file


#loading VirusTotal api_key from environment viriables
#load_dotenv()
#api_key = os.getenv(‘***’)
api_key = os.environ.get('XXXXXXXXXXXXXX')

#assiging the virus total api url
url = "XXXXXXXXXXXX"

#declaring the headers for the service and passing the api_key captured from environment variable
headers = {"content-type": "application/json", "Accept-Charset": "UTF-8", "x-apikey": api_key}

#capturing the response from virustotal api service
response_API = requests.get(url, headers=headers)

data = response_API.text

#parsing the data into json format
parse_json = json.loads(data)

#capturing the values from the virustotal api response as per the required response tags
uploaded_bytes_used = parse_json['data']['attributes']['quotas']['monitor_uploaded_bytes']['used']
uploaded_bytes_allowed = parse_json['data']['attributes']['quotas']['monitor_uploaded_bytes']['allowed']
percent=uploaded_bytes_used/uploaded_bytes_allowed

#printing the values captured from api response as per the required response tags

#print("uploaded_bytes_used: ",uploaded_bytes_used)
#print("uploaded_bytes_allowed: ",uploaded_bytes_allowed)
#print("percentage: ",percent)



#passing the virustotal api values like bytes_used,bytes_allowed and percent to datadogapi_metrics python function. 

datadogapi_metrics.metrics_datadog(uploaded_bytes_used, uploaded_bytes_allowed, percent)





