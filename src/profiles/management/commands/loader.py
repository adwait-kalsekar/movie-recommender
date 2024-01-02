from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from movies.models import Movie
from movie_recommender import utils as movie_recommender_utils

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", nargs="?", default=10, type=int)
        parser.add_argument("--movies", action="store_true", default=False)
        parser.add_argument("--users", action="store_true", default=False)
        parser.add_argument("--show-total", action="store_true", default=False)

    def handle(self, *args, **options):
        count = options.get('count')
        load_movies = options.get('movies')
        generate_users = options.get('users')
        show_total = options.get('show_total')

        if load_movies:
            movie_dataset = movie_recommender_utils.load_movie_data(count)
            new_movies = [Movie(**movie) for movie in movie_dataset]

            movies_bulk = Movie.objects.bulk_create(new_movies, ignore_conflicts=True)

            print(f"Movies Created: {len(movies_bulk)}")

        if generate_users:
            profiles = movie_recommender_utils.create_fake_users(count)

            new_users = []
            for profile in profiles:
                new_users.append(User(**profile))

            user_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)

            print(f"Users Created: {len(user_bulk)}")

        if show_total:
            print(f"Total Users: {User.objects.count()}")
            print(f"Total Movies: {Movie.objects.count()}")