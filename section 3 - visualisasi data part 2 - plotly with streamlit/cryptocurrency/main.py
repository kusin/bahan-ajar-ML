# lib getdataset from yahoo
import yfinance as yf

# import library streamlit
import streamlit as st

# lib visualization data
import plotly.express as px
import plotly.graph_objects as go

# import custom func
from class_data import *
from class_visualization import *

# config web streamlit
st.set_page_config(
  page_title="My Dasboard - Cryptocurrency", 
  layout="wide", 
  initial_sidebar_state="auto",
)

# container-header
with st.container():
  st.markdown("# Visualization Data of Cryptocurrency and Stock Price")

# split two columns
col1, col2 = st.columns([0.3, 0.7], gap="small")

# col1 - config dataset
with col1:

  # set labels
  st.success("Config Dataset")
  
  with st.form("my-form"):
    cryptocurrency = st.selectbox(
      "Choose a cryptocurrency", ("BTC-USD", "ETH-USD", "AMZN", "AAPL", "GOOG", "MSFT"), 
      placeholder="Choose a cryptocurrency", index=None
    )
    start = st.date_input(
      label="Start Date",
      value=None, min_value=None, max_value=None,
    )
    end = st.date_input(
      label="End Date",
      value=None, min_value=None, max_value=None,
    )
    submit = st.form_submit_button(label="Submit", type="secondary", use_container_width=True)

with col1:
  st.info("Created by Aryajaya Alamsyah")

# col1 - Exploration Data Analysis
with col2:

  # set labels
  st.success("Exploration Data Analysis")
  
  # Set Default dataset
  if submit:
    # BTC-USD, ETH-USD, AMZN, AAPL, GOOG, MSFT
    ticker      = yf.Ticker(cryptocurrency)
    startDate   = start
    endDate     = end
  else:
    # BTC-USD, ETH-USD, AMZN, AAPL, GOOG, MSFT
    ticker      = yf.Ticker("BTC-USD")
    startDate   = "2015-01-01"
    endDate     = "2024-06-01"

  # load dataset
  dataset = getData(ticker, startDate, endDate)

  # load timeseries plot
  st.plotly_chart(timeseries_plot(dataset, cryptocurrency))
