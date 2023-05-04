from django.contrib import admin
from hakusai.models import Actions, Exhibitions, Projects, Steps, ExhibitionSettings

# Register your models here.
admin.site.register(Actions)
admin.site.register(Exhibitions)
admin.site.register(Projects)
admin.site.register(Steps)
admin.site.register(ExhibitionSettings)