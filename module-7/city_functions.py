#Dario Gomez CSD325 Assignment 7.2 4/15/2025


def get_city_country(city, country,language='',population=''):
    return_string = f"{city}, {country}"
    if population:
        return_string += f" - population {population}"
    if language:
        return_string += f", {language}"
    return return_string

combo1 = get_city_country('Madrid', 'Spain')
combo2 = get_city_country('Bogota', 'Colombia', population='20,000,000')
combo3 = get_city_country('Rome', 'Italy',population='30,000,000',language='Italian')

print(combo1)
print(combo2)
print(combo3)

