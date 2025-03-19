import streamlit as st

#Streamlit UI
st.title('Power Calculator')
st.write('Enter a number to calculate its square,cube or fifth power')

#Recieve input
n = st.number_input("Enter an Integer",value=1,step=1)

#Process
square = n**2
cube = n**3
fifth_power = n**5

#output
st.write(f"The square of {n} is : {square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"The fifth_power of {n} is : {fifth_power}")