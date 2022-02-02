from django.contrib.auth.models import Group

from users.models import CustomUser

# Group objects

dc = Group(name='DC')
dc.save()

marvel = Group(name='Marvel')
marvel.save()

# User objects

eights = CustomUser(phone_number='+918888888888', password='Eight8s@',
                    first_name='Eight', last_name='8s@')
eights.save()
eights.groups.add(marvel)

sevens = CustomUser(phone_number='+917777777777', password='Seven7s@',
                    first_name='Seven', last_name='7s@')
sevens.save()
sevens.groups.add(dc)

threes = CustomUser(phone_number='+913333333333', password='Three3s@',
                    first_name='Three', last_name='3s@')

threes.save()
threes.groups.add(marvel, dc)
