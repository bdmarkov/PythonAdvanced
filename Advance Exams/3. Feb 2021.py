def stock_availability(stock, del_or_sel, *args):
    if del_or_sel == "delivery":
        if args:
            for i in args:
                stock.append(i)
            return stock
    else:
        if args:
            for i in args:

                if type(i) == int:
                    for i in range(args[0]):
                        stock.pop(0)
                else:
                    if i in stock:
                        while i in stock:
                            stock.remove(i)
            return stock
        else:
            stock.pop(0)
            return stock

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
