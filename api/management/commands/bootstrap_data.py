from django.core.management.base import BaseCommand
from shoe.models import ShoeColor, ShoeType

class Command(BaseCommand):
    help = 'populates Shoe Color and Shoe Type .'
    def handle(self, *args, **options):
        types = [
            ('SK', 'Sneaker'),
            ('B', 'Boot'),
            ('SD', 'Sandal'),
            ('D', 'Dress'),
            ('O', 'Other')
        ]
        colors = [
            ('R', 'red'),
            ('O', 'orange'),
            ('Y', 'yellow'),
            ('G', 'green'),
            ('B', 'blue'),
            ('I', 'indigo'),
            ('V', 'violet'),
            ('B', 'black'),
            ('W', 'white'),
        ]
        for color in colors:
            ShoeColor.objects.create(color_name = color)
        for type in types:
            ShoeType.objects.create(style = type)
        