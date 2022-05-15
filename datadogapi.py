"""
Submit metrics returns "Payload accepted" response
"""

from datetime import datetime
from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.model.metrics_payload import MetricsPayload
from datadog_api_client.v1.model.point import Point
from datadog_api_client.v1.model.series import Series

body = MetricsPayload(
    series=[
        Series(
            metric="UploadUsage",
            type="Count",
            points=[
                Point(
                    [
                        datetime.now().timestamp(),
                        15,
                    ]
                ),
            ],
            tags=[
                "test:ExampleSubmitmetricsreturnsPayloadacceptedresponse",
            ],
        ),
    
        
        Series(
            metric="downloadUsage",
            type="Count",
            points=[
                Point(
                    [
                        datetime.now().timestamp(),
                        20,
                    ]
                ),
            ],
            tags=[
                "test:Testing",
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_metrics(body=body)

    print(response)