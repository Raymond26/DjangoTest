from django.db import models
from members.models import Member
from galleries.models import ImageModel
import datetime
from datetime import date

class Report(models.Model):

    date = models.DateField(auto_add_now=True)

    total_number_of_members = models.IntegerField(default=0)
    new_members_today = models.IntegerField(default=0)

    total_number_of_photos = models.IntegerField(default=0)
    new_photos_today = models.IntegerField(default=0)



    def __init__(self):

        today = date.today()

        self.total_number_of_members = Member.objects.count()
        self.new_members_today = Member.objects.get(register_date=today).count()

        self.total_number_of_photos = ImageModel.objects.count()
        # self.new_photos_today = ImageModel.objects.get(upload_date=today)
        # figure out python queries better

