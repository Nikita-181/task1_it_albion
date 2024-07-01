import datetime

from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

from django.contrib.auth.models import User


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__lastlogin = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            format='d.m.Y',
            anchor='100%')

        self.field__superusersatus = ext.ExtCheckBox(
            label=u'superuser satus',
            name='superusersatus',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__firstname = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=True,
            anchor='100%')

        self.field__lastname = ext.ExtStringField(
            label=u'last_name',
            name='last_name',
            allow_blank=True,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            allow_blank=True,
            anchor='100%')

        self.field__staffstatus = ext.ExtCheckBox(
            label=u'is_staff',
            name='staffstatus',
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label=u'active',
            name='active',
            checked=True,
            anchor='100%')

        self.field__datejoined = ext.ExtDateField(
            label=u'date joined',
            name='datejoined',
            format='d.m.Y',
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__lastlogin,
            self.field__superusersatus,
            self.field__username,
            self.field__firstname,
            self.field__lastname,
            self.field__email,
            self.field__staffstatus,
            self.field__active,
            self.field__datejoined
        ))



    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
