__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework.routers import DefaultRouter
from rests.views import *
from rests.models import student
from django.urls import path,include
from rests import views
router=DefaultRouter()


router.register(r'createviewset',createviewset,basename='createviewset')
router.register(r'listviewset',listviewset,basename='listviewset')
router.register(r'destroyview',destroyview,basename='destroyview')
router.register(r'region',region,basename='location')
router.register(r'create_user',create_user,basename='create_user')
router.register(r'bus_create',bus_create,basename='bus_create')
router.register(r'create_location',create_location,basename='create_location')
router.register(r'bus_create',bus_create,basename='bus_create')
router.register(r'login_client',login_view,basename='login_client')
router.register(r'log_out',logout_viewset,basename='logout_viewset')



urlpatterns=router.urls




'''urlpatterns = [
    path('student_view/',views.student_view.as_view(),name='student_view'),
    path('student_view_create/',views.student_view_create.as_view(),name='student_view'),
     path('student_retriev_create/<int:pk>/',views.student_retriev_create.as_view(),name='student_retriev_create'),
    path('student_updateview_create/<int:pk>/',views.student_updateview_create.as_view(),name='student_updateview_create'),
    path('student_delete_create/<int:pk>/',views.student_delete_create.as_view(),name='student_delete_create'),


]'''
print('hi')