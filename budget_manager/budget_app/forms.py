from django import forms
from .models import Budget


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
    month = forms.ChoiceField(choices=month_choices)

    class Meta:
        model = Budget
        fields = ['category', 'amount', 'month']