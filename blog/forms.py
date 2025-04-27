from django import forms
from blog.models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    photo = forms.ImageField()
    class Meta:
        model = Post
        fields = ('title', 'photo', 'content' )
