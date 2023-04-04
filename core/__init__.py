from core.analyse import analyze_user
from core.display import display_tweet
from core.finder import find_tweet
from core.instaget import advanced_lookup as get_insta_info


def create_URL(username: str, tweet_id: str) -> str:
    """
    create_URL Creates the tweets URL based on Username and tweet ID

    Parameters
    ----------
    username : str
        The twitter username of the tweet's Author
    tweet_id : str
        The ID of the tweet

    Returns
    -------
    str
        The URL of the tweet
    """

    URL = f"https://twitter.com/{username}/status/{tweet_id}"
    return URL
