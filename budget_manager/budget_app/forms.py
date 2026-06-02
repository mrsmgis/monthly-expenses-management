from django import forms
from .models import Budget

from datetime import datetime

current_month = datetime.now().strftime("%B")
class BudgetForm(forms.ModelForm):
    month_choices = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    month = forms.ChoiceField(choices=month_choices, initial=current_month)
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
        model = Budget
        fields = ['category', 'amount', 'month']