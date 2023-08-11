QUESTION 2:
print("\n\t\tCHECKING A YEAR IS LEAP IS NOT :)\n")
year=int(input("\nplease enter a year , you want to check : "))
 if year%4==0 :
   if year%100==0:
     if year%400==0:
       print("\nthis is leap year :)")
     else:print("\nthis is not leap yaer")
   else:print("\nthis is  leap year")   
 else:print("\n this is not leap year :(")