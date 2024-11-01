from .models import Event
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "name",
            "description",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "participant_limit",
            "photo",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter event name",
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter a description for the event.",
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md",
                    "rows": 4,
                }
            ),
            "start_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md",
                }
            ),
            "start_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md",
                }
            ),
            "end_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md",
                }
            ),
            "participant_limit": forms.NumberInput(
                attrs={
                    "placeholder": "Max participants",
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md",
                }
            ),
            "photo": forms.ClearableFileInput(
                attrs={"class": "w-full px-3 py-2 border border-gray-300 rounded-md"},
            ),
        }

    photo = forms.ImageField(
        required=False,
        label="Event Photo",
        help_text="Optional. Upload an image to represent the event.",
        widget=forms.ClearableFileInput(
            attrs={"class": "w-full px-3 py-2 border border-gray-300 rounded-md"}
        ),
    )
