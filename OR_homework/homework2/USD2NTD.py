def usdtontd(x):
    x = x*30
    return x

usd = int(input("Please enter currency in USD:"))

print ("The equivalent NTD is :"+''+str(usdtontd(usd)))