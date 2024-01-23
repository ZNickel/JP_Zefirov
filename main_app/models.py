from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=50)


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, through='VacancySkill')
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency_code = models.CharField(max_length=3, null=True, blank=True)
    employer = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    publication_date = models.DateField()


class VacancySkill(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
