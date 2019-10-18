from django.urls import path

from . import views

urlpatterns = [
    path('expenses', views.ExpenseList.as_view()),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view()),
]
