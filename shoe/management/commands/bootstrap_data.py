from django.core.management.base import BaseCommand
from shoe.models import ShoeColor, ShoeType

class Command(BaseCommand):
    help = 'populates ShoeColor and ShoeType tables with data.'

    def handle(self, *args, **options):
        for choice in ShoeColor.colors:
            ShoeColor.objects.create(color=choice[0])
            self.stdout.write(self.style.SUCCESS(
                'Successfully closed color "%s"' % choice[1]))

        for choice in ShoeType.types:
            ShoeType.objects.create(style=choice[0])
            self.stdout.write(self.style.SUCCESS(
                'Successfully closed type "%s"' % choice[1]))