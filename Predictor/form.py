from django import forms
from django.utils.safestring import mark_safe


class HeartDiseaseForm(forms.Form):
    AgeCategory = forms.ChoiceField(label="What age-category you belong in?", widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('18-24', '18-24'), ('25-29', '25-29'), ('30-34', '30-34'), ('35-39', '35-39'), ('40-44', '40-44'), ('45-49', '45-49'), ('50-54', '50-54'), ('55-59', '55-59'), ('60-64', '60-64'), ('65-69', '65-69'), ('70-74', '70-74'), ('75-79', '75-79'), ('80 or older', '80 or older')])
    BMICategory = forms.ChoiceField(label="What body mass index category you belong in?", widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('Underweight (BMI < 18.5)', 'Underweight (BMI < 18.5)'), ('Normal weight (18.5 <= BMI < 25.0)', 'Normal weight (18.5 <= BMI < 25.0)'), ('Overweight (25.0 <= BMI < 30.0)', 'Overweight (25.0 <= BMI < 30.0)'), ('Obese (30.0 <= BMI < +Inf)', 'Obese (30.0 <= BMI < +Inf)')])
    Sex = forms.ChoiceField(label="Are you a male or a female?", choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    Race = forms.ChoiceField(label="What is your imputed race / ethnic value?", widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('American Indian/Alaskan Native', 'American Indian/Alaskan Native'), ('Asian', 'Asian'), ('Black', 'Black'), ('Hispanic', 'Hispanic'), ('Other', 'Other'), ('White', 'White')])
    PhysicalActivity = forms.ChoiceField(label="Have you done physical activity or exercise during the past 30 days other than your regular job?", choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    DiffWalking = forms.ChoiceField(label="Do you have serious difficulty walking or climbing stairs?", choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    PhysicalHealth = forms.IntegerField(label="Thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?", widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter PhysicalHealth'}))
    MentalHealth = forms.IntegerField(label="Thinking about your mental health, for how many days during the past 30 days was your mental health not good?", widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter MentalHealth'}))
    GenHealth = forms.ChoiceField(label="Would you say that in general your health is:", widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('Poor', 'Poor'), ('Fair', 'Fair'), ('Good', 'Good'), ('Very good', 'Very good'), ('Excellent', 'Excellent')])
    SleepTime = forms.IntegerField(label="On average, how many hours of sleep do you get in a 24-hour period?", widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter SleepTime'}))
    Smoking = forms.ChoiceField(label="Have you smoked at least 100 cigarettes in your entire life?", choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    AlcoholDrinking = forms.ChoiceField(label="Do you consume more than 14 alcoholic drinks per week ( if you are a male ) or more than 7 alcoholic drinks per week ( if you are a female )?", choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    Stroke = forms.ChoiceField(label="Were you ever told / have you ever had a stroke?", choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    Asthma = forms.ChoiceField(label="Were you ever told / have you ever had asthma?", choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    SkinCancer = forms.ChoiceField(label="Were you ever told / have you ever had skin cancer?", choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    Diabetic = forms.ChoiceField(label="Have you ever had diabetes?", widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('No', 'No'), ('No, borderline diabetes', 'No, borderline diabetes'), ('Yes', 'Yes'), ('Yes (during pregnancy)', 'Yes (during pregnancy)'), ('Not sure and would like to check online', 'Not sure and would like to check online')])
    HighBP = forms.ChoiceField(required=False, label=mark_safe("Have you been told that you have high blood pressure by a doctor, nurse, or other health professional?<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    CholCheck = forms.ChoiceField(required=False, label=mark_safe("Have you checked your cholesterol within past 5 years?<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    HighChol = forms.ChoiceField(required=False, label=mark_safe("Have you been told that you have high cholesterol by a doctor, nurse, or other health professional?<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    Fruits = forms.ChoiceField(required=False, label=mark_safe("Do you consume fruits once or more each day?<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    Veggies = forms.ChoiceField(required=False, label=mark_safe("Do you consume vegetables once or more each day?<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    Pregnant = forms.ChoiceField(required=False, label=mark_safe("If you are a female then are you pregnant at this moment? ( Select 'No' if you are a male )<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    Education = forms.ChoiceField(required=False, label=mark_safe("What is the highest grade or year of school you completed?<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('Never attended school or only kindergarden', 'Never attended school or only kindergarden'), ('Grades 1 through 8 (Elementary)', 'Grades 1 through 8 (Elementary)'), ('Grades 9 through 11 (Some high school)', 'Grades 9 through 11 (Some high school)'), ('Grade 12 or GED (High school graduate)', 'Grade 12 or GED (High school graduate)'), ('College 1 year to 3 years (Some college or technical school)', 'College 1 year to 3 years (Some college or technical school)'), ('College 4 years or more (College graduate)', 'College 4 years or more (College graduate)')])
    Income = forms.ChoiceField(required=False, label=mark_safe("What is your annual household income from all sources?<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('Less than $10,000', 'Less than $10,000'), ('$10,000 to less than $15,000', '$10,000 to less than $15,000'), ('$15,000 to less than $20,000', '$15,000 to less than $20,000'), ('$20,000 to less than $25,000', '$20,000 to less than $25,000'), ('$25,000 to less than $35,000', '$25,000 to less than $35,000'), ('$35,000 to less than $50,000', '$35,000 to less than $50,000'), ('$50,000 to less than $75,000', '$50,000 to less than $75,000'), ('$75,000 or more', '$75,000 or more')])
    AnyHealthcare = forms.ChoiceField(required=False, label=mark_safe("Do you have any kind of health care coverage, including health insurance, prepaid plans or government plans?<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    NoDocbcCost = forms.ChoiceField(required=False, label=mark_safe("Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?<br /><br /><strong>( Answer required only for checking diabetes online )</strong>"), choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    KidneyDisease = forms.ChoiceField(label="Do you have kidney disease?", widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('No', 'No'), ('Yes', 'Yes'), ('Not sure and would like to check online', 'Not sure and would like to check online')])
    Bp = forms.FloatField(required=False, label=mark_safe("What is your blood pressure in mm/Hg?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Bp'}))
    Bu = forms.FloatField(required=False, label=mark_safe("What is your blood urea in mgs/dl?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Bu'}))
    Sc = forms.FloatField(required=False, label=mark_safe("What is your serum creatinine in mgs/dl?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Sc'}))
    Sod = forms.FloatField(required=False, label=mark_safe("What is your sodium in mEq/L?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Sod'}))
    Pot = forms.FloatField(required=False, label=mark_safe("What is your potassium in mEq/L?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Pot'}))
    Hemo = forms.FloatField(required=False, label=mark_safe("What is your hemoglobin in gms?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Hemo'}))
    Wbcc = forms.FloatField(required=False, label=mark_safe("What is your white blood cell count in cells/cumm?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Wbcc'}))
    Rbcc = forms.FloatField(required=False, label=mark_safe("What is your red blood cell count in millions/cmm?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Rbcc'}))
    Sg = forms.ChoiceField(required=False, label=mark_safe("What is your specific gravity level?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('1.005', '1.005'), ('1.01', '1.01'), ('1.015', '1.015'), ('1.02', '1.02'), ('1.025', '1.025')])
    Al = forms.ChoiceField(required=False, label=mark_safe("What is your albumin level?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
    Su = forms.ChoiceField(required=False, label=mark_safe("What is you sugar level?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), widget=forms.Select(attrs={'class': 'dropdown'}), choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    Rbc = forms.ChoiceField(required=False, label=mark_safe("Are your red blood cells normal or abnormal?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), choices=[('Normal', 'Normal'), ('Abnormal', 'Abnormal')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))
    Htn = forms.ChoiceField(required=False, label=mark_safe("Do you have hypertension?<br /><br /><strong>( Answer required only for checking kidney disease online )</strong>"), choices=[('Yes', 'Yes'), ('Occasionally', 'Occasionally'), ('No', 'No')], widget=forms.RadioSelect(attrs={'class': 'radiobox'}))