# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# import library streamlit
import streamlit as st

# library data visualization
import requests
import plotly.express as px
import plotly.graph_objects as go

# config web streamlit
st.set_page_config(
  page_title="My Dasboard - Covid 19",
  page_icon="",
  layout="wide",
  initial_sidebar_state="auto",
  menu_items={
    "Get Help": "https://www.github.com/kusin",
    "Report a bug": "https://www.github.com/kusin",
    "About": "### Copyright 2022 all rights reserved by Aryajaya Alamsyah"
  }
)

# --------------------------------------------------------------------------------------- #
# data acquisition country -------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #
# func load dataset ---------------------------------------------------------------
@st.cache_data
def load_xlsx(file_name,sheet_name):

  # load dataset covid-19
  df = pd.read_excel("../dataset/"+file_name, sheet_name=sheet_name)

  # convert obj or str to datetime
  df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

  # setting date
  df["date"] = df['date'].dt.date

  # setting columns
  df = df[[
        "date", "cumulative_positive", "cumulative_recovery", "cumulative_dead",
        "daily_positive", "daily_recovery", "daily_dead"
      ]]

  # sorting dataset by date desc
  df = df.sort_values(by="date", ascending=False)

  # return values
  return df
# ./ func load dataset ------------------------------------------------------------

# container-header-fuild
with st.container():
  st.markdown("## Data Visualization of Covid-19 in Indonesia")
# ---------------------------------------------------------------------------------

# container-dataset
dataset = load_xlsx("dataset_covid.xlsx", "data-covid-indonesia")
with st.container():

  # split two columns
  col1, col2 = st.columns([0.65,0.35], gap="small")
  
  # show dataset
  with col1:
    st.dataframe(data=dataset, use_container_width=True, hide_index=True)
  
  # summary statistics
  with col2:
    # calculate recovery and date
    recovery = (
      dataset["daily_recovery"].sum() / dataset["daily_positive"].sum()
    )*100
    dead = (
      dataset["daily_dead"].sum() / dataset["daily_positive"].sum()
    )*100
    # ---------------------------------------------------------------------------------
    # split two columns
    sub_col1, sub_col2 = st.columns(2)
    sub_col1.metric(
      label="Percentage recovery",
      value="{:.2f}".format(recovery)+"%",
      delta="0,35%",
    )
    sub_col2.metric(
      label="Percentage dead",
      value="{:.2f}".format(dead)+"%",
      delta="0,00%",
    )
    # ---------------------------------------------------------------------------------
    # split three columns
    sub_col1, sub_col2, sub_col3 = st.columns(3)
    sub_col1.metric(
      label="Cumulative Positive",
      value="{:,}".format(dataset["daily_positive"].sum()),
      delta="3,373 People"
    )
    sub_col2.metric(
      label="Cumulative Recovery",
      value="{:,}".format(dataset["daily_recovery"].sum()),
      delta="3.919 People"
    )
    sub_col3.metric(
      label="Cumulative Dead",
      value="{:,}".format(dataset["daily_dead"].sum()),
      delta="106 People"
    )
    # ---------------------------------------------------------------------------------
    # split three columns
    sub_col1, sub_col2, sub_col3 = st.columns(3)
    sub_col1.metric(
      label="Daily Positive",
      value="{:,}".format(dataset["daily_positive"].iloc[0]),
      delta="-732 People"
    )
    sub_col2.metric(
      label="Daily Recovery",
      value="{:,}".format(dataset["daily_recovery"].iloc[0]),
      delta="187 People"
    )
    sub_col3.metric(
      label="Daily Dead",
      value="{:,}".format(dataset["daily_dead"].iloc[0]),
      delta="26 People"
    )
    st.caption("Summary statistics of covid-19, update at 20 October 2020")
    # ---------------------------------------------------------------------------------

