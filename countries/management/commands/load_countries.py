from django.core.management.base import BaseCommand
from countries.models import Country
from countries.countries_by_continent import list_by_continent


class Command(BaseCommand):
    help = 'Load countries data into the database' 

    def handle(self, *args, **kwargs):
        for continent, countries in list_by_continent.items():
            for name, code in countries.items():
                country, created = Country.objects.get_or_create(name=name, country_code=code)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added {name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{name} already exists'))