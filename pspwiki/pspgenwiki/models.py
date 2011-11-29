from django.db import models
from django import forms

class WikiForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(initial='First and last')
    chapter = forms.CharField(initial='Beta Nu')
    school = forms.CharField(initial='Cornell University')
    school_site = forms.CharField(initial='http://www.cornell.edu')
    inducted = forms.CharField(initial='Spring 2009')
    roll_number = forms.CharField(initial='', required=False)
    birth_date = forms.DateField()
    majors = forms.CharField(initial='Biology, Philosophy')
    nicknames = forms.CharField(initial='J-Po', required=False)
    awards = forms.CharField(initial='', required=False)
    early_frat_life = forms.CharField(widget=forms.Textarea, required=False)
    collegiate_years = forms.CharField(widget=forms.Textarea, required=False)
    bigs_littles = forms.CharField(widget=forms.Textarea, required=False)
    national_involvement = forms.CharField(widget=forms.Textarea,required=False)
    other_facts = forms.CharField(widget=forms.Textarea, required=False)
