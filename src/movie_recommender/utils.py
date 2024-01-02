from django.conf import settings
from faker import Faker
from pprint import pprint

import csv
import datetime

METADATA_CSV = settings.DATA_DIR / "movies_metadata.csv"

def validate_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        return None
    return date

def load_movie_data(limit=1):
    with open(METADATA_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        dataset = []
        for i, row in enumerate(reader):
            pprint(row)
            _id = row.get("id")
            try:
                _id = int(_id)
            except:
                _id = None

            release_date = validate_date(row.get("release_date"))

            data = {
                "id": _id,
                "title": row.get("title"),
                "overview": row.get("overview"),
                "release_date": release_date,
            }

            dataset.append(data)

            if i + 1 > limit:
                break

        return dataset

def create_fake_users(count=10):
    user_profiles = []
    fake = Faker()
    for _ in range(count):
        profile = fake.profile()
        data = {
            "username": profile.get('username'),
            "email": profile.get('mail'),
            "is_active": True,
        }
        if "name" in profile:
            fname, lname = profile.get('name').split(" ")[: 2]
            data["first_name"] = fname
            data["last_name"] = lname
        user_profiles.append(data)

    return user_profiles
