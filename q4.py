# Twowaits
Twowaits Problem
cp=int(input("Enter the cost price of the product"))
sp=int(input("Enter the selling price of the product"))
profit=(sp-cp)/cp*100
print("Profit generated is ",profit,"%")
newsp=(profit+5)*100/cp+cp
print("Selling price after 5% increase in profit is ",newsp)
