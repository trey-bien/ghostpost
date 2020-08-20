from django import forms
from ghost.models import Post

class CreatePostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    boast_or_roast = forms.ChoiceField(choices=(
        (True, "Boast"),
        (False, "Roast")
    ))
