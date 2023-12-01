from init import db, bcrypt
from flask import Blueprint
from models.user import User
from models.trip import Trip
from datetime import timedelta

dbcli_bp = Blueprint('db',__name__)

@dbcli_bp.cli.command('create')
def db_drop_and_create():
    db.drop_all()
    db.create_all()
    print('Tables dropped and new tables created without error')

@dbcli_bp.cli.command('seed')
def seed_db():
    users = [
        User(
            username = "JohnnyAdmin",
            email = "Johnny@admin.com",
            password = "testpassword",
            admin_acc = True
        ),
        User(
            username = "WallyWanderer",
            email = "walfred@gmail.com",
            password = "testpassword"
        ),
        User(
            username = "GaryGlobal",
            email = "gazza@email.com",
            password = "testpassword"
        ),
        User(
            username = "NickyDAnomad45",
            email = "nicole@nomadtravelco.com",
            password = "testpassword",
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    trips = [
        Trip(
            trip_name ="Winter Snowboarding + Tokyo",
            trip_desc = "Going to two resorts in Japans northern island Hokkaido and then spend a few days in Tokyo",
            start_date = '2024/01/15',
            finish_date = '2024/1/29',
            estimated_budget = 7000
        ),
        Trip(
            trip_name ="Backpacking Mainland Europe",
            trip_desc = "Spain, France, Italy and Germany - Festivals",
            start_date = '2023/07/15',
            finish_date = '2023/9/15',
            estimated_budget = 15000
        ),
        Trip(
            trip_name ="Vietnam on Motorbike",
            trip_desc = "Riding from Hanoi to Hue",
            start_date = '2023/08/10',
            finish_date = '2024/08/15',
            estimated_budget = 2000
        ),
        Trip(
            trip_name ="Nothern Lights Trip",
            trip_desc = "Camping in the wilderness and hoping to see the Aurora Borealis",
            start_date = '2024/02/4',
            finish_date = '2024/3/11',
            estimated_budget = 6500
        )
    ]

    db.session.add_all(trips)
    db.session.commit()
    print('Tables seeded without error')

