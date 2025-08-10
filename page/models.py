from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Department(models.Model):
    name = models.CharField("Nombre", max_length=100, unique=True)
    description = models.TextField("Descripción", blank=True, null=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True, help_text="Versión del nombre para URLs amigables.")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('maps-department', kwargs={'department_slug': self.slug})

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['name']

class Municipality(models.Model):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción", blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='municipalities', verbose_name="Departamento")
    slug = models.SlugField(max_length=120, unique=True, blank=True, help_text="Versión del nombre para URLs amigables. Se genera automáticamente.")

    def __str__(self):
        return f"{self.name}, {self.department.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.department.name}-{self.name}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('municipality-detail', kwargs={'municipality_slug': self.slug})

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        unique_together = ('name', 'department')
        ordering = ['department__name', 'name']

class MunicipalityImage(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField("Imagen Municipio", upload_to='static/img/municipalities/', blank=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.id}. {self.title} - {self.municipality.name}, {self.municipality.department.name}"

class Category(models.Model):
    name = models.CharField("Nombre", max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True, help_text="Versión del nombre para URLs amigables.")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']

class CategoryPage(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name='category_pages', verbose_name="Municipio")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='municipality_pages', verbose_name="Categoría")
    introduction = models.TextField("Contenido Introductorio", help_text="Contenido principal para la página de esta categoría en el municipio.", blank=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)

    def get_absolute_url(self):
        return reverse('category-page', kwargs={
            'municipality_slug': self.municipality.slug,
            'category_slug': self.category.slug
        })

    class Meta:
        verbose_name = "Página de Categoría"
        verbose_name_plural = "Páginas de Categoría"
        unique_together = ('municipality', 'category')
        ordering = ['municipality__name', 'category__name']

    def __str__(self):
        return f"Página de {self.category.name} en {self.municipality.name}"

class CategoryItem(models.Model):
    name = models.CharField("Nombre", max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True, help_text="Versión del nombre para URLs amigables.")
    description = models.TextField("Descripción", blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Categoría del Ítem"
        verbose_name_plural = "Categorías de Ítems"
        ordering = ['name']

class ContentItem(models.Model):
    page = models.ForeignKey(CategoryPage, on_delete=models.CASCADE, related_name='items', verbose_name="Página de Categoría")
    title = models.CharField("Título", max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True, help_text="Se genera automáticamente para la URL.")
    summary = models.TextField("Resumen", help_text="Texto corto para mostrar en las listas.")
    image = models.ImageField("Imagen Principal", upload_to='static/img/', blank=True, null=True)
    body = models.TextField("Cuerpo del Contenido", help_text="El contenido detallado para la página del ítem.")
    published = models.BooleanField("Publicado", default=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)

    location = models.CharField("Ubicación", max_length=255, blank=True, null=True)
    category = models.ForeignKey(CategoryItem, on_delete=models.CASCADE, related_name='content_items', verbose_name="Categoría del Ítem")
    schedule = models.CharField("Horario", max_length=100, blank=True, null=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('content-item-detail', kwargs={
            'municipality_slug': self.page.municipality.slug,
            'category_slug': self.page.category.slug,
            'item_slug': self.slug
        })
        
    class Meta:
        verbose_name = "Ítem de Contenido"
        verbose_name_plural = "Ítems de Contenido"
        ordering = ['-created_at']
        
class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField(blank=True)
    date = models.DateField(blank=True)
    image = models.ImageField("Imagen Principal", upload_to='static/img/events/', blank=True)
    municipality = models.ForeignKey(Department, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Evento de {self.title} en {self.municipality.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'event_slug': self.slug})
