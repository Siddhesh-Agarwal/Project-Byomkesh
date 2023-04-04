import re
import plotly.express as px
import requests
import streamlit as st
import streamlit.components.v1 as components
from core import analyze_user, create_URL, display_tweet, find_tweet, get_insta_info

st.set_page_config(
    page_title="Byomkesh",
    page_icon=":mag:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title(":mag: Byomkesh")

tools = st.tabs(
    [
        "Tweet Finder",
        "Twitter Profile Analyzer",
        "Instagram Info",
        "Website Info",
    ]
)

# TWEET FINDER
with tools[0]:
    st.subheader("Tweet Finder")

    tweet_text = st.text_area(
        label="Enter Tweet Text",
        height=120,
        max_chars=280,
        help="Enter the text of the tweet you want to find and get statistics about",
    )
    number = 1
    before = st.date_input("Before")

    if st.button("Search", key="submit-0"):
        if tweet_text:
            # st.write(before)
            with st.spinner(f"Searching for Data ..."):
                results = find_tweet(tweet_text, before)

                # st.write(results)
                likes, retweets = 0, 0
                for result in results:
                    try:
                        likes += result["retweeted_status"]["favorite_count"]
                        retweets += result["retweeted_status"]["retweet_count"]
                    except KeyError:
                        pass
                if likes == 0 and retweets == 0:
                    st.error("No results found")
                else:
                    cols = st.columns(3)
                    with cols[0]:
                        st.metric("Likes", f'{likes:,}')
                    with cols[1]:
                        st.metric("Retweets", f'{retweets:,}')
                    with cols[2]:
                        st.metric("Copies", f'{len(results)-1:,}')
                    
                    for result in results[:number]:
                        URL = create_URL(result["user"]["id"], result["id"])
                        components.html(display_tweet(URL), height=850)
        else:
            st.error("Please enter some text")


# TWITTER PROFILE ANALYZER
with tools[1]:
    st.subheader("Twitter Profile Analyzer")
    username = st.text_input(
        label="Enter Twitter Username",
        max_chars=15,
        placeholder="Username",
        help="Enter the username of the Twitter profile you want to analyze",
    )
    press = st.button("Analyze", key="submit-1")
    if press:
        if username:
            with st.spinner(f"Analyzing {username}..."):
                results = analyze_user(username)
                
                # Draw a pie chart of the results
                # +0 - neutral - blue
                # +1 - positive - green
                # -1 - negative - red
                fig = px.pie(
                    values=results,
                    names=["Positive", "Neutral", "Negative"],
                    color_discrete_sequence=["#199554", "#2664F5", "#CC0202"],
                    title=f"Sentiment Analysis of @{username}",
                )
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Please enter a username")


# INSTAGRAM INFORMATION
with tools[2]:
    st.subheader("Instagram Information")
    
    username = st.text_input(
        label="Enter Instagram Username",
        placeholder="Username",
        help="Enter a username to get information about the account",
    )
    
    if st.button("Search", key="submit-3"):
        if username:
            res = get_insta_info(username)
            st.write(res)
        else:
            st.error("Please enter a username")


# WEBSITE INFORMATION
with tools[3]:
    st.subheader("Websites details")

    website = st.text_input(
        label="Enter a website",
        placeholder="www.example.com",
        type="default",
        help="Enter a website name to get information about Domain and Registrant",
    )

    if st.button("Search", key="submit-4"):
        website = website.replace("https://", "")
        website = website.replace("http://", "")
        website = website.replace("www.", "")
        if website:
            # regex validation
            if re.match(r"^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", website):
                with st.spinner("Searching..."):
                    URL_DATA = f"https://www.whois.com/whois/{website}"
                    # st.write(URL)
                    rd = requests.get(URL_DATA)
                    # st.write(r.status_code)

                    if rd.status_code == 200:
                        # Information about the domain and registrar
                        text = rd.content.decode("ascii")
                        # st.code(text, language="html")

                        # find all data in <div class="df-label"> and <div class="df-value"> and put them in a list
                        data = re.findall(
                            r'<div class="df-label">(.+?)</div><div class="df-value">(.+?)</div>',
                            text,
                        )

                        # create a dictionary
                        res = {}
                        for i in data:
                            res[i[0].replace(":", "")] = i[1]

                        # delete "email", if present
                        if "Email" in res.keys():
                            del res["Email"]

                        # if "Status" is present, create a list
                        if "Status" in res.keys():
                            res["Status"] = res["Status"].split("<br>")

                        # if "Name Servers" is present, create a list
                        if "Name Servers" in res.keys():
                            res["Name Servers"] = res["Name Servers"].split("<br>")

                        # display the dictionary
                        st.write(res)
                    else:
                        st.error("❗ Information not found.")
            else:
                st.error("❗ Please enter a valid website")
        else:
            st.error("❗ Please enter a website")
