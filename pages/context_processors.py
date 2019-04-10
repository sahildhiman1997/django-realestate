from listings.choices import *

def add_variable_to_context(request):
    return {
        'cities': cities,
        'values':request.GET,
    }