import datetime

from django import template

INSTAGRAM_USER_URL_TEMPLATE = 'http://instagram.com/{}'

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag
def instagram_url(username):
    return INSTAGRAM_USER_URL_TEMPLATE.format(username)
