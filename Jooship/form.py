from django import forms


class SearchTickerForm(forms.Form):
    ticker = forms.CharField()

# End of File
