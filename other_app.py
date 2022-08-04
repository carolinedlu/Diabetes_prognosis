import streamlit as st
from PIL import Image
#import streamlit.components as stc
#import streamlit.components.v1 as components

def run_other_app():
    st.text("")
    st.subheader("Mental Health:")
    Text_Mental = ('<p style="font-family:Arial;color:black;font-size:20px;">Positive mental health allows people to realize their full potential and cope with the stresses of life better. It is said that depression increases the risk of physical health problems, particularly long-lasting conditions like diabetes, heart disease, and stroke. Life might not be rosy but stay possitive makes life easier and the ride worthwhile.</p>')
    st.markdown(Text_Mental,unsafe_allow_html=True)
    c1,c2=st.columns([1.5,1])
    with c1:
        Text_Mood = ('<p style="font-family:Arial;color:black;font-size:25px;">How are you feeling today?</p>')
        st.markdown(Text_Mood,unsafe_allow_html=True)
        img = Image.open("mood/ImageMood.jpg")
        st.image(img,use_column_width=True)
    with c2:
        Text_Mood = ('<p style="font-family:Arial;color:black;font-size:25px;">Please select.</p>')
        st.markdown(Text_Mood,unsafe_allow_html=True)
        st.text("<*><*><*><*><*><*><*><*><*>")
        if st.button("Just-Another-Day",key="M1"):
            st.info(f"##### Dear Wonderful Creation, your mood is just -a another day-. Cheer!!")
            img = Image.open("mood/ImageQuoteNormal.jpg")
            st.image(img,use_column_width=True)
        elif st.button("Angry-Sad-Lousy",key="M2"):
            st.info(f"##### Dear Precious Creation, your mood is not so good. Smile!!")
            img = Image.open("mood/ImageQuoteSad.jpg")
            st.image(img,use_column_width=True)
        elif st.button("Happy-Excited-Peaceful",key="M3"):
            st.info(f"##### Dear Marvellous Creation, Your mood is good. Stay Cool!!")
            img = Image.open("mood/ImageQuoteHappy.jpg")
            st.image(img,use_column_width=True)
        else:
            st.text("")
        st.text("<*><*><*><*><*><*><*><*><*>")
    st.text("")
    st.text("")
    st.subheader("Other Apps:")
    st.info("BMI_App >>  [Click to find out your BMI](https://alicekoh-bmi-report-streamlit-app-pyjmee.streamlitapp.com/)")