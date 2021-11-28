from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
  return value.split(key)



@register.filter(name='index')
def index(sequence, position):
    return sequence[position]
