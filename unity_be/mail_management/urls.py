from django.urls import path
from . import views


urlpatterns = [
    path("healthcheck/", views.healthcheck.as_view()),
    path('add_partner/', views.AddPartner.as_view()),
    path('add_mail/', views.AddMail.as_view()),
    path('get_list_mail/', views.GetListMails.as_view()),
    path('get_number_mail/', views.GetNumMails.as_view()),
    path('get_number_new_mail/', views.GetNumNewMails.as_view()),
]

