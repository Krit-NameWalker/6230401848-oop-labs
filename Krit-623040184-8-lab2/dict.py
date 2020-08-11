DT = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
}

DT["Jane Doe"] = "+27 555 1024"
DT["Anna Cooper"] = "+27 555 3237"

print(DT["Bob Stone"])
print(DT.get("Bob Stone", None))
print(DT.keys())
print(DT.values())
