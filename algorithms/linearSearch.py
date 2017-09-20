def linearSearch(myItem, myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position +1
    return found

if __name__=="__main__":
    shopping = ["tshirts", "shoes","pants","socks"]
    print("Welcome to our friendly store.")
    print("In-stock now: ")
    print(shopping)
    item = input("What would you like to get today? ")
    isitFound = linearSearch(item, shopping)
    if isitFound:
        print(item +" were added to cart.")
    else:
        print(iterm +" are not in store.")