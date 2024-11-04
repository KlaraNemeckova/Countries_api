from django.core.management.base import BaseCommand
from countries.models import Country
from countries.country_data import countries_dict

class Command(BaseCommand):
    help = 'Load countries data into the database' # informace pro uživatele, zobrazí se po zadání "python manage.py help load_countries"

    def handle(self, *args, **kwargs):
        for name, code in countries_dict.items():
            country, created = Country.objects.get_or_create(name = name, country_code = code)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added {name}'))
            else:
                self.stdout.write(self.style.WARNING(f'{name} already exists'))
