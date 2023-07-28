from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

#combine the logic for a set of related views in a single class, called a ViewSet 
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
