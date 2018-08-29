from django.contrib import admin
from .models import Workshop, Workshift, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['date', 'workshop', 'workshift', 'machine_num', 'order_num',
                  'product_num','product_units','waste_num','operator','remarks']


admin.site.register(Workshop)
admin.site.register(Workshift)
admin.site.register(Post, PostAdmin)