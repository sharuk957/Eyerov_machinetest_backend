from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Imagedata
from .serializer import ImageSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def registration(request):
    if request.method == 'POST':
        data = request.data
        coords=''
        if data.get('shape') == "rect":
            coords = data.get('x1')+','+data.get('y1')+','+data.get('x2')+','+data.get('y2')
        else:
            coords = data.get('x1')+','+data.get('y1')+','+data.get('radius')

        Imagedata.objects.create(title=data.get('title'),coords=coords,shape=data.get('shape'))
        return Response({'message':"suucess"})
    data = Imagedata.objects.all()
    Serializer = ImageSerializer(data,many=True)
    return Response(Serializer.data)