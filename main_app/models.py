from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=128, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} <- {self.category.name}'


class TableFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)


class ChartFile(models.Model):
    image = models.ImageField(upload_to='media/')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)


class Vacancy(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    key_skills = models.CharField(max_length=512, null=True, blank=True)
    company = models.CharField(max_length=128, null=True, blank=True)
    salary = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    area_name = models.CharField(max_length=128)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.publication_date}, {self.area_name}"
