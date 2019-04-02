from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import JobSerializers, BidSerializer
from .models import Job, Bid

@api_view(['GET'])
def job_list(request):
    ordering_field = request.query_params.get('ordering_field', 'created')
    ordering_direction = request.query_params.get('ordering_direction', 'ASC')
    if (ordering_direction == 'DESC'):
        ordering_field = '-' + ordering_field

    jobs = Job.objects.order_by(ordering_field)
    response = JobSerializers(jobs, many=True)
    return Response(response.data)

@api_view(['GET'])
def bid_list(request):
    ordering_field = request.query_params.get('ordering_field', 'price')
    ordering_direction = request.query_params.get('ordering_direction', 'ASC')
    if (ordering_direction == 'DESC'):
        ordering_field = '-' + ordering_field

    bids = Bid.objects.order_by(ordering_field)
    response = BidSerializer(bids, many=True)
    return Response(response.data)