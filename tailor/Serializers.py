from rest_framework import serializers
from django.contrib.auth.models import User
from .models import customer,order




class customerSerializer(serializers.ModelSerializer):

    class Meta:
        model = customer
        #fields=['s_name',]
        fields = '__all__'
    
    #def to_representation(self, instance):
        # rep = super().to_representation(instance)
        # rep['measurementsFK'] = measurementSerializer(instance.measurementsFK).data
        # return rep




class orderSerializer(serializers.ModelSerializer):

    class Meta:
        model = order
        #fields=['s_name',]
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['customerFK'] = customerSerializer(instance.customerFK).data
        return rep