from urllib import response
from django.http import JsonResponse
from django.shortcuts import render


#third party imports
from rest_framework.response import Response
from rest_framework.views import APIView



from .serializers import PostSerializer
from .models import Post

class TestView(APIView):
    def get(self,request, *args, **kwargs):
        # data ={
        # "name":"john",
        # 'age':23
        #         }

        # there are two options to do this, either set the values directly or put a serializer to display the data


        # again we can get all posts in a single time or we can get the first one by one.
        qs = Post.objects.all()

        post = qs.first()
        serializer = PostSerializer(post)
        # serializer = PostSerializer(qs,many=True)  



        return Response(serializer.data)

        

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
         
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)

        return Response(serializer.errors)
        



# Create your views here.
# def test_view(request):
    # data ={
    #     "name":"john",
    #     'age':23
    # }

    # data = [1,2,3,4]
    # return JsonResponse(data,safe=False)
    # return JsonResponse(data)