import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st

def run_about_app():

	st.subheader("About HeartBeats")
	Text_Intro ='<p style="font-family:Bellota;color:black;font-size:20px;"> HeartBeats_App....the health beats of your heart🧡. This app is inspired by the power of Machine Learning. I have been thinking it will be meaningful if  Machine Learning can be used to add value to the society. This inspires me to create simple light hearted interactive apps to invite people for prognosis of diseases at the same time provide light awareness information on the disease to them." </p>'
	st.markdown(Text_Intro,unsafe_allow_html=True)

	Text_Intro2 ='<p style="font-family:Bellota;color:black;font-size:20px;">Hope you find this little app entertaining and meaningful. You are welcome to provide feedback for future improvement. Stay happy, stay healthy" </p>'
	st.markdown(Text_Intro2,unsafe_allow_html=True)

	st.markdown('<a href="mailto:alice.python21@gmail.com">[Click to Sent feedback] </a>', unsafe_allow_html=True)
	st.markdown("")
	st.text("")
	st.text("")
	st.text("")
	img = Image.open("Image/signature.jpg")
	st.image(img,use_column_width=True)

 


	