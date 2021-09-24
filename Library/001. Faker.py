from faker import Faker
fake = Faker()
print("Name:", fake.name())
print("Jobs:", fake.job())
print("Email:", fake.email())
print("Country:", fake.country())
print(fake.profile())