#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Function that fetches number_of_subscribers"""
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # Check if the status code indicates success (200)
        if response.status_code == 200:
            return response.json().get("data").get("subscribers")
        elif response.status_code == 404:
            return f"The subreddit '{subreddit}' does not exist."
        else:
            return "Failed to retrieve subscriber count."

    except Exception as e:
        print("An error occurred:", e)
        return 0

# Test with existing and non-existing subreddits
existing_subreddit = "python"
non_existing_subreddit = "nonexistingsubreddit123"

print("Number of subscribers in the existing subreddit:", number_of_subscribers(existing_subreddit))
print("Number of subscribers in the non-existing subreddit:", number_of_subscribers(non_existing_subreddit))

