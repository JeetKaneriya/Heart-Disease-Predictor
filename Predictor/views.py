from django.http import JsonResponse
from django.shortcuts import render
import joblib
import pandas as pd
from .form import HeartDiseaseForm
import json

# Create your views here.

kidney_disease_model = joblib.load('./static/models/LogisticRegressionClassifierForKidneyDisease.pkl')
diabetes_model = joblib.load('./static/models/LogisticRegressionClassifierForDiabetes.pkl')
heart_disease_model = joblib.load('./static/models/LogisticRegressionClassifierForHeartDisease.pkl')

def index(request):
    return render(request, 'index.html')

# def pivot_data(request):
#     dataset = pd.read_csv('./static/datasets/heart_2020_analysis.csv')
#     dataset.drop("Unnamed: 0", axis=1, inplace=True)
#     dataset = dataset.tail(130424)
#     data = json.loads(dataset.to_json(orient = "records"))
#     return JsonResponse(data, safe=False)

def analyseHeartDisease(request):
    return render(request, 'analyseHeartDisease(single).html')

def predictHeartDisease(request):
    kidney_prediction = None
    kidney_prediction_percentage = None
    diabetes_prediction = None
    diabetes_prediction_percentage = None
    heart_prediction = None
    heart_prediction_percentage = None

    if request.method == "POST":
        kidney = {}
        diabetes = {}
        heart = {}

        form = HeartDiseaseForm(request.POST)
        if form.is_valid():

            if form.cleaned_data['KidneyDisease'] == 'Not sure and would like to check online':
                kidney['Bp'] = [form.cleaned_data['Bp']]
                kidney['Bu'] = [form.cleaned_data['Bu']]
                kidney['Sc'] = [form.cleaned_data['Sc']]
                kidney['Sod'] = [form.cleaned_data['Sod']]
                kidney['Pot'] = [form.cleaned_data['Pot']]
                kidney['Hemo'] = [form.cleaned_data['Hemo']]
                kidney['Wbcc'] = [form.cleaned_data['Wbcc']]
                kidney['Rbcc'] = [form.cleaned_data['Rbcc']]

                for col in ['1.005', '1.01', '1.015', '1.02', '1.025']:
                    if form.cleaned_data['Sg'] == col:
                        kidney['Sg_' + col] = [1]
                    else:
                        kidney['Sg_' + col] = [0]

                for col in ['0', '1', '2', '3', '4']:
                    if form.cleaned_data['Al'] == col:
                        kidney['Al_' + col] = [1]
                    else:
                        kidney['Al_' + col] = [0]

                for col in ['0', '1', '2', '3', '4', '5']:
                    if form.cleaned_data['Su'] == col:
                        kidney['Su_' + col] = [1]
                    else:
                        kidney['Su_' + col] = [0]

                for col in ['Abnormal', 'Normal']:
                    if form.cleaned_data['Rbc'] == col:
                        kidney['Rbc_' + col] = [1]
                    else:
                        kidney['Rbc_' + col] = [0]

                for col in ['No', 'Occasionally', 'Yes']:
                    if form.cleaned_data['Htn'] == col:
                        kidney['Htn_' + col] = [1]
                    else:
                        kidney['Htn_' + col] = [0]

                kidney_test_data = pd.DataFrame.from_dict(kidney)

                if int(kidney_disease_model.predict(kidney_test_data)[0]) == 0:
                    kidney_prediction = 'No'
                else:
                    kidney_prediction = 'Yes'
                
                kidney_prediction_percentage = kidney_disease_model.predict_proba(kidney_test_data)[0][int(kidney_disease_model.predict(kidney_test_data)[0])]
                kidney_prediction_percentage = kidney_prediction_percentage * 100
                kidney_prediction_percentage = round(kidney_prediction_percentage, 2)

            else:
                kidney_prediction = form.cleaned_data['KidneyDisease']
                kidney_prediction_percentage = 100.00

            if form.cleaned_data['Diabetic'] == 'Not sure and would like to check online':
                diabetes['MentHlth'] = [form.cleaned_data['MentalHealth']]
                diabetes['PhysHlth'] = [form.cleaned_data['PhysicalHealth']]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['HighBP'] == col:
                        diabetes['HighBP_' + col] = [1]
                    else:
                        diabetes['HighBP_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['HighChol'] == col:
                        diabetes['HighChol_' + col] = [1]
                    else:
                        diabetes['HighChol_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['CholCheck'] == col:
                        diabetes['CholCheck_' + col] = [1]
                    else:
                        diabetes['CholCheck_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['Smoking'] == col:
                        diabetes['Smoker_' + col] = [1]
                    else:
                        diabetes['Smoker_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['Stroke'] == col:
                        diabetes['Stroke_' + col] = [1]
                    else:
                        diabetes['Stroke_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['PhysicalActivity'] == col:
                        diabetes['PhysActivity_' + col] = [1]
                    else:
                        diabetes['PhysActivity_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['Fruits'] == col:
                        diabetes['Fruits_' + col] = [1]
                    else:
                        diabetes['Fruits_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['Veggies'] == col:
                        diabetes['Veggies_' + col] = [1]
                    else:
                        diabetes['Veggies_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['AlcoholDrinking'] == col:
                        diabetes['HvyAlcoholConsump_' + col] = [1]
                    else:
                        diabetes['HvyAlcoholConsump_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['AnyHealthcare'] == col:
                        diabetes['AnyHealthcare_' + col] = [1]
                    else:
                        diabetes['AnyHealthcare_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['NoDocbcCost'] == col:
                        diabetes['NoDocbcCost_' + col] = [1]
                    else:
                        diabetes['NoDocbcCost_' + col] = [0]

                for col in ['Excellent', 'Fair', 'Good', 'Poor', 'Very good']:
                    if form.cleaned_data['GenHealth'] == col:
                        diabetes['GenHlth_' + col] = [1]
                    else:
                        diabetes['GenHlth_' + col] = [0]

                for col in ['No', 'Yes']:
                    if form.cleaned_data['DiffWalking'] == col:
                        diabetes['DiffWalk_' + col] = [1]
                    else:
                        diabetes['DiffWalk_' + col] = [0]

                for col in ['Female', 'Male']:
                    if form.cleaned_data['Sex'] == col:
                        diabetes['Sex_' + col] = [1]
                    else:
                        diabetes['Sex_' + col] = [0]

                for col in ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older']:
                    if form.cleaned_data['AgeCategory'] == col:
                        diabetes['Age_' + col] = [1]
                    else:
                        diabetes['Age_' + col] = [0]

                for col in ['College 1 year to 3 years (Some college or technical school)', 'College 4 years or more (College graduate)', 'Grade 12 or GED (High school graduate)', 'Grades 1 through 8 (Elementary)', 'Grades 9 through 11 (Some high school)', 'Never attended school or only kindergarden']:
                    if form.cleaned_data['Education'] == col:
                        diabetes['Education_' + col] = [1]
                    else:
                        diabetes['Education_' + col] = [0]

                for col in ['$10,000 to less than $15,000', '$15,000 to less than $20,000', '$20,000 to less than $25,000', '$25,000 to less than $35,000', '$35,000 to less than $50,000', '$50,000 to less than $75,000', '$75,000 or more', 'Less than $10,000']:
                    if form.cleaned_data['Income'] == col:
                        diabetes['Income_' + col] = [1]
                    else:
                        diabetes['Income_' + col] = [0]

                for col in ['Normal weight (18.5 <= BMI < 25.0)', 'Obese (30.0 <= BMI < +Inf)', 'Overweight (25.0 <= BMI < 30.0)', 'Underweight (BMI < 18.5)']:
                    if form.cleaned_data['BMICategory'] == col:
                        diabetes['BMICategory_' + col] = [1]
                    else:
                        diabetes['BMICategory_' + col] = [0]

                diabetes_test_data = pd.DataFrame.from_dict(diabetes)

                if int(diabetes_model.predict(diabetes_test_data)[0]) == 2:
                    if form.cleaned_data['Pregnant'] == 'Yes':
                        diabetes_prediction = 'Yes (during pregnancy)'
                    else:
                        diabetes_prediction = 'Yes'
                elif int(diabetes_model.predict(diabetes_test_data)[0]) == 1:
                    diabetes_prediction = 'No, borderline diabetes'
                else:
                    diabetes_prediction = 'No'

                diabetes_prediction_percentage = diabetes_model.predict_proba(diabetes_test_data)[0][int(diabetes_model.predict(diabetes_test_data)[0])]
                diabetes_prediction_percentage = diabetes_prediction_percentage * 100
                diabetes_prediction_percentage = round(diabetes_prediction_percentage, 2)

            else:
                diabetes_prediction = form.cleaned_data['Diabetic']
                diabetes_prediction_percentage = 100.00

            heart['PhysicalHealth'] = [form.cleaned_data['PhysicalHealth']]
            heart['MentalHealth'] = [form.cleaned_data['MentalHealth']]
            heart['SleepTime'] = [form.cleaned_data['SleepTime']]

            for col in ['Normal weight (18.5 <= BMI < 25.0)', 'Obese (30.0 <= BMI < +Inf)', 'Overweight (25.0 <= BMI < 30.0)', 'Underweight (BMI < 18.5)']:
                if form.cleaned_data['BMICategory'] == col:
                    heart['BMICategory_' + col] = [1]
                else:
                    heart['BMICategory_' + col] = [0]

            for col in ['No', 'Yes']:
                if form.cleaned_data['Smoking'] == col:
                    heart['Smoking_' + col] = [1]
                else:
                    heart['Smoking_' + col] = [0]

            for col in ['No', 'Yes']:
                if form.cleaned_data['AlcoholDrinking'] == col:
                    heart['AlcoholDrinking_' + col] = [1]
                else:
                    heart['AlcoholDrinking_' + col] = [0]
                
            for col in ['No', 'Yes']:
                if form.cleaned_data['Stroke'] == col:
                    heart['Stroke_' + col] = [1]
                else:
                    heart['Stroke_' + col] = [0]

            for col in ['No', 'Yes']:
                if form.cleaned_data['DiffWalking'] == col:
                    heart['DiffWalking_' + col] = [1]
                else:
                    heart['DiffWalking_' + col] = [0]

            for col in ['Female', 'Male']:
                if form.cleaned_data['Sex'] == col:
                    heart['Sex_' + col] = [1]
                else:
                    heart['Sex_' + col] = [0]

            for col in ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older']:
                if form.cleaned_data['AgeCategory'] == col:
                    heart['AgeCategory_' + col] = [1]
                else:
                    heart['AgeCategory_' + col] = [0]

            for col in ['American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic', 'Other', 'White']:
                if form.cleaned_data['Race'] == col:
                    heart['Race_' + col] = [1]
                else:
                    heart['Race_' + col] = [0]

            for col in ['No', 'No, borderline diabetes', 'Yes', 'Yes (during pregnancy)']:
                if diabetes_prediction == col:
                    heart['Diabetic_' + col] = [1]
                else:
                    heart['Diabetic_' + col] = [0]

            for col in ['No', 'Yes']:
                if form.cleaned_data['PhysicalActivity'] == col:
                    heart['PhysicalActivity_' + col] = [1]
                else:
                    heart['PhysicalActivity_' + col] = [0]

            for col in ['Excellent', 'Fair', 'Good', 'Poor', 'Very good']:
                if form.cleaned_data['GenHealth'] == col:
                    heart['GenHealth_' + col] = [1]
                else:
                    heart['GenHealth_' + col] = [0]

            for col in ['No', 'Yes']:
                if form.cleaned_data['Asthma'] == col:
                    heart['Asthma_' + col] = [1]
                else:
                    heart['Asthma_' + col] = [0]

            for col in ['No', 'Yes']:
                if kidney_prediction == col:
                    heart['KidneyDisease_' + col] = [1]
                else:
                    heart['KidneyDisease_' + col] = [0]

            for col in ['No', 'Yes']:
                if form.cleaned_data['SkinCancer'] == col:
                    heart['SkinCancer_' + col] = [1]
                else:
                    heart['SkinCancer_' + col] = [0]

            heart_test_data = pd.DataFrame.from_dict(heart)

            if int(heart_disease_model.predict(heart_test_data)[0]) == 0:
                heart_prediction = 'No'
            else:
                heart_prediction = 'Yes'

            heart_prediction_percentage = heart_disease_model.predict_proba(heart_test_data)[0][int(heart_disease_model.predict(heart_test_data)[0])]
            heart_prediction_percentage = heart_prediction_percentage * 100
            heart_prediction_percentage = round(heart_prediction_percentage, 2)

    form = HeartDiseaseForm()
    return render(request, 'predictHeartDisease.html', {'form': form, 'kidney_prediction': kidney_prediction, 'kidney_prediction_percentage': kidney_prediction_percentage, 'diabetes_prediction': diabetes_prediction, 'diabetes_prediction_percentage': diabetes_prediction_percentage, 'heart_prediction': heart_prediction, 'heart_prediction_percentage': heart_prediction_percentage})