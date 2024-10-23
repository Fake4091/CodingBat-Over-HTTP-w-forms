from django import forms


class FrontForm(forms.Form):
    string = forms.CharField(label="String", max_length=100)
    n = forms.IntegerField(label="Number of Times", min_value=0)


class NoTeenForm(forms.Form):
    a = forms.IntegerField(label="A")
    b = forms.IntegerField(label="B")
    c = forms.IntegerField(label="C")


class XYZForm(forms.Form):
    string = forms.CharField(label="String")


class CenteredAvgForm(forms.Form):
    a = forms.IntegerField(label="Number 1")
    b = forms.IntegerField(label="Number 2")
    c = forms.IntegerField(label="Number 3")
    d = forms.IntegerField(label="Number 4", required=False)
    e = forms.IntegerField(label="Number 5", required=False)
    f = forms.IntegerField(label="Number 6", required=False)
    g = forms.IntegerField(label="Number 7", required=False)
    h = forms.IntegerField(label="Number 8", required=False)
