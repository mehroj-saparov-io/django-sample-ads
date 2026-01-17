from django import forms
from .models import Ad


class AdCreateForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=127)
    description = forms.CharField(min_length=10, widget=forms.Textarea)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()

    def save(self):
        return Ad.objects.create(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email'],
        )
