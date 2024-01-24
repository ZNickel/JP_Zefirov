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


class TableData(models.Model):
    title = models.CharField(max_length=128)
    column_names = models.CharField(max_length=128)
    row_names = models.CharField(max_length=128)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.column_names}, {self.row_names}, {self.theme.name}'


class TableRow(models.Model):
    value_a = models.CharField(max_length=128)
    value_b = models.CharField(max_length=128)
    models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    table_data = models.ForeignKey(TableData, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value_a} - {self.value_b}'


class Chart(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='media/')
    alt_text = models.CharField(max_length=256, null=True, blank=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} <- {self.theme}'


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
