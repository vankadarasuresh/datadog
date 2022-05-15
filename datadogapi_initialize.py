import datadog
import os

def initialize_datadog():

    

        datadog.initialize(
            os.environ.get('DD_API_KEY'),
            os.environ.get('DD_APP_KEY')
        )
        print("inside initialization")
        print(os.environ.get('DD_API_KEY'))
        return True 