list1 = []
while True:
  print ("To Do List")
  print ("1. View Tasks")
  print ("2. Add Tasks")
  print ("3.Remove Tasks")
  print ("4.Exit")
  print("5.Edit a Task")
  selection = int(input("Choose your option 1-5 "))

  if selection == 1:
    if len(list1) ==0:
      print("List Empty")
    else:
      for i in list1:
        print (i)

  elif selection ==2:
   task = input("Add Your Task ") 
   list1.append(task)
   print ("Task " + task+ " added! ")

  elif selection ==3:
    task = input("What Task do you want to delete ")
    if task in list1:
      list1.remove(task)
      print("Task " +task+ " removed! ")
    else:
      print("Not in the list")
    

  elif selection ==4:
    print("Exiting the app")
    break

  elif selection ==5:
    if len(list1)==0:
      print("No task to edit")
    else:
     taskedit = input("What task to edit ") 
     index1 = list1.index(taskedit)
     updated = input("Enter the data task ")
     list1[index1] = updated
     print ("task updated") 

