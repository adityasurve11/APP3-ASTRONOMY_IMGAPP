import requests
import streamlit as st

# Preapre API key and API url
api_key = "RGk3bpm2ccxzcJM2J2O5GT5SgJG8LCeZvcfdXyxp"
url = "https://api.nasa.gov/planetary/apod?" \
       f"api_key={api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)

