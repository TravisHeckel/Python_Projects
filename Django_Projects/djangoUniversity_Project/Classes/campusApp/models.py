from django.db import models


# This model creates a model that allows for 3 variables to be placed
class UniversityCampus(models.Model):
    campusName = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    campusID = models.IntegerField(default="", blank=True,null=False)

    # This creates the instances of the object through our models management module
    object = models.Manager()

    # This will create a string variable to represent our object in the list.

    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_course = '{0.campusName}: {0.State}'
        return display_course.format(self)
    # This creates the model we can select when wanting to create new objects.

    class Meta:
        verbose_name_plural = "University Campus"
