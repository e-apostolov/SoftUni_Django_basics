from django import forms

from FurryFunnies.mixins import ReadOnlyMixin
from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at', 'author']
        labels = {
            'image_url': 'Post Image URL:',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Put an attractive and unique title...',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Share some interesting facts about your adorable pets...'
            }),
        }


class PostCreateForm(PostBaseForm):
    pass

class PostEditForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        help_texts = {
            'image_url': "",
        }

class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    read_only_fields = ['title', 'image_url', 'content']
