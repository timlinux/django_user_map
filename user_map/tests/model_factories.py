# coding=utf-8
"""Tests for the user map app."""
import factory
from user_map.models import Role, UserPoint


class RoleF(factory.django.DjangoModelFactory):
    """
    Role model factory
    """
    FACTORY_FOR = Role

    name = factory.Sequence(lambda n: u'Test Role %s' % n)
    sort_number = factory.Sequence(lambda n: n)


class UserPointF(factory.django.DjangoModelFactory):
    """
    UserPoint model factory
    """
    FACTORY_FOR = UserPoint

    name = factory.Sequence(lambda n: u'User: %s' % n)
    email = factory.Sequence(lambda n: u'fake_user%s@none.com' % n)
    website = factory.Sequence(lambda n: u'http://foo%s.com' % n)
    point = factory.Sequence(lambda n: u'POINT(-10.%s 38.%s)' % n)
    role = factory.SubFactory('changes.tests.model_factories.CategoryF')
    email_updates = True
    approved = True
