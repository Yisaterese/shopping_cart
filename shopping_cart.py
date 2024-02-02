from typing import List
class shopping_cart:
    def __(self,items,max_size )-> None:
        self.items:List[str] = []
        self.max_size = max_size


    def add(self,item: str):
        self.items.append(item)
        return item

    def size(self,item: str) -> int:
        return len(self.items)
    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self,dict_price):
        total_price = 0
        for item in self.items:
            total_price += dict_price.get(dict_price)
        return total_price