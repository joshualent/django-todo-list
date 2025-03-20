from django.contrib import admin

from .models import Todo, Note

# Register your models here.


class NoteInline(admin.TabularInline):
    model = Note
    # display no extra rows in admin view
    extra = 0


# Representation of the model admin interface for Todo
class TodoAdmin(admin.ModelAdmin):
    inlines = [NoteInline]


# Register Todo model to Admin with TodoAdmin representation
admin.site.register(Todo, TodoAdmin)
# Register Note model to Admin
admin.site.register(Note)
