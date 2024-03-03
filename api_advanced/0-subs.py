#!/usr/bin/python3
"""Query the Reddit API to get the number of subscribers for a subreddit."""
import requests

def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for the given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My API advanced 1.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0  # Invalid JSON structure
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0  # Error during request

# Example usage:
subreddit = "python"
print(f"Number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}")

