from astrapy import DataAPIClient
import os

def get_database_client():
    # Initialize Astra DB client
    client = DataAPIClient(os.getenv("TOKEN"))
    db = client.get_database_by_api_endpoint(
        "https://b91613e6-2268-4794-a0c3-7a6dce463a0f-us-east-2.apps.astra.datastax.com"
    )
    return db