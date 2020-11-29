__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField,StringRelatedField,PrimaryKeyRelatedField,Serializer
from rest_framework import serializers
from rests.models import *
from django.contrib.auth import authenticate,logout,login
from rest_framework import exceptions

class student_serializer1(ModelSerializer):
    class Meta:

        model=student
        fields=[
            'student_name'
        ]



class student_serializer(ModelSerializer):

    #student=SerializerMethodField()
    #student_user=StringRelatedField()
    #student_user=PrimaryKeyRelatedField(read_only=True)
    #student_name=student_serializer1()


    class Meta:

        model=student
        fields=[
            'student_name','student_last_name','student_user','student'
        ]

        print('lllllllllllllllllllllllllllllllllllloooooooooooooooooooh')



class Regionserializer(ModelSerializer):
    class Meta:
        model=Region
        fields='__all__'



class Cityserializer(ModelSerializer):
    class Meta:
        model=City
        fields='__all__'





class Stateserializer(ModelSerializer):
    class Meta:
        model=State
        fields='__all__'




class Countryserializer(ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'



class Locationserializer(ModelSerializer):
    class Meta:
        model=Locations
        fields='__all__'



#---------------------------------------------------------------------------------------------

class fees_create(ModelSerializer):
    class Meta:
        model=faire
        fields='__all__'






class user_create1(ModelSerializer):

    class Meta:
        model=name
        fields=['first_name','last_name','phone','address','user']
        print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj6')
    def create(self, validated_data):



        print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj62')

        first_name=validated_data.get('first_name')
        print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj61')
        last_name=validated_data.get('last_name')
        print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj64')
        phone=validated_data.get('phone')
        print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj65')
        address=validated_data.get('address')
        print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj66')
        try:

            p=name.objects.filter(phone=phone)
            print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj6',p)

            return 'Phone no exist'
            print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj68')
        except:

            p1=name.objects.create(**validated_data)
            return p1
            print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj6')




class serializer1(ModelSerializer):
    class Meta:
        model=name
        fields='__all__'


class user_serializer(ModelSerializer):
    profile=serializer1()
    class Meta:
        model=User
        fields=['username','email','password','profile']
    def create(self, validated_data):
        profile_data=validated_data.pop('profile')
        user1=User.objects.create(**validated_data)
        name.objects.create(user=user1,**profile_data)
        return user1








class list_user(ModelSerializer):
    class Meta:
        model=name
        fields=['first_name','last_name','phone','address','user']



class bus_creation(ModelSerializer):
    bus_fees=fees_create(many=True)
    class Meta:
        model=Bus
        fields=['bus_name','bus_no','bus_capacity','bus_status','bus_current_passanger','bus_fees']
    def create(self, validated_data):

        bus_fees=validated_data.pop('bus_fees')


        bus_name=validated_data.get('bus_name')
        bus_no=validated_data.get('bus_no')
        print(bus_no,'jjjjjjjjjjjjjjjjjjjjj89',type(bus_no))
        bus_capacity=validated_data.get('bus_capacity')
        bus_status=validated_data.get('bus_status')
        bus_current_passanger=0
        o=str(bus_no)

        if(len(o)<=4):
            p=Bus.objects.create(**validated_data)
            return p
        else:
            return ('bus no is wrong')









class location_serializer(ModelSerializer):
    Bus_name=SerializerMethodField()
    print(Bus_name,'pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp')
    class Meta:

        model=location
        fields=['place_starting','place_end','place_time_reach','place_time_arrival','Bus_name']


    def get_Bus_name(self,obj):

        print('ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
        return str(obj.Bus_name.bus_name)




    def create(self, validated_data):


        #place_starting=validated_data.pop('bus_fees')


        place_starting=validated_data.get('place_starting')
        place_end=validated_data.get('place_end')
        print(place_end,'jjjjjjjjjjjjjjjjjjjjj89',type(place_end))
        place_time_arrival=validated_data.get('place_time_arrival')
        place_time_reach=validated_data.get('place_time_reach')
        bus_current_passanger=0



        p=location.objects.create(**validated_data)
        return p






class login_client(Serializer):
    username=serializers.CharField(max_length=10)
    password=serializers.CharField(max_length=10)
    def validate(self, data):
        username=data.get("username")
        password=data.get("password")
        if username and password:
            user=authenticate(username=username,password=password)
            if user:

                if user.is_active():

                    data['user']=user
                else:
                       msg="Account is deactivated"
                       raise exceptions.ValidationError(msg)

            else:

                msg="Must provide username and password"
                raise exceptions.ValidationError(msg)

        else:
            msg="Must provide username and password"
            raise exceptions.ValidationError(msg)
        return data






class booking_serializer(ModelSerializer):
    class Meta:
        model=booking1
        fields=['place_end','place_starting','passanger_name','date']
