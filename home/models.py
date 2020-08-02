from django.db import models

# Create your models here. It's a kind of table in the database.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    # The function to make the contact person name visible in admin panel
    def __str__(self):
        return self.name