# coding=utf-8
"""Tests for models."""
from django.test import TestCase
from .model_factories import RoleF, UserPointF


class TestUserPointCRUD(TestCase):
    """Test UserPoint models."""
    factory = UserPointF

    def setUp(self):
        """Sets up before each test."""
        pass

    def test_create(self):
        """Tests creation."""
        model_instance = self.factory.create()

        #check if PK exists
        self.assertTrue(model_instance.pk is not None)

        #check if name exists
        self.assertTrue(model_instance.name is not None)

    def test_read(self):
        """Tests read."""
        model_instance = self.factory.create(
            name=u'Joe Brown'
        )
        self.assertTrue(model_instance.name == 'Joe Brown')
        self.assertTrue(model_instance.slug == 'custom-category')

    def test_update(self):
        """
        Tests Category model update
        """
        model_instance = self.factory.create()
        new_model_data = {
            'name': u'New Category Name',
            'description': u'New description',
            'approved': False,
            'private': True,
        }
        model_instance.__dict__.update(new_model_data)
        model_instance.save()

        #check if updated
        for key, val in new_model_data.items():
            self.assertEqual(model_instance.__dict__.get(key), val)

    def test_delete(self):
        """
        Tests Category model delete
        """
        model_instance = self.factory.create()

        model_instance.delete()

        #check if deleted
        self.assertTrue(model_instance.pk is None)


class TestRoleCRUD(TestCase):
    """
    Tests CRUD for role models.
    """
    factory = RoleF

    def setUp(self):
        """Sets up before each test."""
        pass

    def test_create(self):
        """Tests model creation."""
        model_instance = self.factory.create()

        #check if PK exists
        self.assertTrue(model_instance.pk is not None)

        #check if name exists
        self.assertTrue(model_instance.title is not None)

    def test_read(self):
        """Tests model read."""
        model_instance = self.factory.create(
            title=u'Custom Entry'
        )

        self.assertTrue(model_instance.title == 'Some role')

    def test_update(self):
        """Tests model update."""
        model_instance = self.factory.create()
        new_model_data = {
            'name': u'Some rol',
        }
        model_instance.__dict__.update(new_model_data)
        model_instance.save()

        #check if updated
        for key, val in new_model_data.items():
            self.assertEqual(model_instance.__dict__.get(key), val)

    def test_delete(self):
        """Tests model delete."""
        model_instance = self.factory.create()
        model_instance.delete()
        #check if deleted
        self.assertTrue(model_instance.pk is None)
