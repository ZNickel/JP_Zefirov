from django.contrib import admin

from main_app.models import Currency, Region, Skill, Employer, Vacancy, VacancySkill

admin.site.register(Currency)
admin.site.register(Region)
admin.site.register(Skill)
admin.site.register(Employer)
admin.site.register(Vacancy)
admin.site.register(VacancySkill)
