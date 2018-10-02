import gkeepapi

class Keep:
    def __init__(self, user, password):
        self.keep = gkeepapi.Keep()
        success = self.keep.login(user, password)

        #self.shopping = sorted(self.keep.get('1525379338363.1704307895').items, key=lambda item: -int(item.sort))
        #self.shopping_order = sorted(self.keep.get('1525384801118.2014102721').items, key=lambda item: -int(item.sort))
        #self.shopping = self.keep.get('1525542472380.379233536')
        #self.shopping_order = self.keep.get('1525384801118.2014102721')

    def add_shopping(self, str):
        self.shopping.add(str)
        self.keep.sync()

    def remove_shopping(self, str):
        for item in self.shopping.items:
            if item.text == str:
                item.delete()
        self.keep.sync()

    def sort_shopping(self):
        for item in self.shopping.items:
            for ritem in self.shopping_order.items:
                if ritem.text == item.text:
                    item.sort = ritem.sort
                    break
        self.keep.sync()

    def save_sort_shopping(self):
        start = 0
        for item in self.shopping.items:
            found = False
            for ritem in self.shopping_order.items:
                if ritem.text == item.text:
                    ritem.sort = item.sort
                    found = True
                    break
            # add of not found yet
            if not found:
                self.shopping_order.add(item.text)
                for ritem in self.shopping_order.items:
                    if ritem.text == item.text:
                        ritem.sort = item.sort
        self.keep.sync()
