from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100, blank=False)
    url = models.TextField(blank=True)
    body = models.TextField()

    pub_date = models.DateTimeField(default=datetime.datetime.now)
    votes_total = models.IntegerField(default=1)

    product_img = models.ImageField(blank=True, upload_to="images/")
    product_icon = models.ImageField(blank=True, upload_to="icons/")

    hunter = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
