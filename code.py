import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Titanic EDA Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ Custom Styling ------------------
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #fafafa;
    }
    .css-18e3th9 {
        background-color: #0e1117;
    }
    .css-1d391kg {
        background-color: #1c1f26;
    }
    h1, h2, h3, h4 {
        color: #f5f5f5;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Load Dataset ------------------
data = sns.load_dataset("titanic")

# ------------------ Data Cleaning ------------------
data.drop_duplicates(inplace=True)
data["age"] = data["age"].fillna(data["age"].median())
data["embarked"] = data["embarked"].fillna(data["embarked"].mode()[0])
data["embark_town"] = data["embark_town"].fillna(data["embark_town"].mode()[0])
if "deck" in data.columns:
    data.drop("deck", axis=1, inplace=True)

# ------------------ Title ------------------
st.title("馃殺 Titanic Dataset EDA Dashboard")
st.markdown("Explore survival patterns, relationships, and trends interactively in a modern dashboard.")

# ------------------ Sidebar ------------------
st.sidebar.header("馃攳 Choose Analysis")
options = st.sidebar.radio(
    "Select a visualization:",
    [
        "Survival Count",
        "Survival by Gender",
        "Survival by Passenger Class",
        "Age Distribution",
        "Age vs Survival",
        "Fare Distribution",
        "Survival by Embark Town",
        "Correlation Heatmap",
    ]
)

# ------------------ Plot Rendering ------------------
if options == "Survival Count":
    fig = px.histogram(data, x="survived", color="survived",
                       title="Survival Count", labels={"survived": "Survived (0=No, 1=Yes)"})
    st.plotly_chart(fig, use_container_width=True)

elif options == "Survival by Gender":
    fig = px.histogram(data, x="sex", color="survived", barmode="group",
                       title="Survival by Gender")
    st.plotly_chart(fig, use_container_width=True)

elif options == "Survival by Passenger Class":
    fig = px.histogram(data, x="pclass", color="survived", barmode="group",
                       title="Survival by Passenger Class")
    st.plotly_chart(fig, use_container_width=True)

elif options == "Age Distribution":
    fig = px.histogram(data, x="age", nbins=30, title="Age Distribution",
                       marginal="box", color="sex")
    st.plotly_chart(fig, use_container_width=True)

elif options == "Age vs Survival":
    fig = px.box(data, x="survived", y="age", color="survived",
                 title="Age vs Survival")
    st.plotly_chart(fig, use_container_width=True)

elif options == "Fare Distribution":
    fig = px.histogram(data, x="fare", nbins=30, title="Fare Distribution",
                       marginal="box", color="pclass")
    st.plotly_chart(fig, use_container_width=True)

elif options == "Survival by Embark Town":
    fig = px.histogram(data, x="embark_town", color="survived", barmode="group",
                       title="Survival by Embark Town")
    st.plotly_chart(fig, use_container_width=True)

elif options == "Correlation Heatmap":
    corr = data.corr(numeric_only=True)
    fig = px.imshow(corr, text_auto=True, title="Correlation Heatmap",
                    color_continuous_scale="RdBu_r")
    st.plotly_chart(fig, use_container_width=True)

# ------------------ Insights ------------------
st.subheader("馃搶 Key Insights")
st.markdown("""
- **Women** had a much higher survival rate than men.  
- **Higher-class passengers (Pclass 1)** had better survival chances.  
- **Younger children** tended to survive more.  
- **Higher fares** correlated with survival (wealthier passengers).  
""")
