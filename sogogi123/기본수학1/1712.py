fixedFee,productionFee,price =map(int,input().split())
if productionFee >= price:
    print(-1)
else:
    print(fixedFee//(price-productionFee)+1)
