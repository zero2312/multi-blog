from django import forms
from blog.models import Post
from ckeditor.widgets import CKEditorWidget
from .models import Comment

class PostForm(forms.ModelForm):
    content = forms.CharField(
        label='Содержимое',
        widget=CKEditorWidget()
    )
    photo = forms.ImageField(label='Фото')

    class Meta:
        model = Post
        fields = ('title', 'photo', 'content')
        labels = {
            'title': 'Заголовок',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок'}),
        }

from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # ЭТО ГЛАВНОЕ
            'rows': 3,
            'placeholder': 'Оставьте комментарий...',
            'required': True
        })
    )

    class Meta:
        model = Comment
        fields = ['content']