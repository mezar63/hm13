from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Blog

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Add the specified number of blogs to the database"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, default=100)

    def handle(self, *args, **options):
        for i in range(options["number"]):
            blog = Blog.objects.create(title=fake.sentence(), content=fake.paragraph())

            self.stdout.write(
                self.style.SUCCESS('Successfully added blog "%s"' % blog.id)
            )
