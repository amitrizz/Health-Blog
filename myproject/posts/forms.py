from django import forms
from . import models

class Createpost(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=['title','body','slug','banner']
 
class CreateComment(forms.ModelForm): 
    class Meta:
        model=models.Comments
        fields=['comment']