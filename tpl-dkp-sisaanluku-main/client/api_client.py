import requests

def fetch_data(api_url):
    try:
       data =requests.get(api_url)
       data.raise_for_status()
       return data.json()
    except requests.exceptions.HTTPError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None
    except Exception as e:
        print(e)
        return None


# TODO: 
# Import requests library
# Define fetch_data function, that takes an API URL as parameter
# Use try - except structure to
# - make a GET request to the given URL with the requests library,
# - raise an exception if the response status code indicates an error,
# - return the response data as JSON
# - print an error message if something goes wrong with the request, and return None.
