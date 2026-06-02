from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    type_choices = [
        ('credit', 'credit'),
        ('debit', 'debit'),
    ]
    type = forms.ChoiceField(choices=type_choices)
    category_choices = [
        ('Rent/Electricity/Rechage', 'Rent/Electricity/Rechage'),
        ('Rice/Floor', 'Rice/Floor'),
        ('Grocery', 'Grocery'),
        ('Vegetables', 'Vegetables'),
        ('Meat/Fish/Eggs', 'Meat/Fish/Eggs'),
        ('Diary/Fruits/Bread', 'Diary/Fruits/Bread'),
        ('Cleaning/Hygine', 'Cleaning/Hygine'),
        ('Water/Gas', 'Water/Gas'),
        ('Family', 'Family'),
        ('Medical', 'Medical'),
        ('Travel', 'Travel'),
        ('Other', 'Other')
    ]
    category = forms.ChoiceField(choices=category_choices)

    class Meta:
        model = Account
        fields = ['date', 'type', 'description', 'amount', 'category']