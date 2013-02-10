from rest_framework import serializers
from models import Member

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('pk', 'username', 'email', 'location', 'date_of_birth')