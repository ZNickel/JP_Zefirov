from django.contrib import admin

from main_app.models import Theme, ChartFile, Category, TableFile, Vacancy

admin.site.register(Theme)
admin.site.register(Vacancy)
admin.site.register(ChartFile)
admin.site.register(Category)
admin.site.register(TableFile)
