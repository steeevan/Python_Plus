class Product:
    def __init__(self, product_id:str, name:str, description:str, price:float, stock:int) -> None:
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
    def update_stock(self,quantatiy) -> None:
        self.stock += quantatiy
    def display_product_info(self) -> str:
        return f"{self.name}: {self.description} - ${self.price} (Stock: {self.stock})"
    

if __name__ == "__main__":
    item = Product("001","Roblox GC","This is the roblox gif card",10.00,5)
    print(item)
    print(item.display_product_info())
    item.update_stock(5)
    print(item.display_product_info())