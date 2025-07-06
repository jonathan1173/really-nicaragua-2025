from django.db import models

class Department(models.Model):
    name = models.CharField(blank=True, null=True)
    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='municipalities')

    def __str__(self):
        return self.name
