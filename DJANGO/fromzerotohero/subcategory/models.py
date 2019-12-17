from django.db import models


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)
    category_id = models.IntegerField()

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return self.name
