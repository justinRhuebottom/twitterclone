from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class TwitterUserManager(BaseUserManager):
    def create_user(self, handle, display_name, age, password=None, is_active=True, is_admin=False, is_staff=False):
        if not handle:
            raise ValueError("User must have a handle")
        if not display_name:
            raise ValueError("User must have a display name")
        if not age:
            raise ValueError("User must have a age")

        user = self.model(
            handle=handle, 
            display_name=display_name, 
            age=age,
            active=is_active,
            admin=is_admin,
            staff= is_staff
            )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, handle, display_name, age, password=None):
        user = self.create_user(
            handle, 
            display_name, 
            age, 
            password=password,
            is_admin = True, 
            is_staff=True
            )
        return user

class TwitterUser(AbstractBaseUser):
    handle       = models.CharField(max_length=20, unique=True)
    display_name = models.CharField(max_length=30)
    age          = models.DateField()
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    
    USERNAME_FIELD  = 'handle'
    REQUIRED_FIELDS = ['display_name', 'age']

    objects = TwitterUserManager()

    def __str__(self):
        return self.display_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active