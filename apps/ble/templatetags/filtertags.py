from django import template

register = template.Library()

@register.filter
def in_room(things, gateway):
    return things.filter(gateway=gateway)