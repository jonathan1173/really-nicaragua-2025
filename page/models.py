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


class MunicipalityContent(models.Model):
    CATEGORY_CHOICES = [
        ('historia', 'Historia'),
        ('gastronomia', 'Gastronomía'),
        ('turismo', 'Turismo'), 
    ]

    municipality = models.ForeignKey('Municipality', on_delete=models.CASCADE, related_name='contents')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    content = models.TextField(help_text="Contenido en formato HTML")

    class Meta:
        unique_together = ('municipality', 'category') 

    def __str__(self):
        return f"{self.municipality.name} - {self.category}"
