from . import views
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   path('fruits/',views.Fruits_list,name='fruits_list') ,
   path('fruits/<int:id>',views.Fruits_detail,name="fruit_detail")
]


urlpatterns=format_suffix_patterns(urlpatterns) 
# format_suffix_patterns Returns a URL pattern list which includes format suffix patterns appended to each of the URL patterns provided