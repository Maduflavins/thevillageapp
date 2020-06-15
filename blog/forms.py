from django import forms
from .models import Comment

class CommentsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Enter your content',
        'id':'usercomment',
        'rows':'4'
    }))

    class Meta:
        model=Comment
        fields=('content', )