

#it will count the letters in the word
arr = "bananas"
a= 0
while a < len(arr):
    print("Num:",a,arr[a], 'seq')
    a= a+1

fruit = 'Banana is a cheap fruit \n Hello the'
fruit = fruit.splitlines()
print(fruit)
fruit[0] = 'b'
print(fruit, '->>Length is :', len(fruit))