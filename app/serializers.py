from rest_framework import serializers
from . import models

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'manager',
      'id',
      'name',
      'email',
      'phone',
      'info',
      'gender',
      'image',
      'date_added'
    )
    model = models.Contact