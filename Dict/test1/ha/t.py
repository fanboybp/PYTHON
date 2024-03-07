dictCar = {
    "Brand": "Honda",
    "model": "Honda Civic",
    "year": 1972
}
print("*"*35)
# print(dictCar)
# print(dictCar["model"]) # cách 1
# print(dictCar.get("model")) # cách 2
print("Dic cũ:", dictCar)
# print(dictCar)
# dictCar["year"] = 2024
# print("Dic mới:")
# print(dictCar)
# for x in dictCar: # cách 1
#     print(x, ":", dictCar.get(x))
# for x in dictCar.values(): # cách 2
#     print(x)
# if "model" in dictCar:
#     print("Luân \"model\" có tồn tại.")
# else:
#     print("Luân \"model\" Không tồn tại.")
# print(len(dictCar))
dictCar["color"] = "BlackPink"
print(dictCar)
print("*"*35)