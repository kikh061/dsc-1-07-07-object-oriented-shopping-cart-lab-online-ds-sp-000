class ShoppingCart:

    #init
    def __init__(self,employee_discount=None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount
        
    #total
    def get_total(self):
        return self._total
    
    def set_total(self, amount):
        self._total = amount
        
    total = property(get_total, set_total)
    
    
    #items
    def get_items(self):
        return self._items
    
    def set_items(self,item):
        self._items += item
    
    items = property(get_items, set_items)
    
    
    
    #employee_discount
    def get_employee_discount(self):
        return self._employee_discount
    
    
    def set_employee_discount(self,amount):
        self._employee_discount = amount
        
    employee_discount = property(get_employee_discount, set_employee_discount)
    
    
    #custom methods
    def add_item(self, item, amount,quantity=1):
        i = 1
        while i<= quantity:
            self._items.append({"name":item,"price":amount})
            self._total += amount
            i+=1
        return self._total
        
    
    #mean
    def mean_item_price(self):
        numberOfItems = len(self._items)
        total = self._total
        return total/numberOfItems
    
    
    
    #median
    def median_item_price(self):
        
        #get all prices
        prices = []
        for item in self._items:
            prices.append(item['price'])
            
        #sort all prices
        prices.sort()
        
        #check length and get median
        if len(prices)%2 == 0:
            return (prices[int(len(prices)/2)] + prices[int(len(prices)/2+1)]/2)
        else:
            return prices[int(len(prices)/2)]
            
            
            
    #apply_discount
    def apply_discount(self):
        if self._employee_discount:
            return (100-self._employee_discount)/100*self._total 
        else:
          return "Sorry, there is no discount to apply to your cart :("  
        
    #item_names
    def item_names(self):
        item_list = []
        for item in self._items:
            item_list.append(item['name'])
            
        return item_list
        
    #delete last item
    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']