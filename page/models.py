from django.db import models
from django.utils.text import slugify

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

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        unique_together = ('name', 'department')
        ordering = ['department__name', 'name']

class Category(models.Model):
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
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']

class CategoryPage(models.Model):
    """
    Representa la página de una categoría específica dentro de un municipio.
    Contiene el contenido introductorio o "padre".
    """
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name='category_pages', verbose_name="Municipio")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='municipality_pages', verbose_name="Categoría")
    introduction = models.TextField("Contenido Introductorio", help_text="Contenido principal para la página de esta categoría en el municipio.", blank=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)

    class Meta:
        verbose_name = "Página de Categoría"
        verbose_name_plural = "Páginas de Categoría"
        unique_together = ('municipality', 'category')
        ordering = ['municipality__name', 'category__name']

    def __str__(self):
        return f"Página de {self.category.name} en {self.municipality.name}"

class ContentItem(models.Model):
    """
    Representa un "ítem" de contenido individual (artículo, lugar, etc.)
    que pertenece a una página de categoría.
    """
    page = models.ForeignKey(CategoryPage, on_delete=models.CASCADE, related_name='items', verbose_name="Página de Categoría")
    title = models.CharField("Título", max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True, help_text="Se genera automáticamente para la URL.")
    summary = models.TextField("Resumen", help_text="Texto corto para mostrar en las listas.")
    image = models.ImageField("Imagen Principal", upload_to='static/img', blank=True, null=True)
    body = models.TextField("Cuerpo del Contenido", help_text="El contenido detallado para la página del ítem.")
    published = models.BooleanField("Publicado", default=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def municipality(self):
        return self.page.municipality

    @property
    def category(self):
        return self.page.category

    class Meta:
        verbose_name = "Ítem de Contenido"
        verbose_name_plural = "Ítems de Contenido"
        ordering = ['-created_at']
