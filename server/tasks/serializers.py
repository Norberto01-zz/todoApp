from rest_framework import serializers
from tasks.models import Tasking
from django.contrib.auth.models import User

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Tasking
        fields = ('id', 'taskName', 'done', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(queryset=Tasking.objects.all(), view_name='todo-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'tasks')