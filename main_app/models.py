from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    conversion_rate_to_rub = models.DecimalField(max_digits=10, decimal_places=4)


class Region(models.Model):
    name = models.CharField(max_length=50)


class Skill(models.Model):
    name = models.CharField(max_length=50)


class Employer(models.Model):
    name = models.CharField(max_length=100)


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, through='VacancySkill')
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    publication_date = models.DateField()


class VacancySkill(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
