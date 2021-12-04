from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import CheckList, CheckListItem
from core.permissions import IsOwner
from core.serializers import ChecklistSerializer,ChecklisItemtSerializer
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    )
# Create your views here.

# class ChecklistsAPIView(APIView):
#     serializer_class=ChecklistSerializer
#     permission_classes=(IsAuthenticated,IsOwner)
#     def get(self,request,*args,**kwargs):
#         data=CheckList.objects.filter(user=request.user)
#         serialize=self.serializer_class(data,many=True)
#         return Response(serialize.data)
    
#     def post(self,request,*args,**kwargs):
#         serializer=self.serializer_class(data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ChecklistsAPIView(ListCreateAPIView):
    serializer_class=ChecklistSerializer
    permission_classes=(IsAuthenticated,IsOwner)
    
    def get_queryset(self):
        queryset=CheckList.objects.filter(user=self.request.user)
        return queryset

# class ChecklistAPIView(APIView):
#     serializer_class=ChecklistSerializer
#     permission_classes=(IsAuthenticated,IsOwner)

#     def check_checklist(self,id):
#         try:
#             obj=CheckList.objects.get(pk=id)
#             self.check_object_permissions(self.request,obj)
#             return obj
#         except CheckList.DoesNotExist:
#             raise Http404


#     def get(self,request,id,format=None):
#         data=self.check_checklist(id)
#         serializer=self.serializer_class(data)
#         return Response(serializer.data,status=status.HTTP_200_OK)
        
#     def put(self,request,id,format=None):
#         data=self.check_checklist(id)
#         serializer=self.serializer_class(data,data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         data=self.check_checklist(id)
#         data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ChecklistAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=ChecklistSerializer
    permission_classes=(IsAuthenticated,IsOwner)

    def get_queryset(self):
        queryset=CheckList.objects.filter(user=self.request.user)
        return queryset

# class ChecklistItemCreateAPIView(APIView):
#     serializer_class=ChecklisItemtSerializer
#     permission_classes=(IsAuthenticated,IsOwner)

#     # def get(self,request,*args,**kwargs):
#     #     data=CheckListItem.objects.all()
#     #     serialize=self.serializer_class(data,many=True)
#     #     return Response(serialize.data)

#     def post(self,request,*args,**kwargs):
#         serializer=self.serializer_class(data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ChecklistItemCreateAPIView(CreateAPIView):
    serializer_class=ChecklisItemtSerializer
    permission_classes=(IsAuthenticated,IsOwner)


# class ChecklistItemAPIView(APIView):
#     permission_classes=(IsAuthenticated,IsOwner)
#     serializer_class=ChecklisItemtSerializer
#     def check_checklist(self,id):
#         try:
#             obj=CheckList.objects.get(pk=id)
#             self.check_object_permissions(self.request,obj)
#             return obj
#         except CheckListItem.DoesNotExist:
#             raise Http404

#     def get(self,request,id,format=None):
#         checklist_item=self.check_checklist(id)
#         serializer=self.serializer_class(checklist_item)
#         return Response(serializer.data,status=status.HTTP_200_OK)
        
#     def put(self,request,id,format=None):
#         checklist_item=self.check_checklist(id)
#         serializer=self.serializer_class(checklist_item,data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         checklist_item=self.check_checklist(id)
#         checklist_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ChecklistItemAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,IsOwner)
    serializer_class=ChecklisItemtSerializer
    
    def get_queryset(self):
        queryset=CheckListItem.objects.filter(user=self.request.user)
        return queryset

    