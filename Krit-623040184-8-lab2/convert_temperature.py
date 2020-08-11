Fahrenheit = False

while not Fahrenheit:
    try:
        t_f = int(input("Enter a temperature in Fahrenheit : "))
        t_c = 5 / 9
        x = (t_c) * (t_f - 32)
        print("Temperature is %.2f" % t_f, "in Fahrenheit is %.2f" % x, "in Celsius")
    except ValueError:
        print("Please enter valid floating point for the temperature")
    else:
        Fahrenheit = True
