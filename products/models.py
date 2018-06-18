from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required

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

    @login_required
    def upvote(self):
        self.votes_total += 1
        return self.votes_total

    @login_required
    def downvote(self):
        self.votes_total -= 1
        self.save()
        return self.votes_total
