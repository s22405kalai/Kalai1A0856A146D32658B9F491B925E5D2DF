#To find the leap or not using if,elif and else.
n=int(input("Enter the year to find leap year or not: "))
if n==0:
  print(n,"is not a year")
elif(n%4==0):
  print(n,"The year is an leap year")
else:
  print(n,"The year is not an leap year")