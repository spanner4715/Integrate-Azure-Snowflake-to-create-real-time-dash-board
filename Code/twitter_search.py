import requests
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from datetime import datetime
datetime = datetime.now().strftime("%Y_%m_%d_%I:%M:%S")

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAIquiQEAAAAAzp4gVxwrIr7Up1Eixq%2Fh4QOC3%2Bk%3DwzkoXSBr2yzpMZzrMFYVmCqfTaVAPi6fWqOdVVaie4NkdvnxTc'
conn_string="DefaultEndpointsProtocol=https;AccountName=snowpipeline2022;AccountKey=WC0DUo3H78nlmIwngeU8dOigO6tqRX6fSe+1B9ADQER2dF09LN46+HafN5/J0RsAzDcqvjQkDr3j+ASt8qSiNQ==;EndpointSuffix=core.windows.net"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id,public_metrics'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    container_client = ContainerClient.from_connection_string(conn_string,container_name="twitter")
    container_client.upload_blob(f"files/twitter_{datetime}.json",data=json.dumps(json_response))
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()