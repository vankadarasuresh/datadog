import requests
import json
import datadogapi_metrics_new

response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print("Active cases in South Andaman:", active_case)

#datadogapi_metrics.metrics_datadog(500,500,1010.12)

datadogapi_metrics_new.metrics_datadog(5000,5000,1010.12)

