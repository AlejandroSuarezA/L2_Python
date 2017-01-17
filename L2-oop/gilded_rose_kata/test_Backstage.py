from normalItem import *

if __name__ == '__main__':

    item = Ticket("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 30):
        item.update_quality()
        print(item)
