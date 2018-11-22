from django import template
register = template.Library()

@register.assignment_tag
def set(val=-1):
  return val+1