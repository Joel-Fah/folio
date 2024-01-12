from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val == 0

@register.filter() 
def get_range(start, end):
    return range(start, end)