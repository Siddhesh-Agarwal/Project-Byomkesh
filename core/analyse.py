import tweepy
from pandas import Series
from textblob import TextBlob


def clean(text: str) -> str:
    arr = text.lower().split()
    tetx = " ".join(arr)
    cleaned = ""
    for i in tetx:
        if i.isalnum() or i.isspace():
            cleaned += i
    return cleaned


def classify(text: str, patience: float = 0.15) -> int:
    """
    classify the text into positive, negative or neutral

    Parameters
    ----------
    text : str
        The text to be classified

    Returns
    -------
    int
        -1 for negative, 0 for neutral and 1 for positive
    """

    wiki = TextBlob(text)
    polarity = wiki.sentiment.polarity
    if polarity < -patience:
        return -1
    if polarity > patience:
        return 1
    return 0


def analyze_user(username: str, count: int = 100) -> list:
    """
    analyzes the tweets of the user

    Parameters
    ----------
    username : str
        The twitter username of a person.
    count : int, optional
        The number of tweets to be analyzed, by default 100

    Returns
    -------
    pandas.Series
        The series contains the count of positive, negative and neutral tweets
    """

    consumerKey = "TEQFrdbSGCbvi2kchzF82Cx67"
    consumerSecret = "b9xHHubPbKsGPOhwTqznh6xt8oAO3Noqo5R9nmgJCIrHpDxcPg"
    accessToken = "1266960995869618176-1fiUMxF6YniwRytzIKpiOOHhpykceH"
    accessTokenSecret = "Y6wAIo3HjcfpzfN9RLKDCKlDWYpsLVPWGSzXoG8jXFrAx"

    # Create the authentication object
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    # Create the API object while passing in auth information
    api = tweepy.API(auth)

    # extract a users timeline
    tweets = api.user_timeline(screen_name=username, count=count)
    # return len(tweets)
    # return tweets
    arr = []
    for tweet in tweets:
        arr.append(classify(clean(tweet.text)))

    # return value
    return Series(arr).value_counts()
