# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# import library streamlit
import streamlit as st
import streamlit_extras.add_vertical_space as avs

# library data visualization
import plotly.express as px
import plotly.graph_objects as go

# config web streamlit
st.set_page_config(
  page_title="My Dasboard - Classification Iris Flowers",
  page_icon="",
  layout="wide",
  initial_sidebar_state="auto",
  menu_items={
    "Get Help": "https://www.github.com/kusin",
    "Report a bug": "https://www.github.com/kusin",
    "About": "### Copyright 2024 all rights reserved by Aryajaya Alamsyah"
  }
)

# func iris dataset
@st.cache_data
def load_dataset(df):
  dataset = pd.read_csv("../dataset/"+df)
  return dataset
#-------------------------------------------------------------------------------------------

def heatmap(df):
  # plotting heatmap corr
  fig = px.imshow(
    img=df,
    x=['Sepal length', 'Sepal width', 'Petal length', 'Petal width'],
    y=['Sepal length', 'Sepal width', 'Petal length', 'Petal width'],
    color_continuous_scale = 'viridis',
    zmin=-1, zmax=1,
    aspect=True,
    text_auto=True,
  )

  # customize heatmap corr
  fig.update_traces(
    xgap=5, ygap=5,
  )

  # customize layout
  fig.update_layout(
    title="Heatmaps correlations of iris flowers",
    width=600, height=375,
  )

  # show heatmap corr
  return fig

#-------------------------------------------------------------------------------------------
# container-header-fuild
with st.container():
  st.markdown("## Classification of iris flower using supervised learning algorthm")
  avs.add_vertical_space(2)

# container-dataset
dataset = load_dataset("iris.csv")
with st.container():
  col1, col2 = st.columns([0.4,0.6], gap="small")
  with col1:
    st.info("Dataset of iris flowers")
    st.dataframe(dataset, use_container_width=True)
  with col2:
    st.info("Exploration Data Analysis")
    tab1, tab2, tab3 = st.tabs(["Heatmap", "Barplot", "Scatterplot"])

    df = np.round(dataset.corr(method="pearson", numeric_only=True), 4)
    tab1.plotly_chart(heatmap(df),use_container_width=True)
    

# container-predictions
with st.container():
  st.info("Predictions of iris flowers")


