#Diego Espinola
#04.12.2020
#second part of the exam, the drive.
from Seacrh_Methods import bubble_sort
from Seacrh_Methods import selection_sort
from Seacrh_Methods import insertion_sort
from Seacrh_Methods import merge_sort
from Seacrh_Methods import quick_sort

list = []
method = 0
print("Welcome to this program, this program will let you type any random list of numbers you have and it will"
      " organized the list for you")

while method != 6:
      print("Lets start by asking you what method do you want yo use? Here are you options please type "
      "the number of the method you want to use")
      print("1 = bubble sort")
      print("2 = selection sort")
      print("3 = insertion sort")
      print("4 = merge  sort")
      print("5 = quick sort")
      print("6 = Exit the program")
      method = int(input(">"))

      if method == 1:
            num = int(input("How many numbers do you want to add? \n>"))
            for n in range(num):
                  numbers = int(input("Enter number:"))
                  list.append(numbers)
                  bubble_sort(list)
                  print(f"Here is your list sorted:{list}")
            list.clear()


      if method == 2:
            num = int(input("How many numbers do you want to add? \n>"))
            for n in range(num):
                  numbers = int(input("Enter number:"))
                  list.append(numbers)
                  selection_sort(list)
                  print(f"Here is your list sorted:{list}")
            list.clear()

      if method == 3:
            num = int(input("How many numbers do you want to add? \n>"))
            for n in range(num):
                  numbers = int(input("Enter number:"))
                  list.append(numbers)
                  insertion_sort(list)
                  print(f"Here is your list sorted:{list}")
            list.clear()

      if method == 4:
            num = int(input("How many numbers do you want to add? \n>"))
            for n in range(num):
                  numbers = int(input("Enter number:"))
                  list.append(numbers)
                  merge_sort(list)
                  print(f"Here is your list sorted:{list}")
            list.clear()
      if method == 5:
            num = int(input("How many numbers do you want to add? \n>"))
            for n in range(num):
                  numbers = int(input("Enter number:"))
                  list.append(numbers)
                  quick_sort(list)
                  print(f"Here is your list sorted:{list}")
            list.clear()
      if method == 6:
            print("Bye bye")

