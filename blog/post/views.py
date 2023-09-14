from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from post.serializers import CommentSerializer, PostDetailSerializer, PostListSerializer
from post.models import Post
from django.utils import timezone 

# Create your views here.

@api_view(['GET'])
def PostListView(request):
    if request.method == 'GET':
        Posts = Post.objects.all().order_by('-published_on')
        serializer = PostListSerializer(Posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def PostDetailView(request, pk):
    if request.method == 'GET':
        Posts = Post.objects.get(id=pk)
        serializer = PostDetailSerializer(Posts, many=False)
        return Response(serializer.data)

@api_view(['PUT'])
def update_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PostDetailSerializer(post, data=request.data)

    if serializer.is_valid():
        serializer.save()  
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def comment_list(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        serializer = PostDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['published_on'] = timezone.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'Not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        post.delete()
        return Response({'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
