from django.urls import path
from . import views

urlpatterns = [
    path("", views.expense_list, name="expense_list"),
    path("add/", views.add_expense, name="add_expense"),
    path("delete/<int:id>/", views.delete_expense, name="delete_expense"),
    path("summary/", views.expense_summary, name="expense_summary"),
    path("signup/", views.signup, name="signup"),

]
