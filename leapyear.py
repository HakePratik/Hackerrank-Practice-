def leap(year):
    if 1900<=year<=10**5:
        if (year%4==0 and year%100!=0) or year%400==0:
            print ("True, This is leap year")
        else:
            print ("False, this is not leap year")
year=leap(int(input("enter year=")))