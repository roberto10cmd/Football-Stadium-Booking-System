from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField( User,on_delete=models.CASCADE, null=True,blank=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255) 
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.firstname} (ID: {self.id})"

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()    


    def __str__(self):
        return f"{self.name} (ID: {self.id})"

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

class Feedback(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.firstname} for {self.stadium.name} (ID: {self.id})"

class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    equipment = models.ManyToManyField(Equipment, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.firstname}"
