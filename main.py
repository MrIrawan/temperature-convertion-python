# python temperature convertion program

def celcius_to_fahrenheit(temperature_celcius):
    temperature_fahrenheit = (temperature_celcius * 9/5) + 32
    return temperature_fahrenheit

def celcius_to_reamur(temperature_celcius):
    temperature_reamur = temperature_celcius * 4/5
    return temperature_reamur

def fahrenheit_to_celcius(temperature_fahrenheit):
    temperature_celcius = (temperature_fahrenheit - 32) * 5/9
    return temperature_celcius