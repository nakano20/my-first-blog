from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','location', 'text',)
        widgets = {
            'title': forms.Textarea(
                attrs={'rows': 1, 'cols': 30, 'placeholder': '何が起きていますか？'}
            ),
            'location': forms.Textarea(
                attrs={'rows': 1, 'cols': 30, 'placeholder': 'どこで被害がでていますか？'}
            ),
            'text': forms.Textarea(
                attrs={'rows': 10, 'cols': 30, 'placeholder': '詳細'}
            ),
        }
