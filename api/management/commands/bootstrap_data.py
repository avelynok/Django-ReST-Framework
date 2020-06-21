from django.core.management.base import BaseCommand
from shoe.models import ShoeColor, ShoeType

class Command(BaseCommand):
    help = 'populates ShoeColor and ShoeType tables with data.'

    def handle(self, *args, **options):
        for color in colors:
            ShoeColor.objects.create(
                color_name = color
            )
        for type in types:
            ShoeType.objects.create(
                style = type
            )
        