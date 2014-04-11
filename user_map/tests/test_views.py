# coding=utf-8
"""Tests for views."""
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from user_map.tests.model_factories import RoleF, UserPointF
from core.model_factories import UserF
import logging


class TestUserPointViews(TestCase):
    """Tests that User Point views work."""

    def setUp(self):
        """Setup before each test."""
        logging.disable(logging.CRITICAL)
        self.role = RoleF.create()
        self.user_point1 = UserPointF.create(role=self.role)
        self.user_point1 = UserPointF.create(role=self.role)
        self.user = UserF.create(username='timlinux', password='password')

    def test_list_view(self):
        client = Client()
        response = client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)
        expected_templates = [u'user_map/list.html']
        self.assertEqual(response.template_name, expected_templates)
        self.assertEqual(
            response.context_data['object_list'][0],
            self.my_category)

    def test_create_with_login(self):
        my_client = Client()
        my_client.login(username='timlinux', password='password')
        my_response = my_client.get(reverse('category-create', kwargs={
            'project_slug': self.my_project.slug
        }))
        self.assertEqual(my_response.status_code, 200)
        expected_templates = ['category/create.html']
        self.assertEqual(my_response.template_name, expected_templates)
