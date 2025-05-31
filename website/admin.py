from django.contrib import admin
from website.models import Contact, Education, WorkExperience, Project, Achievement  # Import your models!
from .models import DownloadLog

class ContactAdmin(admin.ModelAdmin):
    # Display 'created_at' in the list view
    list_display = ('name', 'email', 'subject', 'created_at')

    # Make 'created_at' read-only in the form
    readonly_fields = ('created_at',)

    # Optionally, if you want to customize the layout in the admin form
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message', 'created_at')
        }),
    )

# Register the customized admin class
admin.site.register(Contact, ContactAdmin)

class DownloadLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'file_name', 'ip_address')
    list_filter = ('timestamp',)
    search_fields = ('file_name',)

# Register the download log class
admin.site.register(DownloadLog, DownloadLogAdmin)

# Register the Education, WorkExperience, and Project models
admin.site.register(Education)
admin.site.register(WorkExperience)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'github_url', 'live_url')
    list_filter = ('category',)
    search_fields = ('title', 'technologies', 'description')
    ordering = ('order',)

admin.site.register(Project, ProjectAdmin)

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('order', 'display_content_snippet')
    search_fields = ('content',)
    ordering = ('order',)

    def display_content_snippet(self, obj):

        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    display_content_snippet.short_description = "Content Snippet"

# Register the Achievement model with its custom admin class
admin.site.register(Achievement, AchievementAdmin)

