from django.shortcuts import render
from .models import Account
from .forms import AccountForm

# Create your views here.
def accounts(request):
    return render(request, "accounts_app/accounts.html")

# Create transaction view
def add_transaction(request):
    if request.method == "POST":
        # Handle form submission and save transaction
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountForm()
    return render(request, "accounts_app/add_transaction.html", {"form": form})

# Create transaction view
def view_accounts(request):
    return render(request, "accounts_app/accounts.html")