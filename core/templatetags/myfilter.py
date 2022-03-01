from django import template
register=template.Library()

@register.filter(name='remove_special')
def remove_chars(value,args):
    print(value)
    for char in args:
        print(char)
        value = value.replace(char,"")
    return value    
