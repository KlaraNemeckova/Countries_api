from django.db import models
from .countries_by_continent import (africa, asia, north_america, south_america, europe, oceania)

class Country(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    group_id = models.IntegerField(null=True, blank=True, default=1) 

    def save(self, *args, **kwargs):   
        if self.group_id is None:
           
            if self.country_code in africa.values():
                self.group_id = 1  
            elif self.country_code in asia.values():
                self.group_id = 2  
            elif self.country_code in europe.values():
                self.group_id = 3  
            elif self.country_code in north_america.values():
                self.group_id = 4  
            elif self.country_code in south_america.values():
                self.group_id = 5  
            elif self.country_code in oceania.values():
                self.group_id = 6  
            else:
                raise ValueError("Country does not exist.")
            
        super().save(*args, **kwargs)   

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"
        ordering = ["name"]
