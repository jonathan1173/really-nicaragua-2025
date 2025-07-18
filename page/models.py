from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='municipalities')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name='contents')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='contents')
    content = models.TextField(help_text="Contenido en formato HTML")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['municipality', 'category'], name='unique_municipality_category')
        ]

    def __str__(self):
        return f"{self.municipality.name} - {self.category.name}"
