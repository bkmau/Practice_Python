import datetime

person = {"name": "Jone", "age": 26}
# dictionary unpacking
print("Hi, I am {name} and, {age} years old.".format(**person))

print("Today is {0:%B %d %Y, %A}. It's {0:%H:%M:%S}.".format(datetime.datetime.now()))


class Product:
    @property
    def p_id(self):
        return self.__p_id

    @property
    def unit(self):
        return self.__unit

    @property
    def description(self):
        return self.__description

    def __init__(self, p_id, unit, description):
        self.__p_id = p_id
        self.__unit = unit
        self.__description = description

products = [
    Product("AX-B-X", "article", "Size X, Blue, for Women, Top"), 
    Product("YQ-B-M", "article", "Size M, Blue, for Men, Top"), 
    Product("TX-B-L", "article", "Size L, Blue, for Women, Skirt"), 
    Product("CW-R-X", "article", "Size X, Red, for Child, Top"), 
    Product("BX-R-M", "article", "Size M, Red, for Men, Jeans")]

detail = "{: ^10}|{: ^10}|{: ^100}\r\n".format("ID", "Unit", "Description")
detail.join("{{:=<{}}}".format(len(detail)).format(""))
for _ in range(len(detail)):
    detail += "="
detail += "\r\n"
for p in products:
    detail += "{0.p_id: <10}|{0.unit: <10}|{0.description: <100}\r\n".format(p)

print(detail)