from django import template
from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

register = template.Library()


@register.simple_tag
def weather_template_tag():
    source = urllib.request.urlopen(
        'http://api.openweathermap.org/data/2.5/weather?q='
        + 'cairo' + '&appid=06142c35a9c83aeb786b55dce0013b8f' + '&units=metric').read()

    # converting JSON data to a dictionary
    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' '
                      + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    return data
