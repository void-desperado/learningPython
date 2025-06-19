from cityFunctions import cityCountry

def test_city_country():
    result=cityCountry('delhi','india','1000')
    assert result=="Delhi, India - population 1000"