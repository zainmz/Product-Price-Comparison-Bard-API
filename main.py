import streamlit as st
import pandas as pd
import os
import requests
import re
from bardapi import Bard

os.environ['_BARD_API_KEY'] = 'XXXXXXXXXXXX'

session = requests.Session()
session.headers = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

bard = Bard(session=session, timeout=30)


# Function to search for the lowest price using Bard API
def get_lowest_price(product_name):
    # API endpoint for Bard API
    try:
        result = \
        bard.get_answer("Get the lowest price for " + product_name + " in Sri Lanka, please give site links aswell")[
            'content']

        # Remove commas from the text
        result = result.replace(',', '').replace('*', '').replace(":", " ")
        print(result)

        # Define the regular expression pattern
        pattern = r'Rs\. (\d+)'

        # Find all matches using the pattern
        matches = re.findall(pattern, result)

        if matches:
            # Print the matching values
            for match in matches:
                print(match)
        else:
            matches = "None"

        # Define the regular expression pattern
        pattern2 = r'(?:https?://)?(?:www\.)?(\w+\.\w+)'

        # Find all matches using the pattern
        match_sites = re.findall(pattern2, result)
        if match_sites:
            print(match_sites)
        else:
            match_sites = "None"

        return matches[0] + " " + match_sites[0]
    except:
        return "Not Found"


# Streamlit application
def main():
    st.title("Price Comparison")

    # Upload CSV file
    csv_file = st.file_uploader("Upload CSV file", type=['csv'])

    if csv_file is not None:
        df = pd.read_csv(csv_file)

        # Display the uploaded CSV data
        st.subheader("Uploaded CSV Data:")
        st.dataframe(df)

        # Create new column to store the matching lines
        with st.spinner("Fetching lowest prices..."):
            df['Matching Lines'] = df['Name'].apply(get_lowest_price)
            # Remove the spinner and display the comparison table
            st.success("Lowest prices fetched!")
            st.subheader("Price Comparison:")
            st.dataframe(df)
    else:
        st.warning("Please upload a CSV file.")


if __name__ == '__main__':
    main()
