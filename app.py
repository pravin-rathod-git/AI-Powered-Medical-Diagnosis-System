import streamlit as st
import pickle

st.set_page_config(page_title="Medical Diagnosis Using AI", page_icon="🧑‍⚕️")

custom_css = """
<style>
@keyframes gradientAnimation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, midnightblue, steelblue, deepskyblue, dodgerblue, royalblue);
    background-size: 400% 400%;
    animation: gradientAnimation 10s ease infinite;
    color: black;
    font-family: Arial, sans-serif;
    text-align: center;
    min-height: 100vh;
    padding: 20px;
}
.stTextInput, .stNumberInput, .stSelectbox, .stButton {
    border-radius: 10px;
    padding: 14px;
    margin-bottom: 18px;
    background: black;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: 2px solid grey;
    display: inline-block;
    width: 48%;
    margin-right: 2%;
    text-align: left;
}
.stTextInput > div > input, .stNumberInput > div > input {
    background: transparent;
    color: red;
    font-size: 18px;
    font-weight: bold;
}
.stButton > button {
    background-color: white;
    color: blue;
    font-size: 20px;
    padding: 16px;
    border-radius: 12px;
    transition: 0.1s;
    display: block;
    margin: 20px auto;
}
.stButton > button:hover {
    background-color: lightred;
    color: black;
}
.tooltip {
    font-size: 18px;
    color: black;
    font-weight: bold;
}
.stsuccess {
    background-color: black !important;
    color: red !important;
    font-size: 24px !important;
    font-weight: bold !important;
    padding: 20px !important;
    border-radius: 10px !important;
    text-align: center !important;
    border: 3px solid white !important;
}
.result-box {
    background-color: white;
    color: green;
    font-size: 22px;
    font-weight: bold;
    padding: 15px;
    border-radius: 12px;
    border: 3px solid #28a745;
    text-align: center;
    margin-top: 20px;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
}
#MainMenu, footer, header {
    visibility: hidden;
}
</style>"""
st.markdown(custom_css, unsafe_allow_html=True)

st.title("Medical Diagnosis Using AI")

# Load trained models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Disease selection dropdown
selected = st.selectbox('Select a Disease to Predict', [
    'Diabetes Prediction',
    'Heart Disease Prediction',
    'Parkinsons Prediction',
    'Lung Cancer Prediction',
    'Hypo-Thyroid Prediction'
])

def display_input(label, tooltip, key, type="text"):
    return st.number_input(f"{label} ({tooltip})", key=key) if type == "number" else st.text_input(f"{label} ({tooltip})", key=key)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    st.write("Enter the following details to predict diabetes:")

    Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
    BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
    SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
    Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
    BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')
 
    diab_diagnosis = ''
    if st.button("Diabetes Test Result"):
       diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
       diab_diagnosis = "The person is diabetic" if diab_prediction[0] == 1 else "The person is not diabetic"
       st.markdown(f'<div class="result-box">{diab_diagnosis}</div>', unsafe_allow_html=True)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict heart disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.markdown(f'<div class="result-box">{heart_diagnosis}</div>', unsafe_allow_html=True)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease:")

    fo = display_input('MDVP: Fo(Hz)','Enter fundamental frequency', 'fo', 'number')
    fhi = display_input('MDVP: Fhi(Hz)','Enter highest frequency.', 'fhi', 'number')
    flo = display_input('MDVP: Flo(Hz)','Enter lowest frequency.', 'flo', 'number')
    Jitter_percent = display_input('MDVP: Jitter(%)','Enter percentage of jitter.', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('MDVP: Jitter(Abs)','Enter absolute jitter.', 'Jitter_Abs', 'number')
    RAP = display_input('MDVP: RAP','Enter relative average perturbation.', 'RAP', 'number')
    PPQ = display_input('MDVP: PPQ','Enter pitch perturbation quotient.', 'PPQ', 'number')
    DDP = display_input('Jitter: DDP','Enter difference of differences of pitch.', 'DDP', 'number')
    Shimmer = display_input('MDVP: Shimmer','Enter amplitude perturbation.', 'Shimmer', 'number')
    Shimmer_dB = display_input('MDVP: Shimmer(dB)','Enter dB of shimmer.', 'Shimmer_dB', 'number')
    APQ3 = display_input('Shimmer: APQ3 - amplitude perturbation quotient.', 'Enter Shimmer: APQ3 value', 'APQ3', 'number')
    APQ5 = display_input('Shimmer: APQ5 - amplitude perturbation quotient.', 'Enter Shimmer: APQ5 value', 'APQ5', 'number')
    APQ = display_input('MDVP: APQ - average perturbation quotient.', 'Enter MDVP: APQ value', 'APQ', 'number')
    DDA = display_input('Shimmer: DDA - difference of differences of amplitude.', 'Enter Shimmer: DDA value', 'DDA', 'number')
    NHR = display_input('NHR - normalized noise-to-harmonic ratio.', 'Enter NHR value', 'NHR', 'number')
    HNR = display_input('HNR - harmonic-to-noise ratio.', 'Enter HNR value', 'HNR', 'number')
    RPDE = display_input('RPDE - nonlinear dynamical complexity.', 'Enter RPDE value', 'RPDE', 'number')
    DFA = display_input('DFA - detrended fluctuation analysis.', 'Enter DFA value', 'DFA', 'number')
    spread1 = display_input('Spread1', 'Enter spread of the first frequency ', 'spread1', 'number')
    spread2 = display_input('Spread2', 'Enter spread of the second frequency', 'spread2', 'number')
    D2 = display_input('D2 - distance measure.', 'Enter D2 value', 'D2', 'number')
    PPE = display_input('PPE - pitch period entropy.', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.markdown(f'<div class="result-box">{parkinsons_diagnosis}</div>', unsafe_allow_html=True)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer")
    st.write("Enter the following details to predict lung cancer:")
    
    GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
    AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
    SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
    ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
    FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
    ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
    WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
    COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
    CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.markdown(f'<div class="result-box">{lungs_diagnosis}</div>', unsafe_allow_html=True)

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid")
    st.write("Enter the following details to predict hypo-thyroid disease:")
    
    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
    on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
    tsh = display_input('TSH Level', 'Enter TSH level', 'tsh', 'number')
    t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number')
    t3 = display_input('T3 Level', 'Enter T3 level', 't3', 'number')
    tt4 = display_input('TT4 Level', 'Enter TT4 level', 'tt4', 'number')

    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
        st.markdown(f'<div class="result-box">{thyroid_diagnosis}</div>', unsafe_allow_html=True)

st.write("\n**Disclaimer:** This prediction is AI-generated and should not replace medical advice.")