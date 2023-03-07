from django import template


register = template.Library()


@register.filter
def list_dict_keys(dictionary):
    return list(dictionary.keys())


@register.filter
def list_dict_values(dictionary):
    return list(dictionary.values())
