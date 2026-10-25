from django.contrib.auth.models import User
from django import forms

from market.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "price", "category", "seller_note"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        # is_staff is a privilege flag, not a profile preference. Leaving it in
        # this form let any signed-in user grant themselves staff (admin site +
        # department desk) just by submitting their profile. Department-board
        # membership is assigned by an admin, not self-service.
        fields = ["first_name", "last_name", "email"]
