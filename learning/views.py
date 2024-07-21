from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from core.model.base_response import BaseResponse

from rest_framework.parsers import MultiPartParser, FormParser


class CreatePostView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)


    def post(self, request, format=None):
        response = BaseResponse()
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                json_response = response.create_success_response(serializer.data)
                return Response(json_response, status=status.HTTP_201_CREATED)
            json_response = response.create_failure_response(serializer.errors)
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ListPostsView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

    def get(self, request, format=None):
        response = BaseResponse()
        try:
            posts = Post.objects.all().order_by('-created_at')
            serializer = self.get_serializer(posts, many=True)
            json_response = response.create_success_response(serializer.data)
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
