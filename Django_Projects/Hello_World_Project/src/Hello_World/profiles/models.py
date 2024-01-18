from django.db import models

TYPE_CHOICES = {
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Dr.', 'Dr.'),
    ('Ms.', 'Ms.'),
}


# Create your models here.
class Profiles(models.Model):
    text = models.CharField(max_length=60, default="", choices=TYPE_CHOICES)
    firstname = models.CharField(max_length=60, default="", blank=True, null=False)
    lastname = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.CharField(max_length=60, default="", blank=True)
    username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.firstname
