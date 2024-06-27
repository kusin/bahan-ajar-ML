import pandas as pd
import numpy as np
import plotly.express as px
# ---------------------------------------------------------------------------

# func build barplot
def barplot(df, title):

  # calculate sum of species
  data = pd.DataFrame(df.value_counts()).reset_index()

  # create barplot
  fig = px.bar(data, x="species", y="count", color="species")

  # custom layout
  fig.update_layout(
    title=title,
    xaxis_title="",
    yaxis_title="",
    legend=dict(title='', orientation='h', yanchor='top', y=1.05, xanchor='center', x=0.5)
  )

  # return values
  return fig
# ---------------------------------------------------------------------------

# func build heatmap coor
def heatmap(df, title):

  # calculate correlation use pearson
  z = df.corr(method="pearson", numeric_only=True)

  # create imshow
  fig = px.imshow(
    z, zmin=-1, zmax=1, text_auto=True, aspect="auto",
  )
  
  # custom layout
  fig.update_layout(
    title=title,
    xaxis_title="",
    yaxis_title="",
  )

  # return values
  return fig
# ---------------------------------------------------------------------------

# func build scatter plot
def scatter(df, x, y, title):

  # create scatter
  fig = px.scatter(df, x=x, y=y, color="species")

  # custom scatter
  fig.update_traces(
    marker_size=7
  )

  # custom layout
  fig.update_layout(
    title=title,
    xaxis_title="",
    yaxis_title="",
    legend=dict(title='', orientation='h', yanchor='top', y=1.05, xanchor='center', x=0.5)
  )

  # return values
  return fig
# ---------------------------------------------------------------------------

# func build boxplot
def boxplot(df, x, y, title):

  # create boxplot
  fig = px.box(df, x=x, y=y, color="species")

  # custom layout
  fig.update_layout(
    title=title,
    xaxis_title="",
    yaxis_title="",
    legend=dict(title='', orientation='h', yanchor='top', y=1.05, xanchor='center', x=0.5)
  )

  # return values
  return fig
# ---------------------------------------------------------------------------

# func build histogram
def histogram(df, x, title):

  # create histogram
  fig = px.histogram(df, x=x, color="species")

  # custom layout
  fig.update_layout(
    title=title,
    xaxis_title="",
    yaxis_title="",
    legend=dict(title='', orientation='h', yanchor='top', y=1.05, xanchor='center', x=0.5)
  )

  # return values
  return fig
