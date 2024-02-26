# models.py

from django.db import models

FAQ_TYPE = [
        ('rent_tracking', 'Rent Tracking'),
        ('new_deposit', 'New_Deposit'),
        ('existing_deposit', 'Existing_Deposit'),
        # Add more choices as needed
    ]

class Testimonial(models.Model):
    name = models.CharField(max_length=255, default='Hafeex')
    designation = models.CharField(max_length=255, default='software development')
    image = models.ImageField(upload_to="testimonials/", )
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name



class  Promoter(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Promoters/")


    def __str__(self):
        return  self.name


class Faqs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    faq_type = models.CharField(max_length=128, choices=FAQ_TYPE)

  
    def __str__(self):
        return self.title
    

class Subscribe(models.Model):
     email = models.EmailField(unique=True,primary_key=True)

     def __str__(self):
         return self.email