def car(manufacturer,model,**properties):
    properties['Manufacturer']=manufacturer
    properties['Model Name']=model
    return properties

myCar = car('subaru', 'outback', color='blue', tow_package=True)
print(myCar)