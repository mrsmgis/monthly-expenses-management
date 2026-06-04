from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from .forms import AccountForm
from django.db.models import Sum

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
            return redirect('accounts_page')
    else:
        form = AccountForm()
    return render(request, "accounts_app/add_transaction.html", {"form": form})

# Create transaction view
def view_accounts(request):
    accounts = Account.objects.all()
    total_debit = Account.objects.filter(type='debit').aggregate(Sum('amount'))['amount__sum'] or 0
    total_credit = Account.objects.filter(type='credit').aggregate(Sum('amount'))['amount__sum'] or 0
    current_balance = total_credit - total_debit
    return render(request, "accounts_app/accounts.html", {"accounts": accounts, "total_debit": total_debit, "total_credit": total_credit, "current_balance": current_balance})

#  Create delete transaction 
def delete_transaction(request, pk):
    transaction = get_object_or_404(Account, pk=pk)
    transaction.delete()
    return redirect('accounts_page')

def edit_transaction(request, pk):
    pass


# show the total debit credit balance
def show_total(request):
    total_debit = Account.objects.filter(type='debit').aggregate(Sum('amount'))['amount_sum'] or 0
    return render(request, "accounts_app/accounts.html", {"total_debit": total_debit})