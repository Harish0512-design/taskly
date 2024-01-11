from django.contrib import admin

from todo.models import Task, Review, Profile


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content")
    list_filter = ("date_posted", "date_updated")
    list_editable = ("title", "content")
    list_per_page = 10

    def get_list_editable(self, request):
        if request.user.is_superuser:
            return self.list_editable
        else:
            return ()  # returning empty tuple so that no fields are editable


admin.site.register(Task, TaskAdmin)
admin.site.register(Review)
admin.site.register(Profile)
