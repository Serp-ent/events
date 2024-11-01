from .models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "location", "birth_date", 'avatar']
        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "class": "w-full p-2 border border-gray-300 rounded resize-none",
                    "rows": 5,
                }
            ),
            "location": forms.TextInput(
                attrs={"class": "w-full p-2 border border-gray-300 rounded"}
            ),
            "birth_date": forms.DateInput(
                attrs={
                    "class": "w-full p-2 border border-gray-300 rounded",
                    "type": "date",
                }
            ),
        }
