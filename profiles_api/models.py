from django.db import models
# to override defoult administration
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your models here.
# user UserProfileManager
class UserProfileManager(BaseUserManager):
    '''manager for user profile '''
    def create_user(self,email,name,password=None):
        '''çreate new user profile'''
        if not email:
            raise ValueError('user must have a email address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        '''create and save super uswr with given detail'''
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user





#user profile
class UserProfile(AbstractBaseUser,PermissionsMixin):
    ''' DATAbase model for users in the system'''
    email=models.EmailField(max_length=255,unique=True)
    name= models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        '''returive full name of user'''
        return self.name

    def get_short_name(self):
        '''retrive short name of user'''
        return self.name

    def __str__(self):
        '''return string representation of user'''
        return self.email
