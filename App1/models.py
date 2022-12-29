from django.db import models

# Create your models here.
class Contact(models.Model): # we are creating a table of name contact
    name =models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone =models.CharField(max_length=122)
    desc = models.TextField(null=True , blank=True)
    date = models.DateField()

    #to change how models are viewed in the admin page
    def __str__(self):
        return self.name