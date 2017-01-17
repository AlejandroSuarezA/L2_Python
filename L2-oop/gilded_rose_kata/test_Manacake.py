from normalItem import *

if __name__ == '__main__':

    item = Conjured("Conjured Mana Cake", 3, 6)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)
