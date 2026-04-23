from django.core.management.base import BaseCommand
from users.models import User


USERS = [
    'Alice',
    'Bob',
    'Carol',
    'David',
    'Eve',
]


class Command(BaseCommand):
    help = 'Seed the database with sample users'

    def handle(self, *args, **kwargs):
        for name in USERS:
            user, created = User.objects.get_or_create(name=name)
            if created:
                self.stdout.write(f'Created user: {name}')
            else:
                self.stdout.write(f'User already exists: {name}')
        self.stdout.write(self.style.SUCCESS('User seeding complete.'))
