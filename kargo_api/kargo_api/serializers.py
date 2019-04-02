from rest_framework import serializers
from .models import Job, Bid

class JobSerializers(serializers.ModelSerializer):
    def create(self, validated_data):
        j = Job()
        j.shipper_id = validated_data.get('shipper_id')
        j.origin = validated_data.get('origin')
        j.destination = validated_data.get('destination')
        j.description = validated_data.get('description')
        j.budget = validated_data.get('budget')
        j.shipment_date = validated_data.get('shipment_date')
        return j

    class Meta:
        model = Job
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        b = Bid()
        j.job_id = validated_data.get('job_id')
        j.transporter_id = validated_data.get('transporter_id')
        j.vehicle = validated_data.get('vehicle')
        j.price = validated_data.get('price')
        return b

    class Meta:
        model = Bid
        fields = '__all__'