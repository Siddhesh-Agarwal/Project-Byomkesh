import requests


class APIFailException(Exception):
    def __init__(self, status_code: int, text: str) -> None:
        self.status_code = status_code
        self.text = text
        super().__init__(f"API failed with status code {status_code} and text {text}.")


def display_tweet(URL: str) -> str:
    """
    display_tweet _summary_

    Parameters
    ----------
    URL : str
        The URL of the tweet who HTML is needed

    Returns
    -------
    str
        The HTML of the twee

    Raises
    ------
    APIFailException
        Raised if the API fails
    """

    API_URL = f"https://publish.twitter.com/oembed?url={URL}"
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise APIFailException(response.status_code, response.text)
    res = response.json()["html"]
    return res
