from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    votes_toal = models.IntegerField(default=1)
    body = models.TextField(max_length=40000)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime("%d %b, %Y")

    def short_desc(self):
        return self.body[0:200]
