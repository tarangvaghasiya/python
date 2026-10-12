# section - A

for i in range(1, 5):
    if i == 1:
        break
    print(i)

print("End")

#output
    #END

for i in range(1, 7):
    print(i)
    if i == 4:
        break
print("Finished")

#output
    #1
    #2
    #3
    #Finished

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#output
    #1
    #2
    #4
    #5


for i in range(1, 5):
    if i == 2:
        pass
    print(i)

#output
    #1
    #2
    #3
    #4
    #5

for i in range(3):
    print("Python")
else:
    print("Done")

#output
    #python
    #python
    #python
    #done

