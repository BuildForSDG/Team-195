from rest_framework import serializers
from .models import Course, Chapter


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'description',
                  'created', 'created_by', 'price']


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('chapter_name', 'content')