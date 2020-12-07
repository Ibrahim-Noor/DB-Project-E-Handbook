from django import template

register = template.Library()

@register.filter(name='sub')
def cut(value, arg):
    try:
        return abs(value-arg)
    except: 
        return 0