import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/abhis/Desktop/Multiple Disease Pred/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/abhis/Desktop/Multiple Disease Pred/saved models/heart_disease_model.sav','rb'))

liver_model = pickle.load(open('C:/Users/abhis/Desktop/Multiple Disease Pred/saved models/model_lr_liver.sav', 'rb'))

# lung_model = pickle.load(open('C:/Users/abhis/Desktop/Multiple Disease Pred/saved models/model_lung.pkl', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Liver Disease Prediction',
                           ],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.number_input('Glucose Level')
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value')
    
    with col2:
        Insulin = st.number_input('Insulin Level')
    
    with col3:
        BMI = st.number_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.number_input('Age of the Person')
    
    
    # code for Prediction
    diabetes_diagnosis = ''
    if st.button('Diabetes Disease Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])                          
            
        if (diabetes_prediction[0] == 1):
            diabetes_diagnosis = 'The person is having diabetes'
        else:
            diabetes_diagnosis = 'The person does not have any diabetes'
            
    st.success(diabetes_diagnosis)
        


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 1 = normal; 2 = fixed defect; 3 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    

# Liver Prediction Page
if (selected == "Liver Disease Prediction"):
    
    # page title
    st.title("Liver Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        fo = st.number_input('Age')
        
    with col2:
        fhi = st.number_input('Gender')
        
    with col3:
        flo = st.number_input('Total_Bilirubin')
        
    with col1:
        Jitter_percent = st.number_input('Direct_Bilirubin')
        
    with col2:
        Jitter_Abs = st.number_input('Alkaline_Phosphotase')
        
    with col3:
        RAP = st.number_input('Alamine_Aminotransferase')
        
    with col1:
        PPQ = st.number_input('Aspartate_Aminotransferase')
        
    with col2:
        DDP = st.number_input('Total_Protiens')
        
    with col3:
        Shimmer = st.number_input('Albumin')
        
    with col1:
        Shimmer_dB = st.number_input('Albumin_and_Globulin_Ratio')
        
    
        
    # code for Prediction
    Liver_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Liver Disease Test Result"):
        liver_prediction = liver_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB]])                          
        
        if (liver_prediction[0] == 1):
          Liver_diagnosis = 'The person has Lung disease'
        else:
          Liver_diagnosis = 'The person does not have Lung disease'
        
    st.success(Liver_diagnosis)


# # Lung Prediction Page
# if (selected == "Lung Disease Prediction"):
    
#     # page title
#     st.title("Lung's Disease Prediction using ML")
    
#     col1, col2, col3, col4= st.columns(4)  
    
#     with col1:
#         Gender = st.number_input('GENDER')
        
#     with col2:
#         Age = st.number_input('AGE')
        
#     with col3:
#         Yellow_Fingers = st.number_input('YELLOW_FINGERS')
        
#     with col4:
#         Anxiety = st.number_input('ANXIETY')
        
#     with col1:
#         Peer_Pressure = st.number_input('PEER_PRESSURE')
        
#     with col2:
#         Chronic_Disease = st.number_input('CHRONIC DISEASE')
        
#     with col3:
#         Fatigue = st.number_input('FATIGUE')
        
#     with col3:
#         Allergy = st.number_input('ALLERGY')
        
#     with col4:
#         Wheezing = st.number_input('WHEEZING')
        
#     with col1:
#         Alchol_Consuming = st.number_input('ALCOHOL CONSUMING')

#     with col2:
#         Coughing = st.number_input('COUGHING')

#     with col3:
#         Shortness_of_breath = st.number_input('SHORTNESS OF BREATH')

#     with col4:
#         Swallowing_Difficulty = st.number_input('SWALLOWING DIFFICULTY')
        
#     with col1:
#         Chest_Pain = st.number_input('CHEST PAIN')

#     with col2:
#         Lung_Cancer = st.number_input('LUNG_CANCER')
        
    
    
#     # code for Prediction
#     Lung_diagonosis = ''
    
#     # creating a button for Prediction    
#     if st.button("Lung's Test Result"):
#         lung_prediction = lung_model.predict([[Gender, Age, Yellow_Fingers, Anxiety, Peer_Pressure, Chronic_Disease, Fatigue, Allergy, Wheezing, Alchol_Consuming, Coughing, Shortness_of_breath, Swallowing_Difficulty, Chest_Pain, Lung_Cancer]])                          
        
#         if (lung_prediction[0] == 1):
#           Lung_diagonosis = 'The person has Lung disease'
#         else:
#           Lung_diagonosis = 'The person does not have Lung disease'
        
#     st.success(Lung_diagonosis)

