"This python file contains the details related to datadog metrics api usage"

from numpy import integer
from datetime import datetime
from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.metrics_payload import MetricsPayload
from datadog_api_client.v1.model.point import Point
from datadog_api_client.v1.model.series import Series


uploaded_bytes_used = int
uploaded_bytes_allowed = int
percent = int

def metrics_datadog(uploaded_bytes_used,uploaded_bytes_allowed,percent):
        body = MetricsPayload(
            series=[
                Series(
                    metric="uploaded_bytes_used",
                    type="Count",
                    points=[
                        Point(
                            [
                                datetime.now().timestamp(),
                                uploaded_bytes_used,
                            ]
                        ),
                    ],
                    tags=[
                        "test:VirusTotal_Bytes_Used",
                    ],
                ),
            
                
                Series(
                    metric="uploaded_bytes_allowed",
                    type="Count",
                    points=[
                        Point(
                            [
                                datetime.now().timestamp(),
                                uploaded_bytes_allowed,
                            ]
                        ),
                    ],
                    tags=[
                        "test:VirusTotal_Bytes_Allowed",
                    ],
                ),

                Series(
                    metric="percent",
                    type="Count",
                    points=[
                        Point(
                            [
                                datetime.now().timestamp(),
                                percent,
                            ]
                        ),
                    ],
                    tags=[
                        "test:VirusTotal_Percent",
                    ],
                ),
            ],
        )

        configuration = Configuration()
        with ApiClient(configuration) as api_client:
            api_instance = MetricsApi(api_client)
            response = api_instance.submit_metrics(body=body)

            print(response)





