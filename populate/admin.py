from populate import base
from django.contrib.auth.models import User
# Register your models here.

def populate():
    print('Creating admin account...', end='')
    User.objects.all().delete()
    User.objects.create_superuser(username='admin', password='admin', email=None)
    print('done')

if __name__=='__main__':
    populate()
