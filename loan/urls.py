from django.urls import path
from . import views

from .views import loan_csv
from .views import card_csv
from django.urls import path
from loan.views import loan_csv, loan_result
from loan.views import card_csv, card_result








app_name = 'loan'
urlpatterns = [
    path('', views.loan, name='loan'),
    path('info/', views.info, name='info'),
    
    path('loan/', views.predict_chances, name='submit_prediction'),
    
    path('loanResult/', views.loan_result, name='loanResult'),

    path('card/', views.predict_Fraud, name='Fraud_prediction'),
    path('cardResult/', views.card_result, name='cardResult'),

    # path('loanResult/', views.loan_csv, name='loan_csv'),
    path('loan_csv/', loan_csv, name='loan_csv'),
    path('loan_result/', loan_result, name='loan_result'),

    path('card_csv/', card_csv, name='card_csv'),
    path('card_result/', card_result, name='card_result'),

    

]

