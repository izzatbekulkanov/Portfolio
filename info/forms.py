from django.forms import ModelForm
from .models import Message, Education
from django import forms

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']

class CreateEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['title', 'description', 'the_year']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 50:
            raise forms.ValidationError("Title should not exceed 50 characters.")
        return title

    def clean_the_year(self):
        the_year = self.cleaned_data.get('the_year')
        if not the_year.isdigit():
            raise forms.ValidationError("Year must be numeric.")
        return the_year