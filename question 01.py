QUESTION :01
print("checking number range")
num=int(input("enter a number :\n"))
if num>0 and num<=10:
  print(f"\n{num} is in low range")
elif num>10 and num<=50:
  print(f"\n{num} is in medium range")
elif num>51 and num<=100 :
  print(f"\n{num} is in high range")
else:
  print(f"\n{num} is out of range")
  