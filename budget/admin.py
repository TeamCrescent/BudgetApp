# from django.contrib import admin
# from .models import Project, Expense, Category
# # Register your models here.
#
# admin.site.register(Project)
# admin.site.register(Expense)
# admin.site.register(Category)

from django.contrib import admin
from .models import Project, Expense, Category

admin.site.register(Project)
admin.site.register(Expense)
admin.site.register(Category)
