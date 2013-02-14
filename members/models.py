from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MemberManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(
            username=username,
            email=MemberManager.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username,email,password)
        user.is_admin = True
        user.save(using=self._db)
        return user

def avatar_file_name(instance, filename):
    return '/'.join(['avatars', str(instance.pk), filename])

class Member(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=254, unique=True) #make this unique when you're done testing
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    register_date = models.DateField(auto_now=True)
    # should be in kilobytes
    disk_space_used = models.IntegerField(null=True)
    # need to specify default path
    # avatar_pic_filepath = models.FilePathField(null=True)
    avatar_pic = models.FileField(upload_to=avatar_file_name)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def get_username_with_id(self):
        return dict(
            username = self.username,
            pk = self.pk,
        )

    objects = MemberManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin