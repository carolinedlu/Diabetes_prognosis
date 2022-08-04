import streamlit as st 
import streamlit.components.v1 as stc
#from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd

df = pd.read_csv("model/data.csv")

result = {'age':'age',
        'gender':'male or female',
        'polyuria':"Excessive Urine ~15litre per day",
        'polydipsia':"Excessive drinking ~6litre per day",
        'sudden_weight_loss':"At least 5kg with same diet/exercise routine.",
        'weakness':"Fatigue where rest may not relieve exhaustion & lethargy.",
        'polyphagia':"Excessive hunger even after eating.",
        'visual_blurring':"Visual_blurring, distorted or cloudy",
        'itching':"Itchy skin and painful.",
        'irritability':"Mood swing, Stress, depression and anxiety.",
        'delayed_healing':"Slow to heal, do not heal well, or never heal.",
        'partial_paresis':"Muscle movement is weakened but not paralysis",
        'alopecia':"Slow hair growth and hair loss in all area of body.",}  

def run_ml_app():
    st.subheader("What is Machine Learning Algorithms?")
    Text_data ='<p style="font-family:Arial;color:black;font-size:18px;">The prognosis of Diabetes is generated based on Machine Learning Algorithms. According to IBM, Machine Learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy. It is about training the machine to think like human to predict the future.</p>'
    st.markdown(Text_data,unsafe_allow_html=True)
    
#--Dataset
    st.markdown("### Dataset:")
    Text_data ='<p style="font-family:Arial;color:black;font-size:18px;">The dataset used to train machine learning was from UCI Machine Learning Repository. It contains the data of 520 patients sign and symptoms of newly diabetic or would be diabetic patient.</p>'
    st.markdown(Text_data,unsafe_allow_html=True)
    Text_variable ='<p style="font-family:Arial;color:black;font-size:18px;">There are total of 16variables in the data set such as:- age, gender,polyuria, polydipsia, sudden_weight_loss, weakness, polyphagia, genital_thrush, visual_blurring, itching, moody, delayed_healing, partial_paresis, muscle_stiffness, alopecia, obesity</p>'
    st.markdown(Text_variable,unsafe_allow_html=True)

    with st.expander("[ Definition ]"):
        st.write(result,unsafe_allow_html=True)

    st.markdown("### Datasource:")
    st.write("url >>  [https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset)")

