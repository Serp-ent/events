from typing import Any
from .models import Event
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# TODO: add check if end date is after start event properties


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

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        start_time = cleaned_data.get("start_time")
        end_date = cleaned_data.get("end_date")
        end_time = cleaned_data.get("end_time")

        if start_date and start_time and end_date and end_time:
            # Combine date and time into a single datetime object
            start_datetime = timezone.make_aware(
                timezone.datetime.combine(start_date, start_time)
            )
            end_datetime = timezone.make_aware(
                timezone.datetime.combine(end_date, end_time)
            )

            # Check if the start datetime is before the end datetime
            if start_datetime >= end_datetime:
                raise ValidationError(
                    "The start date and time must be before the end date and time."
                )

        return cleaned_data


class EventsFilterForm(forms.Form):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Search by event name",
            }
        ),
    )
    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
            }
        ),
    )

    # Status filter using radio buttons
    status = forms.ChoiceField(
        required=False,
        choices=[
            ("", "Any status"),
            ("available", "Only Available"),
            ("expired", "Only Expired"),
            ("future", "Only Future Events"),
            ("in_progress", "Only In Progress"),
        ],
        widget=forms.RadioSelect(
            attrs={
                "class": "form-radio h-5 w-5 text-blue-600",
            }
        ),
    )

    # Checkbox for only events with available slots
    has_slots = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-checkbox h-5 w-5 text-blue-600",
            }
        ),
    )

    ordering = forms.ChoiceField(
        required=False,
        choices=[
            ("date_closest", "Closest in Date"),
            ("date_furthest", "Furthest in Date"),
            ("slots_highest", "Highest Slots Available"),
            ("slots_least", "Least Slots Available"),
        ],
        widget=forms.Select(
            attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
            }
        ),
    )
