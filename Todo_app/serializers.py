from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id','Title','Description','Time_stamp','Due_date','status','tags')

    def create(self, validated_data):
        tags = validated_data.pop('tags').split(',')
        unique_tags = set([tag.strip() for tag in tags])
        task = ToDo.objects.create(**validated_data)
        task.tags = ','.join(unique_tags)
        task.save()
        return task
        