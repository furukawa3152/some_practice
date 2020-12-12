from faker import Faker

fake = Faker("ja_JP")
for i in range(10):
    print(f"name:{fake.name()}")
    print(f"address:{fake.address()}")

    print(f"一言：{fake.email()}")
