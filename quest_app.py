import streamlit as st
from PIL import Image
#import streamlit.components.v1 as components
import pandas as pd
#import numpy as np
from prognosis_app import run_prognosis_app

def run_quest_app():
	st.subheader("Are you at risk of Diabetes?")
	img = Image.open("quest/ImageSing.jpg")
	st.image(img,use_column_width=True)

	Text_quest = ('<p style="font-family:Arial;color:black;font-size:18px;"> While Singing is good for your emotion, your feeling will help us prognose your diabetes risk. Please take your time to feel, think and answer the questionnaires. The more you know about your body, the more we can help you to prognose the risk. If you are unsure of the answer, please input as [No].</p>')
	st.markdown(Text_quest,unsafe_allow_html=True)

	Text_quest2 = ('<p style="font-family:Arial;color:black;font-size:18px;"> If you are a diabetes patient currently and just want to play with this prognosis app, please fill in the questionnaires base on your symptoms before medication.</p>')
	st.markdown(Text_quest2,unsafe_allow_html=True)


#--session_state---
	state = st.session_state
	if 'age' not in state:
	    state.age = 1.0
	if 'weight' not in state:
	    state.weight = 1.0
	if 'height' not in state:
	    state.height = 1.0
	if 'smoke' not in state:
	    state.smoke = 99.0
	if 'alcohol' not in state:
	    state.alcohol = 99.0

#--Question(1-4)	
	st.subheader("**Diabetes Questionnaires**")	
	c1,c2,c3=st.columns([2,0.5,2])
	with c1:
		fname = st.text_input("Enter Name:",max_chars=15)
		state.age = st.number_input("1) How old are you?",min_value=0.0,max_value=150.0, step=1.0,value=state.age)
		gender = st.radio("2) Are you a male or female?",["-","Female","Male"],key="Q02")
		if fname !="" and state.age!=0.0 and gender=="-":
			st.warning("We appologize. There is no gender in-between choice due to body structure.")
		else: 
			st.write("")
	with c2:
		st.text("")
	with c3:
		state.weight = st.number_input("3) What is your weight (KG)?",min_value=0.0,max_value=150.0, value=state.weight, step=1.0)	
		state.height = st.number_input("4) What is your height (M)?",min_value=0.0,max_value=2.5, value=state.height, step=0.1)
		BMI = round(state.weight/state.height**2,1)
		if BMI > 27.5:
			obesity = "Yes"
		else:
			obesity = "No"
	st.markdown("_____________________")

