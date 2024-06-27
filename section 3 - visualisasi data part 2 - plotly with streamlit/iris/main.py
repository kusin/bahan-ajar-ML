# import library streamlit
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# import cumstom func
from class_data import *
from class_visualization import *

# config web streamlit
st.set_page_config(
  page_title="My Dasboard - Iris Dataset", 
  layout="wide", 
  initial_sidebar_state="auto",
)
# ---------------------------------------------------------------------------

# load dataset iris
dataset = getDataset("iris.csv")

# normalized data
dataset = normalized(dataset)

# container-header
with st.container():
  st.markdown("# Data Visualization of Iris Dataset")

# container-visualization data
with st.container():

  # split two columns
  col1, col2 = st.columns([1,1], gap="medium")

  # col-barplot
  col1.plotly_chart(
    barplot(dataset["species"], "Bar Chart to Find the Number of Classes"),
    use_container_width=True
  )

  # col-heatmap
  col2.plotly_chart(
    heatmap(dataset, "Heatmap Corr to calculate correlation between features"),
    use_container_width=True
  )
  # ---------------------------------------------------------------------------

  # col-scatter
  col1.plotly_chart(
    scatter(
      dataset, "petal_length", "sepal_length", "Scatterplot to see linearity between features"
    ),
    use_container_width=True
  )

  # col-scatter
  col2.plotly_chart(
    scatter(
      dataset, "petal_length", "petal_width", "Scatterplot to see linearity between features"
    ),
    use_container_width=True
  )
  # ---------------------------------------------------------------------------

  # col-boxplot
  col1.plotly_chart(
    boxplot(
      dataset, "species", "sepal_length", "Boxplot to see the outlier value in each feature"
    ),
    use_container_width=True
  )
  # col-boxplot
  col2.plotly_chart(
    boxplot(
      dataset, "species", "sepal_width", "Boxplot to see the outlier value in each feature"
    ),
    use_container_width=True
  )
  # col-boxplot
  col1.plotly_chart(
    boxplot(
      dataset, "species", "petal_length", "Boxplot to see the outlier value in each feature"
    ),
    use_container_width=True
  )
  # col-boxplot
  col2.plotly_chart(
    boxplot(
      dataset, "species", "petal_width", "Boxplot to see the outlier value in each feature"
    ),
    use_container_width=True
  )
  # ---------------------------------------------------------------------------

  # col-boxplot
  col1.plotly_chart(
    histogram(
      dataset, "sepal_length", "Histogram to see the distribution of data between features"
    ),
    use_container_width=True
  )
  col2.plotly_chart(
    histogram(
      dataset, "sepal_width", "Histogram to see the distribution of data between features"
    ),
    use_container_width=True
  )
  col1.plotly_chart(
    histogram(
      dataset, "petal_length", "Histogram to see the distribution of data between features"
    ),
    use_container_width=True
  )
  col2.plotly_chart(
    histogram(
      dataset, "petal_width", "Histogram to see the distribution of data between features"
    ),
    use_container_width=True
  )