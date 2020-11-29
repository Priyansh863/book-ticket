from django.shortcuts import render
from django.contrib.auth import authenticate,logout,login
# Create your views here.
from rest_framework.decorators import action
from rest_framework.authtoken .models import Token
from django.contrib.auth.models import User
from rests.models import student
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly,IsAuthenticated
from rests.serializers import *
from rest_framework.response import Response
from rests.permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rests.serializers import *
from rest_framework.authentication import TokenAuthentication
class student_view(ListAPIView):

    queryset = student.objects.all()

    serializer_class = student_serializer
    filter_backends = [ SearchFilter]
    search_fields=["student_name","student_last_name","student_email"]



class student_view_create(CreateAPIView):

    queryset = student.objects.all()

    serializer_class = student_serializer
    permission_classes = [IsOwnerOrReadOnly]



class student_delete_create(DestroyAPIView):

    queryset = student.objects.all()

    serializer_class = student_serializer


class student_retriev_create(RetrieveAPIView):

    queryset = student.objects.all()

    serializer_class = student_serializer



class student_updateview_create(UpdateAPIView):

    queryset = student.objects.all()

    serializer_class = student_serializer
    permission_classes = [IsOwnerOrReadOnly]




class createviewset(ViewSet):
    http_method_names = ['post']
    def create(self,requeat):

        serializer=student_serializer(data=requeat.data)
        if serializer.is_valid():
            serializer.save()
            return Response("ok")
        else:
            return Response(serializer.errors)





class listviewset(ViewSet):
    http_method_names = ['get']
    def list(self,request):
        queryset=student.objects.all()
        serializer=student_serializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = student.objects.filter(id=pk)
        #student = get_object_or_404(queryset, pk=pk)
        serializer = student_serializer(queryset,many=True)
        return Response(serializer.data)




class destroyview(ViewSet):
     http_method_names = ['delete','put','get']
     print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
     def destroy(self,request,pk=None):
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk1')
        queryset = student.objects.filter(id=pk).delete()
        #student = get_object_or_404(queryset, pk=pk)
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk2')

        #object.delete()
        return Response('ok')

     def update(self, request, pk=None):
         user=student.objects.get(id=pk)
         p=request.data
         print(p,'hi')
         user.student_name=p['student_name']
         print(user.student_name,'iiiiiiiiiiiiiiiiiiiiii')
         user.student_last_name=p['student_last_name']
         user.student_email=p['student_email']


         u=p['student_user']
         print(u,'jjjjjjjj1jjjjjjjjjjjjjjj')
         c=User.objects.get(id=u)
         print(c,'jjjjjjjjjjjjjjjjjjjjjjj')
         user.student_user=c


         user.save()
         serializer=student_serializer(user)
         return Response(serializer.data)
     @action(detail=True)
     def deactivate(self,request,pk=None):
         user=student.objects.get(id=pk)
         user.active=False
         serializer=student_serializer(user)
         return Response(serializer.data)


     @action(detail=False)
     def deactivate_all(self,request):
         user=student.objects.all()


         user.update(active=False)
         serializer=student_serializer(user)
         return Response(serializer.data)
     @action(detail=True)
     def activate(self,request,pk=None):
         user=student.objects.get(id=pk)
         user.active=True
         serializer=student_serializer(user)
         return Response(serializer.data)



#===================================================================================================================================================================================


class region(ViewSet):
    http_method_names = ['post','delete','put','patch','get']
    def create(self,requeat):

        serializer=Regionserializer(data=requeat.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def destroy(self,request,pk=None):
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk1')
        queryset = Region.objects.filter(id=pk).delete()
        #student = get_object_or_404(queryset, pk=pk)
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk2')
        return Response('ok delete')


    def list(self,request):
        queryset=Region.objects.all()
        serializer=Regionserializer(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Region.objects.filter(id=pk)
        #student = get_object_or_404(queryset, pk=pk)
        serializer = Regionserializer(queryset,many=True)
        return Response(serializer.data)







class user_create(ViewSet):
    http_method_names = ['post','get']
    def create(self,request):
        serializer=user_create1(data=request.data)
        print('1')
        if serializer.is_valid():
            print('12')
            serializer.save()
            print('12')

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def list(self,request):
        queryset=name.objects.all()
        serializer=list_user(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = name.objects.filter(id=pk)
        #student = get_object_or_404(queryset, pk=pk)
        serializer = list_user(queryset,many=True)
        return Response(serializer.data)


    def destroy(self,request,pk=None):
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk1')
        queryset = name.objects.filter(id=pk).delete()
        #student = get_object_or_404(queryset, pk=pk)
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk2')
        return Response('ok delete')









class bus_create(ViewSet):
    http_method_names = ['post','get']
    def create(self,request):
        serializer=bus_creation(data=request.data)
        print('1')
        if serializer.is_valid():
            print('12')
            serializer.save()
            print('12345')

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def list(self,request):
        queryset=Bus.objects.all()
        serializer=bus_creation(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Bus.objects.filter(id=pk)
        #student = get_object_or_404(queryset, pk=pk)
        serializer = bus_creation(queryset,many=True)
        return Response(serializer.data)


    def destroy(self,request,pk=None):
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk1')
        queryset = Bus.objects.filter(id=pk).delete()
        #student = get_object_or_404(queryset, pk=pk)
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk2')
        return Response('ok delete')






class create_user(ViewSet):
    def create(self,request):
        serializer=user_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)









class create_location(ViewSet):
    def create(self,request):
        serializer=location_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class login_view(ViewSet):
    http_method_names = ['post']

    def post(self,request):
        serializers=login_client(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user=serializers.data['user']
            login(request,user)
            token,created=Token.objects.get_or_create(user=user)
            return Response({"token":token.key},status=200)



class logout_viewset(ViewSet):
    http_method_names = ['post']
    authentication_classes =[TokenAuthentication]
    def post(self,request):
        Token.delete(user=request.user)
        logout(request)
        return Response('ok')






class booking_view(ViewSet):
    def create(self,request):
        serializers=booking_serializer(data=request.data)
        if serializers.is_valid():
            place_start=serializers.data['place_starting']
            place_end=serializers.data['place_end']
            date=serializers.data['date']
            passanger_name=serializers.data['passanger_name']
            bus_name=location.objects.get(place_start=place_start)
            print(bus_name)


            user_name=request.user










