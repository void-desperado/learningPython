def cityCountry(city,country,population=None):
    if population==None:
        return f"{city.title()}, {country.title()}"
    else:
        return f"{city.title()}, {country.title()} - population {population}"