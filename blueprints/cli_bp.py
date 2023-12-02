from init import db, bcrypt
from flask import Blueprint
from models.user import User
from models.trip import Trip
from models.destination import Destination
from models.activity import Activity
from datetime import timedelta

dbcli_bp = Blueprint('db',__name__ )

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
            username = "WandaWanderer",
            email = "wanda@gmail.com",
            password = "testpassword"
        ),
        User(
            username = "GaryGlobal",
            email = "gazza@email.com",
            password = "testpassword"
        ),
        User(
            username = "NickyNomad45",
            email = "nicholas@nomadtravelco.com",
            password = "testpassword",
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    trips = [
        Trip(
            trip_name ="Winter Snowboarding + Tokyo",
            start_date = '2024/01/15',
            finish_date = '2024/1/29',
            estimated_budget = 7000,
            trip_desc = "Snowboarding in two resorts on the northern island of Hokkaido + a few days in Tokyo"
        ),
        Trip(
            trip_name ="Backpacking Mainland Europe",
            start_date = '2023/07/15',
            finish_date = '2023/9/15',
            estimated_budget = 15000,
            trip_desc = "Spain, France, Italy and Germany - Festivals"
        ),
        Trip(
            trip_name ="Vietnam on Motorbike",
            start_date = '2023/08/10',
            finish_date = '2024/08/15',
            estimated_budget = 2000,
            trip_desc = "Riding from Hanoi to Hoi"
        ),
        Trip(
            trip_name ="Nothern Lights Trip",
            start_date = '2024/02/4',
            finish_date = '2024/3/11',
            estimated_budget = 6500,
            trip_desc = "Camping in the wilderness and hoping to see the Aurora Borealis"
        )
    ]

    db.session.add_all(trips)
    db.session.commit()

    destinations = [
        Destination(
            dest_country = 'Japan',
            dest_name = 'Niseko Ski Resort'
        ),
        Destination(
            dest_country = 'Japan',
            dest_name = 'Nozawa Onsen Ski Resort'
        ),
        Destination(
            dest_country = 'Japan',
            dest_name = 'Tokyo'
        ),
        Destination(
            dest_country = 'Spain',
            dest_name = 'Bunol'
        ),
        Destination(
            dest_country = 'Spain',
            dest_name = 'Pamplona'
        ),
        Destination(
            dest_country = 'France',
            dest_name = 'Chamonix'
        ),
        Destination(
            dest_country = 'Italy',
            dest_name = 'Rome'
        ),
        Destination(
            dest_country = 'Germany',
            dest_name = 'Munich'
        ),
        Destination(
            dest_country = 'Germany',
            dest_name = 'Hohenschwangau'
        ),
        Destination(
            dest_country = 'Vietnam',
            dest_name = 'Hanoi'
        ),
        Destination(
            dest_country = 'Vietnam',
            dest_name = 'Bai Bien Vinh Thai beach'
        ),
        Destination(
            dest_country = 'Vietnam',
            dest_name = 'Hue'
        ),
        Destination(
            dest_country = 'Vietnam',
            dest_name = 'Hoi An'
        ),
        Destination(
            dest_country = 'Canada',
            dest_name = 'La Crete'
        )
    ]

    db.session.add_all(destinations)
    db.session.commit()
    
    activities = [
        Activity(
            activity_name = 'Snowboarding Niseko resort',
            activity_desc = 'Explore the resort and riding from the peak to the bottom',
            activity_location_URL = 'https://maps.app.goo.gl/WN9YHnqVA7MSowBT8',
            budget = 2000
        ),
        Activity(
            activity_name = 'Hike Mt Yotei',
            activity_desc = 'Rent snowshoes/poles and and a guide to take us to the top to ride down',
            activity_location_URL = 'https://maps.app.goo.gl/WN9YHnqVA7MSowBT8',
            budget = 500
        ),
        Activity(
            activity_name = 'Snowboarding Nozawa Onsen Resort',
            activity_desc = 'Explore the resort and ride the backcountry',
            activity_location_URL = 'https://maps.app.goo.gl/xkqVSWxRvw1zS85W9',
            budget = 1700
        ),
        Activity(
            activity_name = 'Have an onsen in a Soto-yu',
            activity_desc = 'Use of the many free public baths to relax , post snowboarding',
            activity_location_URL = 'https://maps.app.goo.gl/xkqVSWxRvw1zS85W9',
            budget = 0
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        Activity(
            activity_name = 'Shopping in Harajuku',
            activity_desc = 'Walk around and look for some crazy fashion to buy',
            activity_location_URL = 'https://maps.app.goo.gl/K4uuJJYzsR9ek8Fh9',
            budget = 15
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        ),
        
        Activity(
            activity_name = 'Drinking in Golden Gai, Shinjuku',
            activity_desc = 'Go to as many bars as possible and meet new people',
            activity_location_URL = 'https://maps.app.goo.gl/xsZhtKfEp6vQx9LcA',
            budget = 2000
        )
    ]
    
    
    db.session.add_all(activities)
    db.session.commit()
    print('Tables seeded without error')
