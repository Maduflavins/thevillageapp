from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'forms-control',
        'placeholder': 'Enter your Comment',
        'id': 'userComment',
        'rows': '4'

    }))

    class Meta:
        model=Comment
        fields = ('content', )

