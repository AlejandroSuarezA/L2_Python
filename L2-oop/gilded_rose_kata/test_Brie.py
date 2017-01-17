from normalItem import *

if __name__ == '__main__':

    item = Cheese("Aged Brie", 2, 0)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for day in range(1, 30):
        item.update_quality()
        print(item)