#--QuestionB Section
	status = state.weight
	if status == 1:
		pass
	else:
		if st.checkbox("CONTINUE",key="quest1"):
		
	#---Question (5-6)
			if fname=="":
				st.warning("Dear Stranger, please provide all information.")
			elif state.age=="":
				st.warning(f"Dear {fname}, please provide all information.")
			elif state.weight==1:
				st.warning(f"Dear {fname}, please provide all information.")
			elif state.height==1:
				st.warning(f"Dear {fname}, please provide all information.")
			else:
				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:	
					polyuria = st.radio("5) Do you experience excessive_urine?",["-","No","Yes"],key="Q06")
					if polyuria == "Yes":
						st.markdown("##### You Selected-Yes🤎")
					elif polyuria == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageUrine.jpg")
					st.image(img,use_column_width=True)
				with c3:
					st.text("")
				st.markdown("_______________________")

				c1,c2,c3=st.columns([2.5,2,0.5])	
				with c1:
					polydipsia = st.radio("6) Do you drink excessive water?",["-","No","Yes"],key="Q07")
					if polydipsia == "Yes":
						st.markdown("##### You Selected-Yes🖤")
					elif polydipsia == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageWater.jpg")
					st.image(img,use_column_width=True)
				with c3:
					st.text("")
				st.markdown("_______________________")

		#---Question (7-8)
				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					sudden_weight_loss = st.radio("7) Do you experience sudden_weight_loss?",["-","No","Yes"],key="Q09")
					if sudden_weight_loss == "Yes":
						st.markdown("##### You Selected-Yes💙")
					elif sudden_weight_loss == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageWeight.jpg")
					st.image(img,use_column_width=True)
				with c3:
					st.text("")
				st.markdown("_______________________")

				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					weakness = st.radio("8) Do you feel tired and fatigue?",["-","No","Yes"],key="Q08")
					if weakness == "Yes":
						st.markdown("##### You Selected-Yes💚")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageTired.jpg")
					st.image(img,use_column_width=True)
				with c3:
					st.text("")
				st.markdown("_______________________")

			#--Quest 9-10
				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					polyphagia = st.radio("9) Do you experience excessive_hunger?",["-","No","Yes"],key="Q10")
					if polyphagia == "Yes":
						st.markdown("##### You Selected-Yes💚")
					elif polyphagia == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageHungry.jpg")
					st.image(img,use_column_width=True)	
				with c3:
				    st.text("")
				st.markdown("_______________________")

				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					genital_thrush = st.radio("10) Do you have genital_thrush?",["-","No","Yes"],key="Q11")
					if genital_thrush == "Yes":
						st.markdown("##### You Selected-Yes💙")
					elif genital_thrush == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageGenital.jpg")
					st.image(img,use_column_width=True)
				with c3:
					st.text("")
				st.markdown("_______________________")


	#---NewQuestionSection---
				st.text("<*><*><*><*><*><*><*><*><*><*><*><*><*>")
				st.info(f"##### Hey {fname}, press onn...you have answered 10 questionnaires. 7more to go.")
				img = Image.open("quest/ImageExercise.jpg")
				st.image(img,use_column_width=True)
				st.text("<*><*><*><*><*><*><*><*><*><*><*><*><*>")
				
		#---Question (11-12)---
				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					visual_blurring = st.radio("11) Do you experience visual blurring?",["-","No","Yes"],key="Q12")
					if visual_blurring == "Yes":
						st.markdown("##### You Selected-Yes💚")
					elif visual_blurring == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageEye.jpg")
					st.image(img,use_column_width=True)	
				with c3:
				    st.text("")
				st.markdown("_______________________")
				
				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					itching = st.radio("12) Do you experience itchy skin and painful?",["-","No","Yes"],key="Q13")
					if itching == "Yes":
						st.markdown("##### You Selected-Yes💚")
					elif itching == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageItchy.jpg")
					st.image(img,use_column_width=True)
				with c3:
					st.text("")
				st.markdown("_______________________")

			#---Question (13-14)	
				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					irritability = st.radio("13) Do you feel very moody?",["-","No","Yes"],key="Q14")
					if irritability == "Yes":
						st.markdown("##### You Selected-Yes💙")
					elif irritability == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageMoody.jpg")
					st.image(img,use_column_width=True)	
				with c3:
				    st.text("")
				st.markdown("_______________________")

				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					delayed_healing = st.radio("14) Do you experience delay in healing?",["-","No","Yes"],key="Q15")
					if delayed_healing == "Yes":
						st.markdown("##### You Selected-Yes💚")
					elif delayed_healing == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageHeal.jpg")
					st.image(img,use_column_width=True)
				with c3:
					st.text("")
				st.markdown("_______________________")

				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					partial_paresis = st.radio("15) Do you have partial_paresis?",["-","No","Yes"],key="Q16")
					if partial_paresis == "Yes":
						st.markdown("##### You Selected-Yes💙")
					elif partial_paresis == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageParesis.jpg")
					st.image(img,use_column_width=True)	
				with c3:
				    st.text("")
				st.markdown("_______________________")

			#---Question (16-17)
				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					muscle_stiffness = st.radio("16) Do you experience muscle_stiffness?",["-","No","Yes"],key="Q17")
					if muscle_stiffness == "Yes":
						st.markdown("##### You Selected-Yes💚")
					elif muscle_stiffness == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageLeg.jpg")
					st.image(img,use_column_width=True)
				with c3:
					st.text("")			

				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					alopecia = st.radio("17) Do you experience hair loss?",["-","No","Yes"],key="Q18")
					if alopecia == "Yes":
						st.markdown("##### You Selected-Yes💚")
					elif alopecia == "No":
						st.markdown("##### You Selected-No💛")
					else:
						st.warning(f"Dear {fname}, please select☝️")
				with c2:
					img = Image.open("quest/ImageHair.jpg")
					st.image(img,use_column_width=True)	
				with c3:
				    st.text("")
				st.markdown("_______________________")
				
			#--Quest 18-19
				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					state.smoke = st.number_input("18) Average, how many cigarette do you smoke a day?",min_value=0.0,max_value=99.0, step=1.0,value=state.smoke)
					if state.smoke ==99.0:
						st.warning(f"Dear {fname}, if you dont smoke, please input 0☝️")
					elif state.smoke==0.0:
						st.markdown(f"##### Cool. You dont smoke❤️")
					else:
						st.markdown(f"##### You smoke an average {state.smoke}nos per day💙")
				with c2:
					img = Image.open("quest/ImageSmoke.jpg")
					st.image(img,use_column_width=True) 
				with c3:
					st.text("")
				st.markdown("_______________________")

				c1,c2,c3=st.columns([2.5,2,0.5])
				with c1:
					state.alcohol = st.number_input("20) Average, how many glass of alcohol you drink a week?",min_value=0.0,max_value=99.0, step=1.0,value=state.alcohol)
					if state.alcohol ==99.0:
						st.warning(f"Dear {fname}, if you dont drink, please input 0☝️")
					elif state.alcohol>0.0 and state.alcohol<5.0:
						st.markdown(f"##### Cool. You drink max 4glass per week.❤️")
					elif state.alcohol ==0.0:
						st.markdown(f"##### You dont drink alcohol💚")
					else:
						st.markdown(f"##### You drink more than 4glass per week💙")
				with c2:
					img = Image.open("quest/ImageAlcohol.jpg")
					st.image(img,use_column_width=True) 
				with c3:
					st.text("")
				st.markdown("_______________________")
				st.text("")

				Text_End = ('<p style="font-family:Arial;color:black;font-size:18px;">~~~ Thank You for taking your time to field up the questionnaires. All information provided will not be distributed but merely use to improve the accuracy of the Machine Learning Model. ~~~.</p>')

		#--User Selection---
				st.subheader("**View Your Answers**")	
				with st.expander("CONTINUE"):
					result = {
						'name':fname,
						'age':state.age,
						'gender':gender,
						'BMI':BMI,
						'polyuria':polyuria,
						'polydipsia':polydipsia,
						'sudden_weight_loss':sudden_weight_loss,
						'weakness':weakness,
						'polyphagia':polyphagia,
						'genital_thrush':genital_thrush,
						'visual_blurring':visual_blurring,
						'itching':itching,
						'irritability':irritability,
						'delayed_healing':delayed_healing,
						'partial_paresis':partial_paresis,
						'muscle_stiffness':muscle_stiffness,
						'alopecia':alopecia,
						'obesity':obesity,
						'smoke':state.smoke,
						'alcohol':state.alcohol
						}
				#--show patient his answer in dataframe format
					answer = pd.DataFrame(result,index=[0])
					st.write(answer)

				#--encode the answer
					for key, val in result.items():
						if type(val) == int or type(val) == float:
							result[key] = val
						if val == "Male" or val == "No":
							result[key] = 0
						elif val == "Female" or val == "Yes":
							result[key] = 1
						elif val == "-" or val == 999.0 or val == 99.0:
							result[key] = 999
							st.warning(f"Dear {fname}, you might have missed out some of the questionnaires. Please visit back and answer all questions in order for the machine to do prognosis.")
							pass
						else:
							result[key] = val
							
				#--Show the answer and save a copy to folder-----
					#Need to convert to dataframe to save as csv
					answer = pd.DataFrame(result,index=[0])
					answer.to_csv('data/answer.csv',index=False)

			#--Run Prognosis Result-----
				st.subheader("**Prognosis Result**")
				with st.expander("CONTINUE"):
					run_prognosis_app()
