
from django.contrib import admin

from site_setup.models import MenuLink


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'url_or_path', 'new_tab')
    list_display_links = ('id', 'text', 'url_or_path')
    search_fields = ('id', 'text', 'url_or_path')
