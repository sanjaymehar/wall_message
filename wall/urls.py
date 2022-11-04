
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from task.views import *
router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('createuser/',RegisterView.as_view()),
    path('all/',Wallall.as_view()),
    path('craetewall/',Wallcreate.as_view()),
    path('updateewall/<int:pk>',WallUpdate.as_view()),
    path('deleteewall/<int:pk>',WallDelete.as_view()),
    path('getdata/<int:pk>',WallGetData.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

