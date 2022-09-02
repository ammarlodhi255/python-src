def get_datatype(var):
    typeVal = str(type(var))
    typeVal = typeVal[typeVal.find("'") + 1 : len(typeVal) - 2]
    return typeVal

var = "ammar"
print(f"Type of var is: {get_datatype(var)}")