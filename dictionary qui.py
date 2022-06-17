meaning = {"Hell": "jahanum",
           "Paradise": "Jannah",
           "light": "{ noor, roshni}",
           "Praise": "Tareef"}
print("Hell \nParadise \nlight \nPraise")
print("please enter a word from the Given above  Four words only:")

value = input()
print(meaning.get(value, "Not Found"))
