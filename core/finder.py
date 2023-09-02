import tweepy  # type: ignore
from typing import Any


def find_tweet(search_tweet: str, until: str) -> list[Any]:
    """
    find_tweet


    Parameters
    ----------
    search_tweet : str
        The tweet text to be searched
    count : int
        The number of tweets to be returned

    Returns
    -------
    List[dict]
        the output is the first 3 people to send that exact tweet
    """

    consumerKey = "TEQFrdbSGCbvi2kchzF82Cx67"
    consumerSecret = "b9xHHubPbKsGPOhwTqznh6xt8oAO3Noqo5R9nmgJCIrHpDxcPg"
    accessToken = "1266960995869618176-1fiUMxF6YniwRytzIKpiOOHhpykceH"
    accessTokenSecret = "Y6wAIo3HjcfpzfN9RLKDCKlDWYpsLVPWGSzXoG8jXFrAx"

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)

    # Create the authentication object
    auth.set_access_token(accessToken, accessTokenSecret)  # type: ignore

    # Create the API object while passing in auth information
    api = tweepy.API(auth)

    # Create a tweet
    tweets = api.search_tweets(  # type: ignore
        q=search_tweet,
        result_type="recent",
        until=until,
    )

    # return tweets
    arr = []
    for tweet in tweets:  # type: ignore
        arr.append(tweet._json)  # type: ignore
    # sort array
    arr.sort(reverse=True, key=lambda x: x["created_at"])  # type: ignore

    return arr  # type: ignore
