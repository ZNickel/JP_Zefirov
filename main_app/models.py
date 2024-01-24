from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=128, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TableData(models.Model):
    title = models.CharField(max_length=128)
    column_names = models.CharField(max_length=128)
    row_names = models.CharField(max_length=128)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    pass


class Chart(models.Model):
    title = models.CharField(max_length=128)
    image_path = models.CharField(max_length=256)
    alt_text = models.CharField(max_length=256, null=True, blank=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    key_skills = models.CharField(max_length=512, null=True, blank=True)
    company = models.CharField(max_length=128, null=True, blank=True)
    salary = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    area_name = models.CharField(max_length=128)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.salary}, {self.area}"
