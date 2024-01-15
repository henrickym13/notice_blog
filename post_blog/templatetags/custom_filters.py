from django import template

register = template.Library()

@register.filter(name='custom_data')
def custom_data(data):
    data = data[0:-10]
    data_list = data.split(sep='-')
    data_end = f'{data_list[2]}/{data_list[1]}/{data_list[0]}'
    return data_end