from faker import Faker

fake = Faker("Ru-ru")


class Data:
    def __init__(self, first_name=None, last_name=None, email=None, phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    @staticmethod
    def random():
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()

        return Data(first_name=first_name, last_name=last_name, email=email, phone=phone)