import streamlit as st
import streamlit.components as stc
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import os
from home_app import run_home_app
from quest_app import run_quest_app
from prognosis_app import run_prognosis_app
from ml_app import run_ml_app
from other_app import run_other_app
from about_app import run_about_app

st.set_page_config(page_title="HeartBeats_App",page_icon="❤️",layout="centered")
img = Image.open("ImageLogo.jpg")
st.image(img,use_column_width=True)

def main():

#--SideBar------
	menu_list = ["Home","MachineLearning","Others","About HeartBeats",]
	with st.sidebar:
	    option = option_menu("MENU", 
	    	[menu_list[0], menu_list[1],menu_list[2],menu_list[3]],
	        icons=['house', 'kanban','sliders', 'person-bounding-box', ],
	        menu_icon="app-indicator", default_index=0,styles={
	        "container": {"padding": "5!important", "background-color": "#f0f2f6"},
	        "icon": {"color": "#b77b82", "font-size": "28px"}, 
	        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#F6E1D3"},
	        "nav-link-selected": {"background-color": "#b2beb5"},})

#--HOME-&-Mood------
	if option == menu_list[0]:
		run_home_app()
		if st.checkbox("CONTINUE",key="app1"):
			run_quest_app()

#--Question---------
	elif option== menu_list[1]:
		run_ml_app()
	elif option== menu_list[2]:
		run_other_app()
	elif option== menu_list[3]:		
		run_about_app()
	else:
		run_home_app()
		if st.checkbox("CONTINUE",key="app1"):
			run_quest_app()
			

if __name__ == '__main__':
	main()
