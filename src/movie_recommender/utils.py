from faker import Faker

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
