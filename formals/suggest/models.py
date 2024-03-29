from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.http import urlquote


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = CustomUserManager.normalize_email(email)
        user = self.model(email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class myUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    avatar = models.FileField(upload_to="avatar/", default='avatar/dp.png')
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.pk)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name


class Post(models.Model):
    posted_by = models.ForeignKey(myUser, related_name='postedBy')
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    love = models.IntegerField(default=0)
    total_comment = models.IntegerField(default=0)
    post = models.FileField(upload_to="post/")

    class Meta:
        ordering = ['-posted_on']

    def __unicode__(self):
        return self.description


class Comment(models.Model):
    commented_by = models.ForeignKey(myUser, related_name='commentedBy')
    commented_on = models.DateTimeField(default=timezone.now())
    comment = models.TextField(max_length=1000, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='commentedOn')
    commentImg = models.FileField(upload_to="comment/", blank=True)

    class Meta:
        ordering = ['-commented_on']

    def __unicode__(self):
        return '%s: %s' % (self.commented_by, self.comment)


class Lover(models.Model):
    lover_user = models.ForeignKey(myUser, related_name='user')
    love_post = models.ForeignKey(Post, related_name='love_post')

    class Meta:
        unique_together = ('lover_user', 'love_post')