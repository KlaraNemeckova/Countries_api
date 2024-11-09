from django.db import models
from .countries_by_continent import list_by_continent


# Defines the Country model, representing a country in the database
class Country(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    group_id = models.IntegerField(null=True, blank=True) 


    # Save () method to automatically set group_id based on the continent
    def save(self, *args, **kwargs):
        if self.group_id is None:
            for index, (continent, countries) in enumerate(list_by_continent.items(), start=1):
                if self.country_code in countries.values():
                    self.group_id = index
                    break
            else:
                raise ValueError("Country does not exist.")

        super().save(*args, **kwargs) 

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"
        ordering = ["name"]




    


