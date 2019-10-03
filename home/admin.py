from django.contrib import admin
from .models import Home

# Register your models here.


@admin.register(Home)
class home(admin.ModelAdmin):
    list_display = ('showing_blog_button', 'button_color', 'e_mail',
                    'title', 'Slogan', 'website_icon', 'logo', 'background_image_url1', 'background_image_url2', 'background_image_url3', 'Contact_link', 'About_link')

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False


# admin.site.register(Home, home)
