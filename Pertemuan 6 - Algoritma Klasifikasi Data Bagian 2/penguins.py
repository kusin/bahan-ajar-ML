# library ui-dashboard
import streamlit as st

# library manipulation data
import numpy as np
import pandas as pd

## library data visualization
import seaborn as sns
import matplotlib.pyplot as plt

# lib data preprocessing 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# lib supervised learning
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# library evaluation model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# set random number
import random as rm
rm.seed(1234)

# set random number
import numpy as np
np.random.seed(1234)

# config web streamlit
st.set_page_config(page_title="My Dashboard", layout="wide")

# config load dataset
dataset = sns.load_dataset("penguins").ffill()

with st.sidebar:
    form = st.form("my-form")
    algorithms = form.selectbox(
        label="Choose a algorithms", options=("Decision Tree", "Naive Bayes", "Support Vector Machine"), 
        placeholder="Choose a algorithms", index=None)
    submit = form.form_submit_button(label="Submit", type="secondary", use_container_width=True)

# container-header
with st.container():
    st.markdown("## Classification of penguin species using supervised learning algorithms")
    st.markdown("<br>", unsafe_allow_html=True)

# container-body
with st.container():
    st.dataframe(dataset, use_container_width=True)

# container-results
with st.container():

    # step 1. data preprocessing (set features and labels)
    x = dataset[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]].values
    y = dataset[["sex"]].values

    # step 1. data preprocessing (normalize features)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(x)

    # step 1. data preprocessing (split validation)
    trainX, testX, trainY, testY = train_test_split(
        scaled, y, train_size=0.7, test_size=0.3, random_state=None, shuffle=True)
    
    # step 2. modeling of supervised learning
    if algorithms == "Decision Tree":
        result = DecisionTreeClassifier(criterion="gini", random_state=None).fit(trainX, trainY).predict(testX)
    elif algorithms == "Naive Bayes":
        result = GaussianNB().fit(trainX, trainY).predict(testX)
    elif algorithms == "Support Vector Machine":
        result = SVC(kernel='rbf').fit(trainX, trainY).predict(testX)
    else:
        st.error("Please choose one algorithm from the sidebar.")
        st.stop()

    # step 3. show the results 
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Accuracy", f"{accuracy_score(testY, result):.4f}")
    col2.metric("Precision", f"{precision_score(testY, result, average='macro'):.4f}")
    col3.metric("Recall", f"{recall_score(testY, result, average='macro'):.4f}")
    col4.metric("F1 Score", f"{f1_score(testY, result, average='macro'):.4f}")
