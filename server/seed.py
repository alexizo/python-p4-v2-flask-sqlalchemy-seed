from app import app
from models import db, Pet
from faker import Faker
from random import choice as rc

with app.app_context():
    Pet.query.delete()

    fake = Faker()

    pets = []

    species = ['Dog', 'Cat', 'Hamster', 'Snake']

    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    db.session.add_all(pets)

    db.session.commit()

    print("Database seeded!")
