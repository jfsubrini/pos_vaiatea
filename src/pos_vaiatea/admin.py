"""Overinding the default Admin with custom Vaiatea header, site title and index title.
    """
from django.contrib.admin import AdminSite


class VaiateaAdmin(AdminSite):
    """Vaiatea header, site title and index title."""
    site_header = 'Vaiatea Administration'
    site_title = 'Vaiatea Site Admin'
    index_title = 'Vaiatea Site Admin Home'
