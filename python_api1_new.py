import requests
import json
import os
#from dotenv import load_dotenv
import datadogapi_metrics   #importing datadogapi metrics python file


#loading VirusTotal api_key from environment viriables
#load_dotenv()
#api_key = os.getenv(‘***’)
api_key = os.environ.get('XXXXXXXXXXXXXX')

url = "XXXXXXXXXXXX"

headers = {"content-type": "application/json", "Accept-Charset": "UTF-8", "x-apikey": api_key}

response_API = requests.get(url, headers=headers)
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
#.data.attributes.quotas.monitor_uploaded_bytes.used
uploaded_bytes_used = parse_json['data']['attributes']['quotas']['monitor_uploaded_bytes']['used']
uploaded_bytes_allowed = parse_json['data']['attributes']['quotas']['monitor_uploaded_bytes']['allowed']
percent=uploaded_bytes_used/uploaded_bytes_allowed


print("uploaded_bytes_used: ",uploaded_bytes_used)
print("uploaded_bytes_allowed: ",uploaded_bytes_allowed)
print("percentage: ",percent)



#passing the virustotal api values like bytes_used,bytes_allowed and percent

datadogapi_metrics.metrics_datadog(uploaded_bytes_used, uploaded_bytes_allowed, percent)





