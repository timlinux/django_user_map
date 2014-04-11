# -*- coding: utf-8 -*-
"""View classes for Role"""

__author__ = 'Tim Sutton <tim@linfinit.com>'
__revision__ = '$Format:%H$'
__date__ = ''
__license__ = ''
__copyright__ = ''

# noinspection PyUnresolvedReferences
import logging

logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.views.generic import (
    ListView)
from django.http import Http404
from pure_pagination.mixins import PaginationMixin

from .models import Role


def index(request):
    """Create a map.

    :param request: A django request object.
    :type request: request

    :returns: Reponse will be a nice looking map page.
    :rtype: HttpResponse
    """
    return HttpResponse("Hello, world. You're at the user_map index.")


class JSONResponseMixin(object):
    """A mixin that can be used to render a JSON response."""
    def render_to_json_response(self, context, **response_kwargs):
        """Returns a JSON response, transforming 'context' to make the payload.

        :param context: Context data to use with template.
        :type context: dict

        :param response_kwargs: Keyword args
        :type response_kwargs: dict

        :returns A HttpResponse object that contains JSON
        :rtype: HttpResponse
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs)

    @staticmethod
    def convert_context_to_json(context):
        """Convert the context dictionary into a JSON object.

        :param context: Context data to use with template
        :type context: dict

        :return: JSON representation of the context
        :rtype: str
        """
        result = '{\n'
        first_flag = True
        for category in context['roles']:
            if not first_flag:
                result += ',\n'
            result += '    "%s" : "%s"' % (category.id, category.name)
            first_flag = False
        result += '\n}'
        return result


class RoleMixin(object):
    """Mixin class to provide standard settings for Role."""
    model = Role  # implies -> queryset = Role.objects.all()
    #form_class = RoleForm


class JSONRoleListView(RoleMixin, JSONResponseMixin, ListView):
    """List view for Role as json object - needed by javascript."""
    context_object_name = 'role'

    def dispatch(self, request, *args, **kwargs):
        """Ensure this view is only used via ajax.

        :param request: Http request - passed to base class.
        :type request: HttpRequest, WSGIRequest

        :param args: Positional args - passed to base class.
        :type args: tuple

        :param kwargs: Keyword args - passed to base class.
        :type kwargs: dict
        """
        if not request.is_ajax():
            raise Http404("This is an ajax view, move along please.")
        return super(JSONRoleListView, self).dispatch(
            request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        """Render this version as markdown.

        :param context: Context data to use with template.
        :type context: dict

        :param response_kwargs: A dict of arguments to pass to the renderer.
        :type response_kwargs: dict

        :returns: A rendered template with mime type application/text.
        :rtype: HttpResponse
        """
        return self.render_to_json_response(context, **response_kwargs)

    def get_queryset(self):
        """Get the queryset for this view.

        :returns: A queryset contains all role objects.
        :rtype: QuerySet

        :raises: Http404
        """
        qs = Role
        return qs


class RoleListView(RoleMixin, PaginationMixin, ListView):
    """List view for Role."""
    context_object_name = 'roles'
    template_name = 'user_map/role_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """Get the context data which is passed to a template.

        :param kwargs: Any arguments to pass to the superclass.
        :type kwargs: dict

        :returns: Context data which will be passed to the template.
        :rtype: dict
        """
        context = super(RoleListView, self).get_context_data(**kwargs)
        context['num_roles'] = context['roles'].count()
        return context

    def get_queryset(self, queryset=None):
        """Get the queryset for this view.

        :param queryset: Optional query set to override the default.
        :type queryset: QuerySet

        :returns: Role Queryset.
        :rtype: QuerySet
        """
        if queryset is not None:
            return queryset
        return self.queryset

