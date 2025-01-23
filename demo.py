import streamlit as st

st.title("HEllO STREAMLIT")\

st.header("Hello Nitu")

st.subheader("Hello there this is my first web Application page")
st.subheader("I'll try to make multiple project with streamlit package manager")
st.markdown(""" # h1 tag 
## h2 tag 
### h3 tag 
:moon: <br>
:sunglasses:<br>
:smile:
:joy:

""")
d = {
"name": "Nitu Yadav", 
"language": "Python",
"Topic": "Streamlit"
}
st.write(d)

# st.markdown(""" # h1 tag
# ## h2 tag
# ### h3 tag
# :moon:<br>
# :sunglasses:
# ** bold **
# _ italics _
# """,True)

st.text("List of all")
st.button("clear")
st.checkbox("YES")
st.checkbox("No")
st.radio("yes","No")