# container-lineplot
with st.container():

  # split two columns
  col1, col2 = st.columns([0.5,0.5], gap="medium")

  # col1 - cumulative data of positive, recovery, and dead
  with col1:
    fig = go.Figure()
    fig.add_trace(
      go.Scatter(
        x=dataset["date"],
        y=dataset["cumulative_positive"],
        name="Cumulative Positive",
        line=dict(color="blue",width=2),
      )
    )
    fig.add_trace(
      go.Scatter(
        x=dataset["date"],
        y=dataset["cumulative_recovery"],
        name="Cumulative Recovery",
        line=dict(color="green",width=2),
      )
    )
    fig.add_trace(
      go.Scatter(
        x=dataset["date"],
        y=dataset["cumulative_dead"],
        name="Cumulative Dead",
        line=dict(color="red",width=2),
      )
    )
    fig.update_layout(
      title="TimeSeries of cumulative positive, recovery, and dead",
      xaxis_title="",
      yaxis_title="Number of cases",
      xaxis=dict(tickangle=0),
      yaxis=dict(tickangle=0),
      legend=dict(
        title='', orientation='h', 
        yanchor='top', y=1.05, 
        xanchor='center', x=0.5
      )
    )
    st.plotly_chart(fig, use_container_width=True)
    # ---------------------------------------------------------------------------------

  # col2 - daily data of positive, recovery, and dead
  with col2:
    fig = go.Figure()
    fig.add_trace(
      go.Scatter(
        x=dataset["date"],
        y=dataset["daily_positive"],
        name="Daily Positive",
        line=dict(color="blue",width=2),
      )
    )
    fig.add_trace(
      go.Scatter(
        x=dataset["date"],
        y=dataset["daily_recovery"],
        name="Daily Recovery",
        line=dict(color="green",width=2),
      )
    )
    fig.add_trace(
      go.Scatter(
        x=dataset["date"],
        y=dataset["daily_dead"],
        name="Daily Dead",
        line=dict(color="red",width=2),
      )
    )
    fig.update_layout(
      title="TimeSeries of daily positive, recovery, and dead",
      xaxis_title="",
      yaxis_title="Number of cases",
      xaxis=dict(tickangle=0),
      yaxis=dict(tickangle=0),
      legend=dict(title='', orientation='h', yanchor='top', y=1.05, xanchor='center', x=0.5)
    )
    st.plotly_chart(fig, use_container_width=True)
    # ---------------------------------------------------------------------------------

# container-scatterplot
with st.container():

  # split two columns
  col1, col2 = st.columns([0.5,0.5], gap="medium")

  # col1 - daily data of positive vs recovery
  with col1:
    fig = go.Figure()
    fig.add_trace(
      go.Scatter(
        x=dataset["daily_positive"],
        y=dataset["daily_recovery"],
        text=dataset["date"],
        mode="markers",
      )
    )
    fig.update_traces(
      marker={
        "size" : 12,
        "color": "green",
        "opacity": 0.75,
        "line": {"width": 0.5, "color": "black"},
        "symbol": "circle"
      }
    )
    fig.update_layout(
      title="Scatter plot of positive and recovery",
      xaxis_title="Daily positive",
      yaxis_title="Daily recovery",
      xaxis=dict(tickangle=0),
      yaxis=dict(tickangle=0),
    )
    st.plotly_chart(fig, use_container_width=True)
    # ---------------------------------------------------------------------------------

  # col1 - daily data of positive vs dead
  with col2:
    fig = go.Figure()
    fig.add_trace(
      go.Scatter(
        x=dataset["daily_positive"],
        y=dataset["daily_dead"],
        text=dataset["date"],
        mode="markers",
      )
    )
    fig.update_traces(
      marker={
        "size" : 12,
        "color": "red",
        "opacity": 0.75,
        "line": {"width": 0.5, "color": "black"},
        "symbol": "circle"
      }
    )
    fig.update_layout(
      title="Scatter plot of positive and dead",
      xaxis_title="Daily positive",
      yaxis_title="Daily dead",
      xaxis=dict(tickangle=0),
      yaxis=dict(tickangle=0),
    )
    st.plotly_chart(fig, use_container_width=True)
    # ---------------------------------------------------------------------------------
  
# --------------------------------------------------------------------------------------- #
# data acquisition province ------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #
dataset = pd.read_excel("../dataset/dataset_covid.xlsx", sheet_name="data-covid-provinsi", engine="openpyxl")
st.info("Summary statistic on each province")

