from django.contrib import admin
from.models import Post, categoria

# Register your models here.


class categoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(categoria, categoriaAdmin)
admin.site.register(Post, PostAdmin)