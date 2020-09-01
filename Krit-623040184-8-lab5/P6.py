def make_greeting(title, name, surname, formal=True, time=None):
    if formal:
        fullname = "%s %s" % (title, surname)
    else:
        fullname = name
    if time is None:
        greeting = "Hello"
    else:
        greeting = "Good %s" % time
    return "%s, %s!" % (greeting, fullname)

print(make_greeting("Mr", "John", "Smith"))
print(make_greeting("Mr", "John", "Smith", False))
print(make_greeting("Mr", "John", "Smith", False, "evening"))

make_greeting2 = make_greeting

my_dict = {
"title": "Mr",
"name": "John",
"surname": "Smith",
"formal": False,
"time": "evening",
}

print(make_greeting("Mr", "Mana", "Deejai", True, None))
print(make_greeting2(**my_dict))