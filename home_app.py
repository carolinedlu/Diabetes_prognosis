import streamlit as st
from PIL import Image
#import streamlit.components as stc
#import streamlit.components.v1 as components
import pandas as pd

def run_home_app():
    Text_Intro ='<p style="font-family:Bellota;color:black;font-size:18px;"> .......the health beats of your heart🧡. A little sugar makes you lovely and sweet. Too much sugar however might make you bitter as it is associate with weight gain even in people who exercise regulary. This increasing your risk of getting diabetes" </p>'
    st.markdown(Text_Intro,unsafe_allow_html=True)

    img = Image.open("ImageIntro.jpg")
    st.image(img,use_column_width=True)
    
    st.subheader("Are you at risk of Diabetes? Let's find out.")
    Text_diab2 = ('<p style="font-family:Arial;color:black;font-size:18px;"> Diabetes is a long-lasting health condition that affects how your body turns food into energy. Diabetes cause insufficient blood sugar in your body’s cells for use as energy. A small cut or a fall might be dangerous. Over time, that can cause serious health problems such as heart disease, vision loss, and kidney disease.</p>')
    st.markdown(Text_diab2,unsafe_allow_html=True)

    Text_Mental = ('<p style="font-family:Arial;color:black;font-size:18px;">Are you at risk of Diabetes? Lets find out...</p>')
    st.markdown(Text_Mental,unsafe_allow_html=True)

        
    
