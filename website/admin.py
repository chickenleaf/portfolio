from django.contrib import admin
from website.models import Contact

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
