from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import json
from django.contrib.auth.forms import UserCreationForm

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, "expenses/expense_list.html", {"expenses": expenses})

@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm()
    return render(request, "expenses/add_expense.html", {"form": form})

@login_required
def delete_expense(request, id):
    expense = Expense.objects.get(id=id, user=request.user)
    expense.delete()
    return redirect("expense_list")
@login_required
def expense_summary(request):
    # Group expenses by category
    expenses = Expense.objects.filter(user=request.user)
    category_data = expenses.values("category").annotate(total=Sum("amount"))

    labels = [item["category"] for item in category_data]
    data = [float(item["total"]) for item in category_data]

    context = {
        "labels": json.dumps(labels),
        "data": json.dumps(data),
    }
    return render(request, "expenses/expense_summary.html", context)

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def landing_page(request):
    return render(request, "expenses/landing.html")
