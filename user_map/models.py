# coding=utf-8
"""Models for user map."""
from django.core.urlresolvers import reverse
import logging
from django.contrib.gis.db import models

logger = logging.getLogger(__name__)


class ApprovedEntryManager(models.Manager):
    """Custom entry manager that shows only approved records."""

    def get_query_set(self):
        """Query set generator"""
        return super(
            ApprovedEntryManager, self).get_query_set().filter(
                approved=True)


class UnapprovedEntryManager(models.Manager):
    """Custom entry manager that shows only unapproved records."""

    def get_query_set(self):
        """Query set generator"""
        return super(
            UnapprovedEntryManager, self).get_query_set().filter(
                approved=False)


class Role(models.Model):
    """Role for users e.g. developer, trainer, user."""
    name = models.CharField(
        help_text='How would you define your participation?',
        max_length=255,
        null=False,
        blank=False,
        unique=True)
    sort_number = models.IntegerField(
        help_text='Sorting order for role in role list.',
        null=True,
        blank=True)


class UserPoint(models.Model):
    """An entry is the basic unit of a changelog."""
    name = models.CharField(
        help_text='Title for this change note.',
        max_length=255,
        null=False,
        blank=False,
        unique=True)

    email = models.EmailField(
        help_text='Describe the new feature. Markdown is supported.',
        null=False,
        blank=False,
        unique=True)

    website = models.URLField(
        help_text='Optional link to your personal or organisation web site.',
        null=True,
        blank=True)

    point = models.PointField(
        help_text='Where are you?',
        max_length=255,
        null=False,
        blank=False)
    role = models.ForeignKey(Role)
    email_updates = models.BooleanField(
        help_text='Tick this to receive occasional news email messages.'
    )
    approved = models.BooleanField(
        help_text='Whether this user has approved their entry by email.'
    )
    objects = models.GeoManager()
    approved_objects = ApprovedEntryManager()
    unapproved_objects = UnapprovedEntryManager()

    # noinspection PyClassicStyleClass
    class Meta:
        """Meta options for the version class."""
        app_label = 'user_map'

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        """URL that can be used to access the edit form for the user.
        """
        return reverse('user', kwargs={
            'uid': self.uid,
        })
