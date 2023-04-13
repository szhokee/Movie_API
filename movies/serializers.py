from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.ModelSerializer):
    model = Actor
    fields = ('name', 'age', 'description', 'image')


class VideoSerializer(serializers.ModelSerializer):
    model = Video
    fields = ('title', 'file')


class MovieSerializer(serializers.ModelSerializer):
    model = Movie
    fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = '__all__'
    