from django.shortcuts import render

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

from django.http import JsonResponse
from django.http import HttpResponse
import numpy
import pandas as pd
import numpy as np 
import joblib
from . models import LoanResults 
from . models import cardResults
from loan.models import cardResults 

from . models import cardResult
from loan.models import cardResult 
import json



from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
import json
from django.http import HttpResponse
import csv



# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('loan')
#         else:
#             error_message = 'Invalid login credentials. Please try again.'
#             return render(request, 'login.html', {'error_message': error_message})
#     else:
#         return render(request, 'login.html')





# Create your views here.
def loan(request):
    return render(request, 'loan.html')
def info(request):
    return render(request, 'info.html')




#Loan Prediction
def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Gender = float(request.POST.get('Gender'))
        Married =float(request.POST.get('Married'))
        Education =float(request.POST.get('Education'))
        Self_Employed =float(request.POST.get('Self_Employed'))
        ApplicantIncome = float(request.POST.get('ApplicantIncome'))
        CoapplicantIncome = float(request.POST.get('CoapplicantIncome'))
        LoanAmount = float(request.POST.get('LoanAmount'))
        Loan_Amount_Term = float(request.POST.get('Loan_Amount_Term'))
        Credit_History = float(request.POST.get('Credit_History'))
        Property_Area = float(request.POST.get('Property_Area'))

        # Unpickle model 
        model = joblib.load(r"C:\Users\ADMIN\Desktop\django\djangoapp\model.pkl")
        # model = pd.read_pickle(r"C:\Users\ADMIN\Desktop\django\djangoapp\\model.pkl")
        # Make prediction
        result = model.predict([[Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]])

        classification = result[0]

        LoanResults.objects.create(Gender=Gender, Married=Married, Education=Education, Self_Employed=Self_Employed, ApplicantIncome=ApplicantIncome, CoapplicantIncome=CoapplicantIncome, LoanAmount=LoanAmount, Loan_Amount_Term=Loan_Amount_Term, Credit_History=Credit_History, Property_Area=Property_Area, classification=classification)

        return JsonResponse({'result': classification, 'Gender': Gender,
                             'Married': Married, 'Education': Education, 'Self_Employed': Self_Employed,
                             'ApplicantIncome': ApplicantIncome, 'CoapplicantIncome': CoapplicantIncome, 'LoanAmount': LoanAmount, 'Loan_Amount_Term': Loan_Amount_Term, 'Credit_History': Credit_History, 'Property_Area': Property_Area,},
                            safe=False)


def loan_result(request):
    data = {"dataset": LoanResults.objects.all()}
    return render(request, "loanResult.html", data)


#######################################
#####################
#Card Fraud 
def predict_Fraud(request):

    if request.POST.get('action') == 'post':
        # Receive data from client
        Time = float(request.POST.get(('Time')))        
        V1 =float(request.POST.get(('V1')))
        V2 =float(request.POST.get(('V2')))
        V3 =float(request.POST.get(('V3')))
        V4 = float(request.POST.get(('V4')))
        V5 = float(request.POST.get(('V5')))
        V6 = float(request.POST.get(('V6')))
        V7 = float(request.POST.get(('V7')))
        V8 = float(request.POST.get(('V8')))
        V9 = float(request.POST.get(('V9')))
        V10 =float(request.POST.get(('V10')))
        V11 =float(request.POST.get(('V11')))
        V12 =float(request.POST.get(('V12')))
        V13 =float(request.POST.get(('V13')))
        V14 = float(request.POST.get(('V14')))
        V15 = float(request.POST.get(('V15')))
        V16 = float(request.POST.get(('V16')))
        V17 = float(request.POST.get(('V17')))
        V18 = float(request.POST.get(('V18')))
        V19 = float(request.POST.get(('V19')))
        V20 =float(request.POST.get(('V20')))
        V21 =float(request.POST.get(('V21')))
        V22 =float(request.POST.get(('V22')))
        V23 =float(request.POST.get(('V23')))
        V24 = float(request.POST.get(('V24')))
        V25 = float(request.POST.get(('V25')))
        V26 = float(request.POST.get(('V26')))
        V27 = float(request.POST.get(('V27')))
        V28 = float(request.POST.get(('V28')))
        Amount = float(request.POST.get(('Amount')))
       
        # Unpickle model 
        model1 = joblib.load(r"C:\Users\ADMIN\Desktop\django\djangoapp\model2.pkl")
        
        # Make prediction
        result1 = model1.predict([[Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount]])

        classification1 = int(result1[0])

        cardResult.objects.create(Time=Time, V1=V1, V2=V2, V3=V3, V4=V4, V5=V5, V6=V6, V7=V7, V8=V8, V9=V9, V10=V10, V11=V11, V12=V12, V13=V13, V14=V14, V15=V15, V16=V16, V17=V17, V18=V18, V19=V19, V20=V20, V21=V21, V22=V22, V23=V23, V24=V24, V25=V25, V26=V26, V27=V27, V28=V28, Amount=Amount, classification1=classification1)

        return JsonResponse({'result1' : classification1, 'Time' : Time, 'V1' : V1, 'V2' : V2, 'V3' : V3, 'V4' : V4, 'V5' : V5, 'V6' : V6, 'V7' : V7, 'V8' : V8, 'V9' : V9, 'V10' : V10, 'V11' : V11, 'V12' : V12, 'V13' : V13, 'V14' : V14, 'V15' : V15, 'V16' : V16, 'V17' : V17, 'V18' : V18, 'V19' : V19, 'V20' : V20, 'V21' : V21, 'V22' : V22, 'V23' : V23, 'V24' : V24, 'V25' : V25, 'V26' : V26, 'V27' : V27, 'V28' : V28, 'Amount' : Amount,},
                            safe=False)   
    
    return render(request, 'card.html')




def card_result(request):
    data = {"dataset": cardResult.objects.all()}
    return render(request, "cardResult.html", data)



# def loan_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="Loan_Result.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['Gender'])

#     Loan_Result = LoanResults.objects.all().values_list('Gender')
#     for user in Loan_Result:
#         writer.writerow(user)

#     return response

import csv
from django.http import HttpResponse
from loan.models import LoanResults
from loan.models import cardResult

def loan_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="loan_results.csv"'

    writer = csv.writer(response)
    writer.writerow(['Sr.No.','Gender', 'Married', 'Education', 'Self_Employed', 'Applicant_Income', 'Coapplicant_Income', 'Loan_Amount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Prediction'])

    results = LoanResults.objects.all()
    for result in results:
        writer.writerow([result.id, result.Gender, result.Married, result.Education, result.Self_Employed, result.ApplicantIncome, result.CoapplicantIncome, result.LoanAmount, result.Loan_Amount_Term, result.Credit_History, result.Property_Area, result.classification])

    return response

def card_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="card_results.csv"'

    writer = csv.writer(response)
    writer.writerow(['Sr.No.', 'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount', 'Prediction'])

    results = cardResult.objects.all()
    for result in results:
         writer.writerow([result.id, result.Time, result.V1, result.V2, result.V3, result.V4, result.V5, result.V6, result.V7, result.V8, result.V9, result.V10, result.V11, result.V12, result.V13, result.V14, result.V15, result.V16, result.V17, result.V18, result.V19, result.V20, result.V21, result.V22, result.V23, result.V24, result.V25, result.V26, result.V27, result.V28, result.Amount, result.classification1])

    return response
