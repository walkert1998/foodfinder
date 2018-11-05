from foodapp.models import Restaurant, Review
from django import forms

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name','rating', 'review_text')
