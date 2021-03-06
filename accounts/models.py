from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class ListUserManager(BaseUserManager):

    def create_user(self,email):
        ListUser.objects.create(email=email)

    def create_superuser(self, email, password):
        self.create_user(email)

class ListUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'
    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == 'nwilliams36@yahoo.com'

    @property
    def is_active(self):
        return True

