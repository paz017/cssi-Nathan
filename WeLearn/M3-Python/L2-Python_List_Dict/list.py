# students = ["Alice" , "Javi" , "Damien"]
# students.append("Delilah")
# print(students)
#
# students = ["Alice" , "Javi" , "Damien"]
# students.insert(1, "Zoe")
# print(students)
#
# students = ["Alice" , "Javi" , "Damien"]
# students.remove("Javi")
# print(students)
#
# # my_list.insert(index, element)
#
# smith_siblings = ["Emily" , "Monique" , "Giovanni"]
# for name in smith_siblings:
#     print(name + " Smith")
#
# smith_siblings = ["Emily" , "Monique" , "Giovanni" , "Brianna" , "Jabi"]
# for name in smith_siblings:
#     print(name + " Smith")
#
# smith_siblings = ["Emily" , "Monique" , "Giovanni" , "Brianna" , "Jabi"]
# for index in range(len(smith_siblings)):
#     smith_siblings[index] = smith_siblings + "Smith"
# print(smith_siblings)

# superheros = ["Captain Marvel" , "Wonder Woman" , "Storm" , "Kamala Khan" , "Bumblebee" , "Jessica Jones"]
#
# demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5"))
#
# if demoted_hero in superheros:
#     superheros.remove(demoted_hero)
#     print("Top 5 heroes:" , superheros)
# else:
#     print("Hero not found.")

names = ["Rickon" , "Bran" , "Arya" , "Sansa" , "Jon" , "Robb"]
names[::-1]
names[4:2:-1]
print(names[::-1])
print(names[4:2:-1])
print(names[:2])
print(names[::2])
