rivers = {
    "Nile": ["Egypt", "Sudan", "South Sudan", "Ethiopia", "Uganda", "Democratic Republic of the Congo", "Kenya", "Tanzania", "Rwanda", "Burundi", "Eritrea"],
    "Amazon": ["Brazil", "Peru", "Colombia", "Ecuador", "Bolivia", "Venezuela", "Guyana"],
    "Yangtze": ["China"],
    "Mississippi": ["United States"],
    "Danube": ["Germany", "Austria", "Slovakia", "Hungary", "Croatia", "Serbia", "Romania", "Bulgaria", "Moldova", "Ukraine"],
    "Ganges": ["India", "Bangladesh"],
    "Mekong": ["China", "Myanmar", "Laos", "Thailand", "Cambodia", "Vietnam"],
    "Volga": ["Russia"],
    "Congo": ["Democratic Republic of the Congo", "Republic of the Congo", "Central African Republic", "Angola", "Zambia", "Tanzania", "Cameroon", "Burundi", "Rwanda"],
    "Indus": ["Pakistan", "India", "China"],
    "Tigris": ["Turkey", "Syria", "Iraq"],
    "Euphrates": ["Turkey", "Syria", "Iraq"],
    "Rhine": ["Switzerland", "Liechtenstein", "Austria", "Germany", "France", "Netherlands"],
    "Niger": ["Guinea", "Mali", "Niger", "Benin", "Nigeria"],
    "Murray": ["Australia"],
    "Seine": ["France"],
    "Thames": ["United Kingdom"],
    "Po": ["Italy"],
    "Loire": ["France"],
    "Zambezi": ["Zambia", "Angola", "Namibia", "Botswana", "Zimbabwe", "Mozambique"],
    "Paraná": ["Brazil", "Paraguay", "Argentina"]
}

for river,countries in rivers.items():
    for country in countries:
        print(f"The river {river} runs through {country}")