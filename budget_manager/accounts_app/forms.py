from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    type_choices = [
        ('credit', 'credit'),
        ('debit', 'debit'),
    ]
    type = forms.ChoiceField(choices=type_choices)
    category_choices = [
        ('Food', 'Food'),
        ('Rent', 'Rent'),
        ('Utilities', 'Utilities'),
        ('Entertainment', 'Entertainment'),
        ('Transportation', 'Transportation'),
        ('Healthcare', 'Healthcare'),
        ('Other', 'Other'),
    ]
    category = forms.ChoiceField(choices=category_choices)

    class Meta:
        model = Account
        fields = ['date', 'type', 'description', 'amount', 'category']