#--Model---
    st.markdown("### Machine Learning Model")
    with st.expander("[ Click Model ]"):
        Text_model ='<p style="font-family:Arial;color:black;font-size:18px;">   Pycaret is used to stimulate Machine Learning Models for comparison. The top 5 models are performing well with Recall Rate above 90% as showned in comparison model. The final model selected was RF (Random Forest Classifier) with a Recall Rate of 97% and Precision Rate of 99%. Base on healthcare metrics, RF gives a Sensitivity Rate of 97% while the Specificity Rate of 99% too.</p>'
        st.markdown(Text_model,unsafe_allow_html=True)
        
        st.markdown("### Final Model Selected")
        st.info("""##
            Randam Forest Classifier Accuracy
            Sensitivity Rate: 97%
            Specificity Rate: 99%
            """)
        img = Image.open("model/ModelCompare.jpg")
        st.image(img,use_column_width=True)

        st.markdown("### Create Randam Forest Classifier Model")
        c1,c2=st.columns([1.5,1])
        with c1:
            img = Image.open("model/ModelSelectRF.jpg")
            st.image(img,use_column_width=True)
        with c2:
            st.text("")

    #--Features
        st.markdown("#### Features Important")
        c1,c2=st.columns([1.5,1])
        with c1:
            img = Image.open("model/FeatureRF.jpg")
        st.image(img,use_column_width=True)
        with c2:
            st.text("")

    #--Evaluation
        st.markdown("#### Evaluation Matrix")
        c1,c2=st.columns([2.5,1])
        with c1:
            img = Image.open("model/MatrixSelectRF.jpg")
            st.image(img,use_column_width=True)
        with c2:
            st.text("")
        st.markdown("#### Evaluation Curses")
        c1,c2=st.columns([1,1])
        with c1:
            img = Image.open("model/CurveTrainRF.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("model/CurveValidateRF.jpg")
            st.image(img,use_column_width=True)
        with c2:
            img = Image.open("model/CurveRecallRF.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("model/CurveROCRF.jpg")
            st.image(img,use_column_width=True)
    
    #--Prediction
        img = Image.open("model/PredictionRF.jpg")
        st.image(img,use_column_width=True)

#--Analysis
    st.markdown("#### Analysis of Variables:")
    with st.expander("[ Click Analysis ]"):    
        st.markdown("The sample has almost double male compares to female. while female has higher diabetes risk compares to man.")
        c1,c2,c3=st.columns([3.3,0.2,1.5])
        with c1:
            img = Image.open("ChartGender.jpg")
            st.image(img,use_column_width=True)
        with c2:
            st.text("")
        with c3:
            gender_count = st.dataframe(df['gender'].value_counts().T)
            st.markdown("The gender was made up of the following count for male(0) and female(1).")
            st.markdown("Note: diab+ refers to diabetes positive while diab- refers to diabetes negetive.")

        st.markdown("---------------------")
        st.text("")

        c1,c2=st.columns([3,1])
        with c1:
            st.markdown("The distribution of age is normal as shown below where majority of the patients age 31 to 60.")
            img = Image.open("ChartAge.jpg")
            st.image(img,use_column_width=True)
        st.markdown("---------------------")

        st.markdown("Variables used to train the machine show good correlation with diabetes as below. Men seem to show more obvious difference between those with diabetes and without diabetes.")

        c1,c2=st.columns([2,2])
        with c1:
            img = Image.open("chart/ChartUrine2.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("chart/ChartWater2.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("chart/ChartWeight2.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("chart/ChartTired2.jpg")
            st.image(img,use_column_width=True)
        with c2:
            img = Image.open("chart/ChartHunger2.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("chart/ChartVisual2.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("chart/ChartMood2.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("chart/ChartParesis2.jpg")
            st.image(img,use_column_width=True)
        st.markdown("---------------------")

        st.markdown("Below are variables where by itself, didnt show meaningful correlation. But when a patient has another symptom/s, this increases the risk of diabetes where the pattern become visible.")

        st.markdown("---------------------")
        c1,c2=st.columns([2,2])
        with c1:
            img = Image.open("chart/ChartGenital2.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("chart/ChartHeal2.jpg")
            st.image(img,use_column_width=True)
            st.text("")
        with c2:
            img = Image.open("chart/ChartGenitalHealHungry2.jpg")
            st.image(img,use_column_width=True)
            st.text("")
            st.markdown("When a patient has only thrush or difficult to health, the chart shows negetive correlation. But when a patient has thrush, delayed healing and polyphagia at the same time, the risk of diabetes increases for both man and woman.")

        st.markdown("Below variables alopecia and muscle_stiffness were dropped from the dataset as analysis shown contradicting result from the general known facts. There is a possibility of not well define or fail to describe the symptoms to patients which result in distortion in data collected. I dropped them so that they will not affect the machine learning. In the future if there is more concrete information available, these information will be added to the database to further increae the accuracy.")
         
        c1,c2=st.columns([2,2])
        with c1:
            img = Image.open("chart/ChartMuscle2.jpg")
            st.image(img,use_column_width=True)
            img = Image.open("chart/Charthair2.jpg")
            st.image(img,use_column_width=True)
        with c2:
            img = Image.open("chart/ChartObesity2.jpg")
            st.image(img,use_column_width=True)
            st.markdown("As for obesity, it was also dropped at prognosis as it is in the grey line where obesity cause diabetes but diabetes cause weight lose. The chart shows obesity is not a good gage due to this reason.")
        st.markdown("---------------------")