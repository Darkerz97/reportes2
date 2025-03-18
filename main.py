import streamlit as st
import pandas as pd
import numpy as np
import time 

# MY FIRST APP fundamentals 


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]

}))

# different methods to show dataframes

dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))


#line charts 

chart_data= pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

chart_data
st.line_chart(chart_data)


#plot maps 

map_data = pd.DataFrame(
    np.random.rand(1000,2) / [50, 50]  +  [21.1250, -101.6860],
    columns= ['lat', 'lon'])

st.map(map_data)

#widgets

x= st.slider('x')
st.write(x,'squared is',x * x)

st.text_input("your name", key="name")
st.session_state.name

#check boxes to hide info 

if st.checkbox("show dataframe"):
    chart_data= pd.DataFrame(
        np.random.rand(20,3),
        columns= (['a','b','c'])
    )
    chart_data

#use selectbox for options

df= pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

option = st.selectbox(
    'wich number do you select',
    df['first column']
)

'you selected',option

#layout

# Add a select box to the sidebar:
add_selectbox= st.sidebar.selectbox(
    'how would you like to be contacted?',
    ('Email','Home phone','mobile phone')
)
#add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
#you can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    

'starting a long computation'

#add a placeholder 
latest_iteration = st.empty()
bar = st.progress(0)

for i in range (100):
    #update the progress with each iteration
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'... finish'
