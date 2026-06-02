from django.shortcuts import render, redirect
from .models import Budget
from .forms import BudgetForm

# Create your views here.
def budget(request):
    return render(request, "budget_app/budget.html")

# add item to budget
def add_budget(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_page')
    else:
        form = BudgetForm()
    return render(request, "budget_app/add_budget.html", {"form": form})

# view all budget
def view_budget(request):
    budgets = Budget.objects.all()
    return render(request, "budget_app/budget.html", {"budgets": budgets})