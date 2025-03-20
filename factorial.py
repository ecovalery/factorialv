def factorial (a):
  if a == 0 or a == 1:
    return 1
  else:
    return a * factorial(a-1)
a=int(input("ingrese valor: "))
print("el factorial del valor es:", factorial (a))