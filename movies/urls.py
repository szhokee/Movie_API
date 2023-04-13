from django.shortcuts import render
from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('actors/', ActorViewSet)
router.register('videos/', VideoViewSet)
router.register('movies/', MovieViewSet)


urlpatterns = [
    path('', include(router.urls)),
]