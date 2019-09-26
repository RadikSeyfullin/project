from django.contrib import admin
from todopage.models import TodoList, Category

# Register your models here.
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created", "due_date", "status", "deleted")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")

admin.site.register(TodoList,TodoListAdmin)
admin.site.register(Category,CategoryAdmin)
