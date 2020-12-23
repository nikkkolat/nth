import datetime
name = input("Spring Roll Chicken: ")

name2 = input("Spring Roll Prawn: ")

name3 = input("Spring Roll Duck: ")

name4 = input("Samosa Vagetable: ")

name5 = input("Samosa Chicken: ")

name6 = input("Money Bag Prawn: ")

name7 = input("Japanese Gyoza Prawn: ")

name8 = input("Japanese Gyoza Pork: ")




f = open("niko.txt", "a")
now = datetime.datetime.now()
f.write("<===========" + now.strftime("%A-%d-%m-%y") + "===========>" + "\n")


f.write("Spring Roll Chicken ========> " + str(name) + "\n")
f.write("Spring Roll Prawn   ========> " + str(name2) + "\n")
f.write("Spring Roll Duck    ========> " + str(name3) + "\n")
f.write("Samosa Vagetable    ========> " + str(name4) + "\n")
f.write("Samosa Chicken      ========> " + str(name5) + "\n")
f.write("Money Bag Prawn     ========> " + str(name6) + "\n")
f.write("Japanese Gyoza Prawn  ======> " + str(name7) + "\n")

print("<===========",now.strftime("%A-%d-%m-%y"),"===========>" )


print('Spring Roll Chicken ========>',name)
print("Spring Roll Prawn   ========>",name2)
print("Spring Roll Duck    ========>",name3)
print("Samosa Vagetable    ========>",name4)
print("Samosa Chicken      ========>",name5)
print("Money Bag Prawn     ========>",name6)
print("Japanese Gyoza Prawn  ======>",name7)
print("Japanese Gyoza Pork   ======>" ,name8)
f.close()
f.close()