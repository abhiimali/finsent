import streamlit as st
import json
import requests
from datetime import datetime, timedelta

# Define the main function
def news_summary():
    print("heyy")
    st.title('Welcome to fiNSHORT')

    # Search input on the main page
    st.header('Search')
    search = st.text_input('Enter your favorite stock tick:')
    submitted = st.button("Search")

    # Fetch articles based on search query
    if submitted:
        try:
            url = "https://yahoo-finance-india1.p.rapidapi.com/market_india/news/"
            querystring = {"symbol":search}
            headers = {
                "X-RapidAPI-Key": "5b79605ad3msh2189bb7a6a8f4e3p18496ajsn690351c19b9c",
                "X-RapidAPI-Host": "yahoo-finance-india1.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            print(response.json)
            response_dict = json.loads(response.text)

            # Display articles and summaries on the same page
            print(response_dict)
            if response_dict == []:
                st.error(f'No News Available For Stock {search}')
            else:
                display_summaries(response_dict)

        except Exception as e:
            st.error("An error occurred. Please try again later. Insufficient data")

# Function to display summaries
def display_summaries(articles):
    st.title('Summaries')
    st.write("Here are the summaries of the articles:")

    # Display summaries
    for article in articles:
        st.header(article['title'])
        st.subheader('Summary of Article')
        st.write(article['summary'])
        st.write(f"Published by: {article['publisher_name']}")
        st.write(f"Published time: {datetime.utcfromtimestamp(article['published_time'] // 1000)}")
        st.write(f"Source URL: {article['source_url']}")
        st.markdown("---")

