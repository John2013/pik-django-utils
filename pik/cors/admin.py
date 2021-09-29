from django.contrib import admin

from pik.admin import SecuredVersionedModelAdmin

from pik.cors.models import Cors


@admin.register(Cors)
class CorsAdmin(SecuredVersionedModelAdmin):
    list_display = ['cors']
    search_fields = ['cors']
    permitted_fields = {'{app_label}.change_{model_name}': ['cors']}