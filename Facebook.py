print("creat new facebook account")
name =input("entet the name ")
if name>="a" and name<="z"or name>="A" and name<="Z":
    print(name)
    last_name=input("enter the  last_name")
    if last_name>="a" and last_name<="z" or last_name>="A" and last_name>="Z":
        print(last_name)
        birth_date=int(input("entet the birth_date"))
        if birth_date>=1 and birth_date<=31:
            print("birth_date") 
            month=int(input("enter the month"))
            if month>=1 and month<=12:
                print("month")
                year=int(input("entet the year"))
                if year>=1000 and year<=year<=9999:
                    print("year")
                    print(birth_date,"-",month,"-",year)
                    gender=input("enter the gender")
                    if gender=="male" or gender=="femal":
                        print(gender)
                        print("next")
                        mo_no=int(input("enter the mo_number"))
                        if mo_no>=1000000000 and mo_no<=10000000000:
                            print("mo number")
                            password=int(input("enter the password"))
                            if password>=100000 and password<=1000000 :
                                print(password)
                                print("cleck next")
                                OTP=int(input("enter the otp"))
                                if OTP>=100 and OTP<=1000:
                                    print("signup")
                                    print("creating your account")
                                else:    
                                    print("invalid")
                            else:
                                print("invalid")
                        else:
                            print("invalid")
                    else:
                        print("invalid")
                else:
                    print("invalid") 
            else:
                print("invalid")        
        else:
            print("invalid") 
    else:
        print("invalid")  
                                                   
