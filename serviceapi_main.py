import requests

import json

import os

import Datadogapi_Metrics  #importing datadogapi metrics python file



#loading VirusTotal api_key from environment viriables

api_key = os.environ.get('virustotal_apikey')



#assiging the virus total api url

url = “******************”



#declaring the headers for the service and passing the api_key captured from environment variable

headers = {"content-type": "application/json", "Accept-Charset": "UTF-8", "x-apikey": api_key}







def virustotal_api_call():

    



    #capturing the response from virustotal api service

    response_API = requests.get(url, headers=headers)



    if response_API.status_code == 200:   #Checking if the API response is success or not

        

        data = response_API.text



        #parsing the data into json format

        parse_json = json.loads(data)



        #capturing the values from the virustotal api response as per the required response tags

        uploaded_bytes_used = parse_json['data']['attributes']['quotas']['monitor_uploaded_bytes']['used']

        uploaded_bytes_allowed = parse_json['data']['attributes']['quotas']['monitor_uploaded_bytes']['allowed']

        percent=uploaded_bytes_used/uploaded_bytes_allowed



        return uploaded_bytes_used,uploaded_bytes_allowed,percent   #Returning the API response values

    else:

        return None,None,None    #Returning API response values as none when the API response status is failed





if __name__ == "__main__":



    #Capturing the API response values

    uploaded_bytes_used,uploaded_bytes_allowed,percent = virustotal_api_call()





    #If the API call is failed then Datadog Metrics API won't be called

    if (uploaded_bytes_used is not None) or (uploaded_bytes_allowed is not None) or (percent is not None):

        Datadogapi_Metrics.metrics_datadog(uploaded_bytes_used, uploaded_bytes_allowed, percent)