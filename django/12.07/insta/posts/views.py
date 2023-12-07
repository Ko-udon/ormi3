# Basic Django Modules
from django.shortcuts import get_object_or_404

# Rest Framework Modules
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Models
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # SNS는 인증된 사용자만 볼 수 있도록 설정, 이미 설정이 되어 있음에도 유지보수, 가독성을 위해 추가
    permission_classes = [IsAuthenticated] 


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer): # author를 현재 로그인한 유저로 설정
        serializer.save(author=self.request.user)


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])


class LikeView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id): # 좋아요 생성
        post = get_object_or_404(Post, id=post_id) # 게시물이 존재하지 않으면 404 에러
        like, is_created = post.like_set.get_or_create(author=request.user) # 좋아요를 검색한 후 좋아요가 없으면 생성(like 생성된 객체, is_created가 생성 여부 판단) 

        # is_created == True : 좋아요가 클릭이 안되어 있어서 새로 생성했다.
        # is_created == False : 좋아요가 클릭이 되어서 생성하지 못했다.

        if not is_created: # 좋아요가 이미 클릭되어 있어서 좋아요가 생성되지 않았다면 409 에러
            return Response(status=409)
        
        return Response(status=201) # 좋아요가 생성되었으면 201 응답

    def delete(self, request, post_id): # 좋아요 삭제
        post = get_object_or_404(Post, id=post_id) # 게시물이 존재하지 않으면 404 에러
        like = get_object_or_404(post.like_set, author=request.user) # 좋아요가 존재하지 않으면 404 에러
        like.delete() # 좋아요 삭제
        return Response(status=204) # 좋아요가 삭제되었으면 204 응답