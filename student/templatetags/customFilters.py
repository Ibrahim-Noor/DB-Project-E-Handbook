from django import template

register = template.Library()

@register.filter(name='sub')
def cut(value, arg):
    return abs(value-arg)