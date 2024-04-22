from dataclasses import dataclass
import random
from faker import Faker

faker_ru = Faker("ru_RU")


# faker_en = Faker("En")


@dataclass
class Person:
    full_name: str
    first_name: str
    last_name: str
    email: str
    age: int
    salary: int
    department: str
    current_address: str
    permanent_address: str
    phone_number: str

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield value


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(18, 100),
        salary=random.randint(15000, 400000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        phone_number=faker_ru.msisdn(),
    )
