from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=40,required=True)
    body = serializers.CharField(required=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=True)
    class Meta:
        model = Comment
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        


