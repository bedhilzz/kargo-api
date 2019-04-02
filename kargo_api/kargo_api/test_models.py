from django.test import TestCase
from .models import Job, Bid, Shipper, Transporter
from datetime import datetime, timedelta

class JobTestCase(TestCase):
    def setUp(self):
        shipper = Shipper.objects.create(email='shipper@example.com', password='password', name='test', address='scbd')
        Job.objects.create(shipper_id=shipper, origin='JKT', destination='SBY', description='Kayu Jati', budget=2000000, shipment_date=datetime.now())
        Job.objects.create(shipper_id=shipper, origin='JKT', destination='BDG', description='Lemari Jati', budget=4000000, shipment_date=datetime.now() + timedelta(days=1))
    
    def test_job_created(self):
        jkt_to_sby = Job.objects.get(origin='JKT', destination='SBY')
        jkt_to_bdg = Job.objects.get(origin='JKT', destination='BDG')
        self.assertEqual(jkt_to_sby.description, 'Kayu Jati')
        self.assertEqual(jkt_to_bdg.description, 'Lemari Jati')

    def test_sorted_job(self):
        sorted_jobs = Job.objects.order_by('shipment_date')
        self.assertEqual(sorted_jobs[0].destination, 'SBY')
        self.assertEqual(sorted_jobs[1].destination, 'BDG')

class BidTestCase(TestCase):
    def setUp(self):
        shipper = Shipper.objects.create(email='shipper@example.com', password='password', name='test', address='scbd')
        job = Job.objects.create(shipper_id=shipper, origin='JKT', destination='SBY', description='Kayu Jati', budget=2000000, shipment_date=datetime.now())
        transporter = Transporter.objects.create(email='shipper@example.com', password='password', name='test', rating=5)
        Bid.objects.create(job_id=job, transporter_id=transporter, vehicle='CDD', price=2000000)
        Bid.objects.create(job_id=job, transporter_id=transporter, vehicle='CDE', price=2500000)
    
    def test_job_created(self):
        vehicle_cdd = Bid.objects.get(vehicle='CDD')
        vehicle_cde = Bid.objects.get(vehicle='CDE')
        self.assertEqual(vehicle_cdd.price, 2000000)
        self.assertEqual(vehicle_cde.price, 2500000)

    def test_sorted_job(self):
        sorted_bids = Bid.objects.order_by('price')
        self.assertEqual(sorted_bids[0].vehicle, 'CDD')
        self.assertEqual(sorted_bids[1].vehicle, 'CDE')