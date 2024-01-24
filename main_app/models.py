from django.core.files.storage import default_storage
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


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
    file = models.FileField(upload_to='media')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)


class ChartFile(models.Model):
    image = models.ImageField(upload_to='media')
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

# @receiver(pre_delete, sender=TableFile)
# @receiver(pre_delete, sender=ChartFile)
# def delete_unused_files(sender, instance, **kwargs):
#     all_files = default_storage.listdir('media')[1]
#
#     # Получаем список файлов, на которые существует ссылка из модели ChartFile
#     used_in_table = set(TableFile.objects.values_list('file', flat=True))
#     used_in_chart = set(ChartFile.objects.values_list('image', flat=True))
#     referenced_files = used_in_table | used_in_chart
#
#     # Определяем список файлов, которые не имеют ссылок и удаляем их
#     unused_files = set(all_files) - set(referenced_files)
#     for file_name in unused_files:
#         file_path = f'media/{file_name}'
#         default_storage.delete(file_path)
