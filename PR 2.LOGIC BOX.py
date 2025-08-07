print("welcome to the pattern Generator and Number Analyzer!")
print()

print()
print(" select an option:")
print("1. Right-angled Triangle")
print("2. Pyramid")
print("3. Left-angled Triangle")
print("4. Analyze a range of numbers")
print()

X= int(input("Enter your chocice:"))
while X<4:
  Y=int(input("Enter the number for the pattern:"))

  if X==1:
    for i in range(1, Y):
      for j in range(i):
          print("*", end="")
      print()
  


  elif X==2:
    for i in range(1, Y + 1):
      spaces = Y - i
      stars = 2 * i - 1
      print(" " * spaces + "*" * stars)
      print()
 


  elif X==3:
    for i in range(1, Y + 1):
      print(" " * (Y - i) + "*" * i)
      print()

  break


while X==4:

  A=int(input("enter the start of the range:"))
  B=int(input("enter the end of range:"))

  for i in range (A,B + 1):
    print("number",i,"is Odd" if i%2==1 else "is Even")
  print("sum of all numbers from",A, "To" ,B, "is:",sum (range(A,B + 1)))

  break
        
              
        
      
    


          













