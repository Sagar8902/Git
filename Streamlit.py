
import streamlit as st
import time as t

#image
st.image("D:/# SAGAR/# Resources/Urjaa Exim's logo .jfif")

#Title - It is used to add the title of the app
st.title("Hello World")

#Header  - It is used to add header
st.header("Machine Learning")

#subheader
st.subheader("Linear Regression")

#Info
st.info("Let's learn about machine learning from scrath")

#warning
st.warning("be consistant")

#error message
st.error("wrong password")

#success message
st.success("You successfully register the course")

#write
st.write("Project Name")


# Markdown
st.markdown("# Machine Leanring")
st.markdown("## Machine Leanring")
st.markdown("### Machine Leanring")
st.markdown(":moon:")
st.markdown(":smile:")

#text
st.text("Welcome Learners")

#caption
st.caption("let's write code")


# to display mathematical equation
st.latex(r'''a+b x^2+c''')


## Widget

#checkbox
st.checkbox("login")

#button
#st.button("sign up")

#radio widget
st.radio("pick your gender",["Male","Female","Other"])

#select box
st.selectbox("Pick your course",["ML","AI","Data Science","DAta Analysis"])

#multiselect
st.multiselect("Choose the dept",["Developer","Data","Designer"])

#select Slider
st.select_slider("Rating",["Bad","Good","Excellent","Outstanding"])


#slider
st.slider("Enter your number",0,10)

#number input
st.number_input("Pick a number",0,10)

#text input
st.text_input("Enter your email address")

#date input
st.date_input("Course start date")

#time input
st.time_input("What the timing")

#text area
st.text_area("Welcome to the course")

#file uploader
st.file_uploader("upload your file here")

#color picker
st.color_picker("select color")


#progess
st.progress(80)

#spinner - waiting messege
with st.spinner("Just Wait"):
    t.sleep(2)

#ballon - celebration
st.balloons()

#sidebar
st.sidebar.title("Welcome to the course")
st.sidebar.text_input("Enter your email")
st.sidebar.text_input("Enter your password")
st.sidebar.button("sign up")
st.sidebar.radio("Select your profession",["Working","Student","Other"])


## Data Visualization

import pandas as pd
import numpy as np

st.title("Bar Chart")
data = pd.DataFrame(np.random.randn(35,2),columns=["x","y"])
st.bar_chart(data)

st.title("Line Chart")
data = pd.DataFrame(np.random.randn(35,2),columns=["x","y"])
st.line_chart(data)

st.title("Area Chart")
data = pd.DataFrame(np.random.randn(35,2),columns=["x","y"])
st.area_chart(data)

