from django.contrib import admin

from main_app.models import Theme, Chart, Category, TableData, Vacancy

admin.site.register(Theme)
admin.site.register(Vacancy)
admin.site.register(Chart)
admin.site.register(Category)
admin.site.register(TableData)
