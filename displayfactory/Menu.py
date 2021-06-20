#from ProductFactory import *
from GridMenu import *
if __name__=='__main__':
    Items=GridMenu()
    Allitems=Items.DisplayItems()
    for item in Allitems:
        print(item.name)
        print(item.price)