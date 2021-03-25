"""Product Tags Extras"""

# Django
from django import template

register = template.Library()


@register.filter(name='format_to_cop')
def format_to_cop(value):
    return '$ {:,.0f} COP'.format(value)


@register.filter(name='get_main_picture')
def get_main_picture(obj):
    return obj.get_main_picture()
