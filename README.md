django\_user\_map
=================

Django app for creating a user map

# Quick start

1. Add "user\_map" to your INSTALLED\_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'user_map',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^user-map/', include('user_map.urls')),

3. Run `python manage.py migrate` to create the user_map models.

4. Start the development server.

5. Visit http://127.0.0.1:8000/user-map/ to participate in the map.
