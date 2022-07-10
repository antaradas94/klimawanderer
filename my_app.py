from msilib import sequence
from turtle import width
import streamlit as st
import pandas as pd 
from PIL import Image
import PIL
import altair as alt
from utils import load_data, lin_reg
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

#006D77, #83C5BE, #EDF6F9, #FFDDD2, #E29578

def get_image(img_path):
    image = Image.open(img_path)
    return image

st.set_page_config(
    page_title="Healthy City",
    layout="wide",
    initial_sidebar_state="auto",
)

df = pd.read_csv( 'unconv.zip')
X_train, X_test, y_train, y_test = load_data('unconv.zip', 'Prod')
y_pred = lin_reg(X_train, y_train, X_test)

#---------------------------------#
# Title

st.sidebar.image(get_image('images.png'),width=300)
st.sidebar.markdown("<h1 style='text-align: center; color: #006D77;'>Healthy City</h1>", unsafe_allow_html=True)
st.sidebar.write("""
-----
""")

#---------------------------------#
# About
expander_bar = st.expander("About")
expander_bar.markdown("""
**Stay healthy in healthy city**
\n
**Einfach gesund bleiben**
\n
Recieve relevant for you information 
* *At the right time*
* *At the right spot*
""")

#---------------------------------#
# Sidebar

st.sidebar.header('User Input')

selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))
age = st.sidebar.slider('Year', min_value = 1920, max_value=2022, step = 1)
cond_list = st.sidebar.multiselect('Select relevant' , ['allergic', 'cardiovascular', 'no direct UV'])

#---------------------------------#
# Set the page layout of the webapp

col1, col2 =  st.columns((1,1)) # column ratio is 1:1

#---------------------------------#
# 1st column
col1.markdown("<h3 style='text-align: center; color: #E29578;'>The best to do</h3>", unsafe_allow_html=True)
col1.line_chart(y_pred)
for i in cond_list: 
    col1.markdown(i)
#---------------------------------#
# 2nd column

col2.markdown("<h3 style='text-align: center; color: #E29578;'>No go</h3>", unsafe_allow_html=True)
col2.line_chart(df.Prod)



#---------------------------------#
# Containers

c = st.container()
c_col1 , c_col2= c.columns(2)
c_col1.write('Cool')
c_col2.markdown(f">I am  __{2022-age}__ ")  

#---------------------------------#
# Colors

def col_pale(color_pale): 
    fig, ax = plt.subplots(figsize=(6, 1)) 
    x = list(range(len(color_pale)))
    h = np.ones(len(color_pale)).tolist()
    ax.bar(x,h, color=color_pale)
    plt.xticks([])
    plt.yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.tight_layout()
    return fig

color_pale = ['#006D77', '#83C5BE', '#EDF6F9', '#FFDDD2', '#E29578']
fig = col_pale(color_pale)
c_col2.pyplot(fig)



with st.container():
    st.write("This is inside the container")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")



sequence_input = "Dancing Queen"
sequence = sequence_input.splitlines()
sequence = ''.join(sequence) # Concatenates list to string

info = st.text_area('Enter your name', sequence_input, height=1)

st.write("""
*****
""")

def count_letters(seq):
    d = dict( [('a', seq.count('a')),
               ('e',  seq.count('e')),
               ('i',  seq.count('i'))
               ])
    return d

X = count_letters(sequence)
st.write(X)
X_label = list(X)
X_values = list(X.values())

st.subheader('Example of visualization')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'} , axis= 'columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)


p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)
