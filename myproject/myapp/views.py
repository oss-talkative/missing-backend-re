from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import MChild
from .serializers import MChileSerializer

# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# Create your views here.

def index(req):
    return render(req,'index.html')

# @method_decorator(csrf_exempt,name='dispatch')
@api_view(['POST'])
def addMissingChild(request):
        try:
            print("-----------", request.data)
            serializer=MChileSerializer(data=request.data)
            print("serializer:", serializer)
        except Exception as e:
            print('expection::',e)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def allFoundChild(request):
        mchild = MChild.objects.all()
        serializer=MChileSerializer(mchild, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['Get', 'Post'])
def FoundChild(request):
    if(request.method == 'POST'):
        serializer=MChileSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        mchild = MChild.objects.all()
        serializer=MChileSerializer(mchild, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def nameFoundChild(request):
    if request.method == 'POST':
        # print("----------------", request.data)
        mchild=MChild.objects.filter(name=request.data['name']).all()
        serializer=MChileSerializer(mchild, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    mchild = MChild.objects.filter().all()
    serializer=MChileSerializer(mchild, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def nameFoundChild(request, name):
#     if request.method == 'GET':
#         mchild=MChild.objects.filter(name=request.data[name]).all()
#         serializer=MChileSerializer(mchild)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