# container-positive
with st.container():

  # sorting sum-positive with most cases
  df_positive = dataset.sort_values("sum_positive", ascending=False)
  df_positive = df_positive[["province", "sum_positive"]].head(5)

  # split two columns
  col1, col2 = st.columns([0.5,0.5], gap="medium")

  # col1 - Pieplot (Top 5 province of sum positive)
  with col1:
    fig = px.pie(
      df_positive, names="province", values="sum_positive", hole=0.5,
    )
    fig.update_traces(
      textinfo="percent+value",
      textfont_size=14,
      marker_colors = px.colors.qualitative.Pastel,
      marker_line_color="#FFFFFF",
      marker_line_width=1.25,
    )
    fig.update_layout(
      title = "Top 5 province of sum positive",
      legend=dict(orientation='h', x=0.05, y=0.0),
    )
    st.plotly_chart(fig, use_container_width=True)
   
  # col2 - Barplot (Top 5 province of sum positive)
  with col2:
    fig = px.bar(
      df_positive, x="province", y="sum_positive", text_auto=True,
    )
    fig.update_traces(
      textfont_size=14,
      textangle=0,
      textposition="inside",
      marker_color="#0071c5",
      marker_line_color="#292929",
      marker_line_width=1,
    )
    fig.update_layout(
      title = "Top 5 province of sum positive",
      xaxis_title = "province",
      yaxis_title = "sum positive",
    )
    st.plotly_chart(fig, use_container_width=True)
    # ---------------------------------------------------------------------------------

# container-recovery
with st.container():

  # sorting sum-recovery with most cases
  df_recovery = dataset.sort_values("sum_recovery", ascending=False)
  df_recovery = df_recovery[["province", "sum_recovery"]].head(5)

  # split two columns
  col1, col2 = st.columns([0.5,0.5], gap="medium")

  # col1 - Pieplot (Top 5 province of sum recovery)
  with col1:
    fig = px.pie(
      df_recovery, names="province", values="sum_recovery", hole=0.5,
    )
    fig.update_traces(
      textinfo="percent+value",
      textfont_size=14,
      marker_colors = px.colors.qualitative.Pastel,
      marker_line_color="#FFFFFF",
      marker_line_width=1.25,
    )
    fig.update_layout(
      title = "Top 5 province of sum recovery",
      legend=dict(orientation='h', x=0.05, y=0.0),
    )
    st.plotly_chart(fig, use_container_width=True)
   
  # col2 - Barplot (Top 5 province of sum recovery)
  with col2:
    fig = px.bar(
      df_recovery, x="province", y="sum_recovery", text_auto=True,
    )
    fig.update_traces(
      textfont_size=14,
      textfont_color="black",
      textangle=0,
      textposition="inside",
      marker_color="#63c689",
      #marker_color="green",
      marker_line_color="#292929",
      marker_line_width=0.5,
    )
    fig.update_layout(
      title = "Top 5 province of sum recovery",
      xaxis_title = "province",
      yaxis_title = "sum recovery",
    )
    st.plotly_chart(fig, use_container_width=True)
    # ---------------------------------------------------------------------------------

# container-dead
with st.container():

  # sorting sum-dead with most cases
  df_dead = dataset.sort_values("sum_dead", ascending=False)
  df_dead = df_dead[["province", "sum_dead"]].head(5)

  # split two columns
  col1, col2 = st.columns([0.5,0.5], gap="medium")

  # col1 - Pieplot (Top 5 province of sum dead)
  with col1:
    fig = px.pie(
      df_dead, names="province", values="sum_dead", hole=0.5,
    )
    fig.update_traces(
      textinfo="percent+value",
      textfont_size=14,
      marker_colors = px.colors.qualitative.Pastel,
      marker_line_color="#FFFFFF",
      marker_line_width=1.25,
    )
    fig.update_layout(
      title = "Top 5 province of sum dead",
      legend=dict(orientation='h', x=0.05, y=0.0),
    )
    st.plotly_chart(fig, use_container_width=True)
   
  # col2 - Barplot (Top 5 province of sum dead)
  with col2:
    fig = px.bar(
      df_dead, x="province", y="sum_dead", text_auto=True,
    )
    fig.update_traces(
      textfont_size=14,
      textfont_color="black",
      textangle=0,
      textposition="inside",
      marker_color="#dc143c",
      marker_line_color="#292929",
      marker_line_width=0.5,
    )
    fig.update_layout(
      title = "Top 5 province of sum dead",
      xaxis_title = "province",
      yaxis_title = "sum dead",
    )
    st.plotly_chart(fig, use_container_width=True)
    # ---------------------------------------------------------------------------------

# container footer
with st.container():
  st.info("Copyright all rights reserved 2024 by Aryajaya Alamsyah, S.Kom., M.Kom., MTA.")