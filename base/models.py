from django.db import models
from django.utils import timezone
# Create your models here.
import random  
import string 


class Merchant(models.Model):
    merchantId = models.TextField()
    secret = models.TextField()
    msisdn = models.TextField()
    name = models.TextField()
    phone = models.TextField()
    balance = models.IntegerField(default=0)

class Account(models.Model):
    name = models.TextField()
    phone = models.TextField()
    balance = models.IntegerField(default=0)
    pin = models.TextField()
    otp = models.TextField()


class Transaction(models.Model):
    amount = models.IntegerField()
    serviceType = models.TextField()
    orderId = models.TextField()
    redirectUrl = models.TextField()
    iat = models.IntegerField()
    exp = models.IntegerField()
    lang = models.TextField()
    operation_id = models.CharField(max_length=100, null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    def generate_operation_id(self):
        length = 50  
        letters = string.ascii_lowercase + string.ascii_uppercase + "0123456789"
        result = ''.join((random.choice(letters)) for x in range(length))
        result += timezone.now().strftime(r"%Y%m%d%H%M%S")
        self.operation_id = result 
        self.save()









