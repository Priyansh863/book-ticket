from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class student(models.Model):
    print('lllllllllllllllllllllllllllllllllllloooooooooooooooooooh9')
    student_name=models.CharField(max_length=10,null=True,blank=True)
    print('lllllllllllllllllllllllllllllllllllloooooooooooooooooooh9')
    student_last_name=models.CharField(max_length=10,null=True,blank=True)
    print('lllllllllllllllllllllllllllllllllllloooooooooooooooooooh9')
    student_email=models.EmailField()
    student_user=models.OneToOneField(User,on_delete=models.CASCADE)
    print('lllllllllllllllllllllllllllllllllllloooooooooooooooooooh9')

    '''@property
    def status_message(self):
        if self.active:
            print('hiiii1')
            return 'client active'

        else:
            print('hiiii2')
            return 'customer not active'
    def student(self):

        return self.student_last_name'''




class Region(models.Model):
    name=models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.name

class Country(models.Model):
    name_country=models.CharField(max_length=10,null=True,blank=True)
    region=models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):

        return self.name_country
class State(models.Model):
    name_state=models.CharField(max_length=10,null=True,blank=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):

        return self.name_state




class City(models.Model):
    name_city=models.CharField(max_length=10,null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):

        return self.name_city



class Locations(models.Model):
    name_address=models.CharField(max_length=10,null=True,blank=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):

        return self.name_address



















# =========================================================================================================================================================================.

class name(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
class faire(models.Model):
    faire_price=models.IntegerField()
class Bus(models.Model):
    bus_name=models.CharField(max_length=100,null=True,blank=True)
    bus_no=models.IntegerField(null=True,blank=True,unique=True)
    bus_fees=models.ForeignKey(faire,null=True,blank=True,on_delete=models.CASCADE)
    bus_capacity=models.IntegerField(null=True,blank=True)
    bus_status=models.CharField(max_length=100,null=True,blank=True)
    bus_current_passanger=models.CharField(max_length=100,null=True,blank=True)
    bus_img=models.ImageField(upload_to='media/img',null=True,blank=True)
    def __str__(self):
        return self.bus_name




class booking1(models.Model):
    Bus_name=models.ForeignKey(Bus,on_delete=models.CASCADE,null=True,blank=True)
    booking_no=models.CharField(max_length=100,null=True,blank=True)
    user_name=models.ForeignKey(name,on_delete=models.CASCADE,null=True,blank=True)
    passanger_name=models.CharField(max_length=100,null=True,blank=True)
    place_starting=models.CharField(max_length=100,null=True,blank=True)
    place_end=models.CharField(max_length=100,null=True,blank=True)
    bus_no=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True,auto_now=True)
class location(models.Model):
    place_starting=models.CharField(max_length=100,null=True,blank=True,unique=True)
    place_end=models.CharField(max_length=100,null=True,blank=True,unique=True)
    place_time_reach=models.TimeField(null=True,blank=True)
    place_time_arrival=models.TimeField(null=True,blank=True)
    Bus_name=models.OneToOneField(Bus,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.place_starting


class ticket(models.Model):

    price=models.CharField(max_length=20,null=True,blank=True)
    ticket_no=models.IntegerField(null=True,blank=True)
    location=models.OneToOneField(location,on_delete=models.CASCADE,null=True,blank=True)

class staff(models.Model):
    driver_name=models.CharField(max_length=100,null=True,blank=True)
    driver_no=models.CharField(max_length=100,null=True,blank=True)
    driver_email=models.EmailField(null=True,blank=True)
    driver_image=models.ImageField(upload_to='media/img',null=True,blank=True)


    conductor_name=models.CharField(max_length=100,null=True,blank=True)
    conductor_no=models.CharField(max_length=100,null=True,blank=True)
    conductor_email=models.EmailField(null=True,blank=True)
    conductor_image=models.ImageField(upload_to='media/img',null=True,blank=True)
    Bus_no=models.OneToOneField(Bus,on_delete=models.CASCADE,null=True,blank=True)












