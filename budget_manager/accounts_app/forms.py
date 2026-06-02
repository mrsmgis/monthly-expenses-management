from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    type_choices = [
        ('debit', 'debit'),
        ('credit', 'credit')
    ]
    type = forms.ChoiceField(choices=type_choices)
    debit_categories = [
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
    credit_categories = [
        ('Salary', 'Salary'),
        ('Business', 'Business'),
        ('Investment', 'Investment'),
        ('Gift', 'Gift'),
        ('Other', 'Other')
    ]
    category = forms.ChoiceField(choices=[('debit', debit_categories), ('credit', credit_categories)])

    class Meta:
        model = Account
        fields = ['date', 'type', 'description', 'amount', 'category']