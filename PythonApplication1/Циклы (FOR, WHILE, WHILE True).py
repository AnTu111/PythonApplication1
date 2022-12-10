#ulesanne 1:вводят 15 чисел. определить, сколько среди них целых.
j=0
for i in range(0,15,1):#range (15)
    a=float(input(f"{i+1} sisesta a : "))
    if int(a)==a:
        j+=1
print(j)
     

    

#ulesanne 2: запросите у пользователя число а и найдите сумму всех натуральных чисел от 1 до а.
numbera=int(input("введите число а: "))
x=0
for i in range(1,numbera+1):
    x+=i
print(x)


#ulesanne 3: вводят 8 чисел. найти их произведение (только положительных).
j=1
for i in range(8):
    a=float(input(f"{i+1} sisesta number : "))
    j*=a
print(j)




#ulesanne 4:составьте программу, выводящую на экран квадраты чисел от 10 до 20.
for i in range(10,21):
    print(i**2)




#ulesanne 8:составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры (1 дюйм =
2,5 см) для значений длин от 1 до 20 дюймов.
for i in range(1,21):
    print(i,"inches = ",i*2.5,"cm")




#ulesanne 13.найти все натуральные числа от 100 до 1000 кратные 7. и посчитать их колличество и сумму.
amount=0
summ=0
for i in range(100,1001):
    if i%7==0:
        amount+=1
        summ+=i
print("колличество = ",amount , ",а сумма = ", summ)



        


#ulesanne 15:написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
for r in range(10):
    for i in range(10):
        print(i,end=" ",)
    print()



#ulesanne 16:напишите программу, печатающую столбик строк такого вида:
for r in range(9):
    for c in range(9):
        if r==c:
            print(r+1, end=" ")
        else:
            print(0, end=" ")
        print(0,end=" ")
    print()#строка закончилась



#ulesanne 17.напишите программу, печатающую столбик таблицу умножения такого вида:
for i in range(1,10):
  print(2,"*",str(i)+"=" + str(i*2),sep="")



#ulesanne 12:.в бригаде, работающей на уборке сена, имеется n сенокосилок.
первая сенокосилка работала m часов, а каждая следующая на 10 минут больше, чем предыдущая.
сколько часов проработала вся бригада?
n=int(input("kogus: "))
m=int(input("min: "))
m=m*60
summa=0
for i in range(1,n):
    summa+=m
    m=m+10
print("kokku nad töötavad:",summa/60)




#ulesanne 10:ввести с клавиатуры 10 пар чисел.  сравнить числа в каждой паре и напечатать большие из них.
from random import*
for i in range(1,11):
    arv1=randint(-100,100)
    arv2=randint(-100,100)
    if arv1>arv2:
        print(f"{arv1} on surem kui {arv2}")
    elif arv2>arv1:
        print(f"{arv2} on surem kui {arv1}")
    else:
        print(f"{arv1}, {arv2} on võrdsed")






    
