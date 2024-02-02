from django import template

register = template.Library()


@register.filter
def translate_numbers_to_persian(value):
    value = str(value)
    persian = '۰١٢٣٤٥٦٧٨٩'
    english = '0123456789'
    translation_table = value.maketrans(english, persian)
    return value.translate(translation_table)
