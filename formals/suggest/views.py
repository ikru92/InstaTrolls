import json

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, mixins
from suggest import serializers
from suggest.models import Post, Comment, Lover,myUser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ParseError

class ADViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class ADUViewSet(ADViewSet, mixins.UpdateModelMixin):
    pass


class ADURViewSet(ADUViewSet, mixins.RetrieveModelMixin):
    pass

class FeedsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.FeedsListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class PostsViewSet(ADURViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if not request.data['post']:
            request.data['post'] = instance.post
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def addLove(self, post_id):
        instance = Post.objects.get(id=post_id)
        instance.love += 1
        instance.save()

    def addComment(self, post_id):
        instance = Post.objects.get(id=post_id)
        instance.total_comment += 1
        instance.save()

    

class CommentsViewSet(ADUViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentsListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        new_comment = json.loads(request.data['new_comment'])
        if request.data.get('new_image') or new_comment['comment']:
            if request.data.get('new_image'): 
                new_comment['commentImg'] = request.data['new_image']
            post_id = new_comment['post']
            serializer = self.get_serializer(data= new_comment)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            PostsViewSet().addComment(post_id=post_id)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data)
        else :
            raise ParseError('Some error occurred')

    

class LoveViewSet(ADViewSet):
    queryset = Lover.objects.all()
    serializer_class = serializers.LoverSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        post_id = request.data['love_post']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        PostsViewSet().addLove(post_id=post_id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data)


class CommentList(viewsets.ModelViewSet):
    serializer_class = serializers.CommentsListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id)
    

class Auth(APIView):
    def post(self,request):
        data = json.loads(request.body)
        email=data.get('email') if data.get('email') else ''
        password=data.get('password') if data.get('password') else ''
        user=authenticate(email=email,password=password)
        if user is not None:
            token = Token.objects.get(user=user)
            login(request, user)
            return Response(token.key)
        else:
            return Response("")   

class SignOut(APIView):
    def get(self,request):
        logout(request)
        return Response(True)

