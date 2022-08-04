import streamlit as st
from PIL import Image
import os
import pandas as pd
from pycaret.classification import *

def run_prognosis_app():

    answer = pd.read_csv('data/answer.csv')
    answer2 = answer.drop(["name","BMI",'muscle_stiffness', 'alopecia', 'obesity','smoke','alcohol'], axis=1)

#--Loan model
    loaded_model = load_model("model/Final_Model")
  
#--Prognosis
    prediction = loaded_model.predict(answer2)
    pred_prob = loaded_model.predict_proba(answer2)
    
    chance_list =["low","moderate","high"]
    risk_list =["Negative","positive"]
    action_list = ["maintain active and "]

    prob = round(pred_prob[0][1]*100,1)
    if prediction==0 and prob<35:
        chance = chance_list[0]
        risk =  risk_list[0]
    elif prediction == 1 and prob>64:
        chance = chance_list[2]
        risk =  risk_list[1]
    else:
        chance = chance_list[1]
        if prediction==0:
            risk=risk_list[0]
        else:
            risk=risk_list[1]

#--Get the name from dictionary
    answer3 = answer.to_dict('dict')
    for key, val in answer3.items():
        if key == "name":
            name = val[0]
        if key == "age":
            age = val[0]
        if key == "obesity":
            obesity = val[0]
        if key == "smoke":
            smoke = val[0]
        if key == "alcohol":
            alcohol = val[0]

    img = Image.open("predict/ArrowRisk.jpg")
    st.image(img,use_column_width=True)
    st.markdown("_____________________")

    st.markdown(f"##### Dear {name},")
    st.markdown(f"Diabetes is a ‘silent’ disease in its early stages, and you may feel perfectly well until complications occur. A late diagnosis can result in serious and irreversible complications. Thank you for taking the first step to access your risk by completeing the questionnaires.")
    st.markdown(f"Base on the information that you provided, your chance of getting early stage diabetes positive is {chance} at {prob}%.")

    st.markdown("_______________________")
    c1,c2,c3=st.columns([1,0.8,0.8])
    with c1:
        st.info(f"##### Summary Result:")
        st.markdown(f"-  Diabetes Prognosis : {risk}")
        st.markdown(f"-  Probability of Diabetes : {prob}%")
        st.markdown(f"-  Diabetes Risk Level: {chance}")
    with c2:
        if chance == "low":
            img = Image.open("predict/ArrowMiss.jpg")
            st.image(img,use_column_width=True)
            if age > 40:
                Text_action = "You are doing good. Continue to maintain a good health. But since you are above 40, it is good to go for blood glucose test as a prevention afford."
        elif chance =="high":
            img = Image.open("predict/ArrowHit.jpg")
            st.image(img,use_column_width=True)
            Text_action = "You are strongly encourage to go for blood glucose test to accertain your risk and if you need medication."
        else:
            img = Image.open("predict/ArrowBad.jpg")
            st.image(img,use_column_width=True)
            Text_action = "You are encourage to go for blood glucose test to accertain your risk level."
    with c3:
        st.warning(f"###### Our Recommendation:")
        st.markdown(Text_action,unsafe_allow_html=True)
    st.markdown("_______________________")

    st.markdown("##### **Additional Remarks**")
    c1,c2=st.columns([2,1])
    if obesity ==1:
        with c1:
            st.markdown("Your BMI shows that you are obesity. We suggest that you consider losing weight through healthy eating and being more physically active.")
            st.markdown("Obesity increase the risk of diabetes by 3times of normal weight.")
        with c2:
            img = Image.open("predict/FoodHealthy.jpg")
            st.image(img,use_column_width=True)

    c1,c2=st.columns([2,1])
    if smoke > 1:
        with c1:
            st.markdown("You are a smoker. We suggest that you considering quit smoking.")
            st.markdown("Smokers are 30% to 40% more likely to develop diabetes than nonsmokers as high levels of nicotine makes regulate blood sugar more difficult. Quitting smoking is also the single best way to protect family members, coworkers and friends from the health risks associated with breathing secondhand smoke")
        with c2:
            img = Image.open("predict/NoSmoke.jpg")
            st.image(img,use_column_width=True)
    
    c1,c2=st.columns([2,1])
    if alcohol ==0:
        with c1:
            st.markdown("You dont drink alcohol. No harm to drink a little.")
            st.markdown("Heavy consumption or no alcohol increase the risk of Diabetes. Moderate drinking of lesser than 4glass per week is good for health")
        with c2:
            img = Image.open("predict/Wine.jpg")
            st.image(img,use_column_width=True)
    elif alcohol>4:
            with c1:
                st.markdown("You probably consume too much alcohol.")
                st.markdown("Heavy consumption or no alcohol increase the risk of Diabetes. Moderate drinking of lesser than 4glass per week is good for health")
            with c2:
                img = Image.open("predict/Wine.jpg")
                st.image(img,use_column_width=True)
            st.markdown("_______________________")

    st.subheader("Prognosis Evaluation")
    Text_Eval = ('<p style="font-family:Arial;color:black;font-size:18px;">How accurate is the Diabetes prognosis? Do you have Diabetes? </p>')
    st.markdown(Text_Eval,unsafe_allow_html=True)
    st.text("<*><*><*><*><*><*><*><*><*>")
    if st.button("I am Diabetes Positive",key="E1"):
        diabetes_act = 1
        diabetes_final = {'name':name,'age':age,"diabetes_act":diabetes_act}
        diabetes_final = pd.DataFrame(data/diabetes_final,index=[0])
        diabetes_final.to_csv('data/diabetes_final.csv',index=False)
    elif st.button("I am Diabetes Negetive",key="E2"):
        diabetes_act = 0
        diabetes_final = {'name':name,'age':age,"diabetes_act":diabetes_act}
        diabetes_final = pd.DataFrame(diabetes_final,index=[0])
        diabetes_final.to_csv('data/diabetes_final.csv',index=False)
    elif st.button("I dont know",key="E3"):
        diabetes_act = 99
        diabetes_final = {'name':name,'age':age,"diabetes_act":diabetes_act}
        diabetes_final = pd.DataFrame(diabetes_final,index=[0])
        diabetes_final.to_csv('data/diabetes_final.csv',index=False)
    else:
        st.text("")

    st.text("<*><*><*><*><*><*><*><*><*>")
    st.info(f"##### Dear {name}, Thank you for your information. This will help us improve our machine learning accuracy for future prognosis.")

    st.write('---The End---')

    #--Concate to master
    df = pd.read_csv('data/master.csv')
    master = pd.concat([df,answer], axis=0)
    master.to_csv('data/master.csv',index=False)

    
