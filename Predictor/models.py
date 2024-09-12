from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# BOOLEAN_CHOICES = (
#     ('Yes', 'Yes'),
#     ('No', 'No')
# )

# BMI_CHOICES = (
#     ('Underweight (BMI < 18.5)', 'Underweight (BMI < 18.5)'),
#     ('Normal weight (18.5 <= BMI < 25.0)', 'Normal weight (18.5 <= BMI < 25.0)'),
#     ('Overweight (25.0 <= BMI < 30.0)', 'Overweight (25.0 <= BMI < 30.0)'),
#     ('Obese (30.0 <= BMI < +Inf)', 'Obese (30.0 <= BMI < +Inf)')
# )

# SEX_CHOICES = (
#     ('Male', 'Male'),
#     ('Female', 'Female')
# )

# AGE_CATEGORY_CHOICES = (
#     ('18-24', '18-24'),
#     ('25-29', '25-29'),
#     ('30-34', '30-34'),
#     ('35-39', '35-39'),
#     ('40-44', '40-44'),
#     ('45-49', '45-49'),
#     ('50-54', '50-54'),
#     ('55-59', '55-59'),
#     ('60-64', '60-64'),
#     ('65-69', '65-69'),
#     ('70-74', '70-74'),
#     ('75-79', '75-79'),
#     ('80 or older', '80 or older')
# )

# RACE_CHOICES = (
#     ('American Indian/Alaskan Native', 'American Indian/Alaskan Native'),
#     ('Asian', 'Asian'),
#     ('Black', 'Black'),
#     ('Hispanic', 'Hispanic'),
#     ('Other', 'Other'),
#     ('White', 'White')
# )

# DIABETIC_CHOICES = (
#     ('No', 'No'),
#     ('No, borderline diabetes', 'No, borderline diabetes'),
#     ('Yes', 'Yes'),
#     ('Yes (during pregnancy)', 'Yes (during pregnancy)')
# )

# GEN_HEALTH_CHOICES = (
#     ('Poor', 'Poor'),
#     ('Fair', 'Fair'),
#     ('Good', 'Good'),
#     ('Very good', 'Very good'),
#     ('Excellent', 'Excellent')
# )

# class HeartDisease(models.Model):
#     HeartDisease = models.CharField(max_length=5, choices=BOOLEAN_CHOICES)
#     BMICategory = models.CharField(max_length=40, choices=BMI_CHOICES)
#     Smoking = models.CharField(max_length=5, choices=BOOLEAN_CHOICES)
#     AlcoholDrinking = models.CharField(max_length=5, choices=BOOLEAN_CHOICES)
#     Stroke = models.CharField(max_length=5, choices=BOOLEAN_CHOICES)
#     PhysicalHealth = models.IntegerField(validators=[MaxValueValidator(30), MinValueValidator(0)])
#     MentalHealth = models.IntegerField(validators=[MaxValueValidator(30), MinValueValidator(0)])
#     DiffWalking = models.CharField(max_length=5, choices=BOOLEAN_CHOICES)
#     Sex = models.CharField(max_length=10, choices=SEX_CHOICES)
#     AgeCategory = models.CharField(max_length=15, choices=AGE_CATEGORY_CHOICES)
#     Race = models.CharField(max_length=35, choices=RACE_CHOICES)
#     Diabetic = models.CharField(max_length=25, choices=DIABETIC_CHOICES)
#     PhysicalActivity = models.CharField(max_length=5, choices=BOOLEAN_CHOICES)
#     GenHealth = models.CharField(max_length=15, choices=GEN_HEALTH_CHOICES)
#     SleepTime = models.IntegerField(validators=[MaxValueValidator(24), MinValueValidator(0)])
#     Asthma = models.CharField(max_length=5, choices=BOOLEAN_CHOICES)
#     KidneyDisease = models.CharField(max_length=5, choices=BOOLEAN_CHOICES)
#     SkinCancer = models.CharField(max_length=5, choices=BOOLEAN_CHOICES)
