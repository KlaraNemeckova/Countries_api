from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    group_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"
        ordering = ["name"]
