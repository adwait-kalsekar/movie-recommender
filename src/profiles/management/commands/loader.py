from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from movie_recommender import utils as movie_recommender_utils

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", nargs="?", default=10, type=int)
        parser.add_argument("--show-total", action="store_true", default=False)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        show_total = kwargs.get('show_total')
        profiles = movie_recommender_utils.create_fake_users(count)

        new_users = []
        for profile in profiles:
            new_users.append(User(**profile))

        user_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)

        print(f"Users Created: {len(user_bulk)}")

        if show_total:
            print(f"Total Users: {User.objects.count()}")