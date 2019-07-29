def credit_check():

    i = input("enter number :")
    list1=[]
    list2=[]
    list3=[]
    global l
    l=0

    for j in i:
        list1.append(j)

    for j in list1[0::2]:
      list2.append(j)


    for j in list1[1::2]:
       list3.append(j)

    for k in list2[0::1]:
        a = int(k)*2
        if a>=10:
           k = a%10
           k = k+1
           l = l+k
        else:
           l = l+a


    for j in list3[0::1]:
        l = l+int(j)

    while True:
        print(l)
        if l%10 !=0:
            print("invalid")
            credit_check()

        elif int(list1[0]) == 4:
                print("Visa")
                break

        elif int(list1[0]) == 5 and int(list1[1]) >=1 and  int(list1[1]) <=5 :
                print("MasterCard")
                break

        elif  int(list1[0]) == 3 and int(list1[1]) == 4 or  int(list1[1]) == 7 :
                print("Amex")
                break


        else:
            print("invalid")
            credit_check()


credit_check()


