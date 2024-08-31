from django.contrib import admin
from website.models import Contact
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

