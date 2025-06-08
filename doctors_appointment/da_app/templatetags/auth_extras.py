# da_app/templatetags/auth_extras.py

from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name="has_group")
def has_group(user, group_name):
    """
    Проверяет, входит ли пользователь в определенную группу.
    Использование в шаблоне: {% if user|has_group:"ИмяГруппы" %}
    """
    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False

    return group in user.groups.all()
