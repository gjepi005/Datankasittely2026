import requests as rq

def fetch_data(api_url):
    try:
       data =rq.get(api_url)
       data.raise_for_status()
       return data.json()
    except rq.exceptions.HTTPError as e:
        if e.response is not None:
            status = e.response.raise_for_status()
        else:
            status = "unknown"
        print("HTTPError... " + status + " " + e)
        return None
    except Exception as e:
        print("something went wrong... " + e)
        return None


# TODO: 
# Import requests library
# Define fetch_data function, that takes an API URL as parameter
# Use try - except structure to
# - make a GET request to the given URL with the requests library,
# - raise an exception if the response status code indicates an error,
# - return the response data as JSON
# - print an error message if something goes wrong with the request, and return None.
