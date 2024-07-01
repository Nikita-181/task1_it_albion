import objectpack.ui as OPUI
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack

# from .models import Person

# from .add_window_class import PersonAddWindow
from .user_add_window import UserAddWindow
from .PermissionAddWindow import PermissionAddWindow

"""
class PersonPack(ObjectPack):

    model = Person

    add_to_desktop = edit_window = True

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    # add_to_menu = True

    add_window = PersonAddWindow
"""

class ContentTypeWindow(ObjectPack):

    model = ContentType

    add_to_desktop = True

    add_window = edit_window = OPUI.ModelEditWindow.fabricate(model)

class UserWindow(ObjectPack):

    model = User

    add_to_desktop = True

    add_window = edit_window = UserAddWindow# OPUI.ModelEditWindow.fabricate(User)#UserAddWindow #

    columns = [
        {
            'data_index': 'password',
            'header': u'password',
            'width': 2,
        },
        {
            'data_index': 'last_login',
            'header': u'last login',
            'width': 2,
        },
        {
            'data_index': 'superusersatus',
            'header': u'superuser satus',
            'width': 1,
        },
        {
            'data_index': 'username',
            'header': u'username',
            'width': 1,
        },
        {
            'data_index': 'first_name',
            'header': u'first name',
            'width': 1,
        },
        {
            'data_index': 'last_name',
            'header': u'last name',
            'width': 1,
        },
        {
            'data_index': 'email',
            'header': u'email address',
            'width': 1,
        },
        {
            'data_index': 'is_staff',
            'header': u'staff status',
            'width': 1,
        },
        {
            'data_index': 'is_active',
            'header': u'active',
            'width': 1,
        },
        {
            'data_index': 'date_joined',
            'header': u'date joined',
            'width': 1,
        }
    ]

class GroupWindow(ObjectPack):

    model = Group

    add_to_desktop = True

    add_window = edit_window = OPUI.ModelEditWindow.fabricate(model)

class PermissionWindow(ObjectPack):

    model = Permission

    add_to_desktop = True

    add_window = edit_window = PermissionAddWindow #OPUI.ModelEditWindow.fabricate(model)

