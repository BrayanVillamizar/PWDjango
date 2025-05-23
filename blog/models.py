from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class  categoria (models.Model):
    nombre =models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
       

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog',null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created']

    def __str__(self):
        return self.titulo