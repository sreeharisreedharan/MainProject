from django.db import models
from Admin.models import *
from Staff.models import*

# Create your models here.
class tbl_notification(models.Model):
    notification_content=models.CharField(max_length=200)
    notification_date=models.DateField(auto_now_add=True)
    notification_status=models.IntegerField(default=0)
    student=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
