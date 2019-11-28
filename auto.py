auto = ["bmw", "Honda", "Mercedes","bmw"]

auto.append("Audi")
auto.append("Honda")


print(auto)
print(len(auto))
print(auto.count("bmw"))
print(auto.count("Lexus"))
print(auto[0:3])
print(auto[-1])
print(auto.index("Honda"))
print("bmw" in auto)
auto.remove("Honda")
del auto[3]
print(auto)