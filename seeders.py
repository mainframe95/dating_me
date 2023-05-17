from models import Member, Gender
from faker import Faker

fake = Faker()



async def insertMember():
    # await Gender.create(
    #     label = 'Male',
    #     is_actived = True
    # )
    # await Gender.create(
    #     label = 'Female',
    #     is_actived = True
    # )
    for _ in range(8):
        print('_', _)
        # print(await Gender.filter( label = 'Female' if (_ % 2) else 'Male').first())
        name = fake.first_name()
        await Member.create(
            username =  name,
            firstname = name,
            lastname = fake.last_name(),
            email = name +'@gmail.com',
            salt = fake.address(),
            tel = fake.msisdn(),
            gender = await Gender.filter( label = 'Female' if (_ % 2) else 'Male').first()
        )