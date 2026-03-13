import requests
import logging
from datetime import datetime

# configure logging
logging.basicConfig(
    filename="api_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=5)

        # check status code
        if response.status_code != 200:
            logging.error(f"API returned non-success status: {response.status_code}")
            return None

        return response.json()

    except requests.exceptions.ConnectionError as e:
        logging.error(f"Network connection failed: {e}")

    except requests.exceptions.Timeout as e:
        logging.error(f"API request timed out: {e}")

    except requests.exceptions.RequestException as e:
        logging.error(f"General API error: {e}")

    return None


# example test
data = fetch_api_data("https://jsonplaceholder.typicode.com/users")
print(data[:1] if data else "No data fetched")
