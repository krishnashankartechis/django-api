from rest_framework import serializers

from .models import Post

from django import forms

# class PostForm (forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = (
#             'title','description'
#         )

# serializers are almost same as how we create forms

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description'
        )