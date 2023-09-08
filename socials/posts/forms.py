from django import forms
from posts.models import Post,Comment


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('user','text')

        widgets = {
            'user':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea()
        }
