from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Complainant(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(default="Amritsar",max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ("W","Water"),
    ("L","Light"),
    ("S","Sewer"),
    ("R","Road")
)

class Complaint(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    describe = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)

    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (
    ("Registered","Registered"),
    ("Work Under Progress","Work Under Progress"),
    ("Completed","Completed"),
    ("False complaint","False complaint")
)

class Progress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    complainant = models.ForeignKey(Complainant,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    describe = models.TextField()
    category = models.CharField(max_length=2)
    complaint_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default="Registered")