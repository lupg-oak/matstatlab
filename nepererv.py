import random
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import stats
import statistics
import math


def moda(X, N):
     mods = []
     maxN= max(N)
     for i in range(len(N)):
         if(N[i] == maxN):
             index = i
             if(index == 0):
                 prev = 0
             else:
                 prev = N[index-1]
             if index == len(N)-1:
                 next = 0
             else:
                 next = N[index+1]
             mod = X[index][0] + ((X[index][1]-X[index][0])*(N[index]-prev))/((N[index]-prev)+(N[index]-next))
             mods.append(mod)
     return mods

def mediana(X, N):
    average = sum(N)/2
    tempsum = 0
    index = 0
    for i in range(len(N)):
        tempsum+=N[i]
        if(tempsum >= average):
            index = i
            break
    tempsum -= N[index]
    med = X[index][0]+(X[index][1]-X[index][0])*(0.5*sum(N)-tempsum)/N[index]
    return med

def draw_diagram(keys, values):
    x = range(len(keys))
    ax = plt.gca()
    plt.xlabel("Xi")
    plt.ylabel("Ni")
    ax.bar(x, values, align='edge')
    ax.set_xticks(x)
    keys2 = [round(((keys[i][0]+keys[i][1])/2), 2) for i in range(len(keys))]
    ax.set_xticklabels(keys2)
    plt.show()

def average_value(N, Z):
    sumN=0
    for i in N:
        sumN += i
    sum = 0
    for i in range(len(N)):
        sum+= N[i]*Z[i]
    sum /= sumN
    return sum

def deviazia(N, Z):
    average = average_value(N, Z)
    result = 0
    for i in range(len(N)):
        result += N[i]*((Z[i]-average)**2)
    return result

def varianza(dev, N):
    sumN=0
    for i in N:
        sumN += i
    return dev/(sumN-1)

def standart(vari):
    S = math.sqrt(vari)
    return math.fabs(S)

def variaziya(stand, average):
    V = stand/average
    return V

def dispersiya(dev, N):
    sumN = 0
    for i in N:
        sumN += i
    return dev / sumN

def momenty(N, Z, average):
    moments = []
    sum = 0
    #check
    for i in range(0, 4):
        sum += N[i]*((Z[i]-average)**i)
        moments.append(sum)
    return moments

#def asimetriya(moments):

def excess(moments):
    excess = (moments[3]/(moments[1]**2))-3
    return excess

def asymetria(moments):
    asymetria = moments[2]/(moments[1]**1.5)
    return  asymetria

def Inter(n, a, b):
    r=0
    while(not((2**r<n) and (n<2**(r+1)))):
        r+=1
    return (b-a)/r

def Exponent_rozpodil(keys,average):
    first = []
    second = []
    lyambda = 1/average
    result = []
    for i in keys:
        first.append(i[0])
        second.append(i[1])
    print("first",first)
    print("second",second)
    for f,s in zip(first,second):
        E1 = (-lyambda) * f
        E2 = (-lyambda) * s
        F = math.pow(math.e,E1)
        S = math.pow(math.e,E2)
        result.append(F - S)
    return result

def NPI(pi, N):
    result = []
    sumN = 0
    for i in N:
        sumN += i
    for p in pi:
        result.append(sumN*p)
    return result

def x2_empir(N,npi):
    sum = 0
    for i,j in zip(N,npi):
        sum += (math.pow((i-j),2)/j)
    return sum

def x2_kritic(N, num):
    n = len(N) - 1
    res = 0
    list1 = [6.6, 9.2, 11.3, 13.3, 15.1, 16.8, 18.5, 20.1, 21.7, 23.2]
    list2 = [3.8, 6.0, 7.8, 9.5, 11.1, 12.6, 14.1, 15.5, 16.9, 18.3]
    if(num == 0.01):
        if(n > len(list1)):
            res = print("Кількість частот більша за 10")
        else:
            res = list1[n]
    elif(num == 0.05):
        if (n > len(list2)):
            res = print("Кількість частот більша за 10")
        else:
            res = list2[n]
    else:
        res = print("Ви можете ввести тільки значення '0.01' та '0.05'")
    return res

def check(empir, kritic):
    res = ""
    if(empir < kritic):
        res = "Підтверджено => ( X емпіричне < X критичне )"
    else:
        res = "Не підтверджено => ( X емпіричне > X критичне )"
    return res


def runstat(start, end, amount, accuracy):
    numbers1 = [random.uniform(start, end) for i in range(amount)]
    numbers1.sort()
    print(numbers1)
    inter =Inter(len(numbers1), numbers1[0], numbers1[len(numbers1)-1])
    keys = []
    a = start
    while(a+inter < end):
        keys.append((a, a+inter))
        a=a+inter
    keys.append((a, end))
    values = [0 for i in range(len(keys))]
    for i in numbers1:
        for j in range(len(keys)):
            if i >=keys[j][0] and i < keys[j][1]:
                values[j] += 1
    index = [0 for i in range(len(keys))]
    for i in range(len(keys)):
        index[i] = (keys[i][0]+keys[i][1])/2
    print("Ряд:", numbers1)
    result = []
    print("X:", keys)
    result.append(keys)
    print("N:", values)
    result.append(values)
    print("Z:", index)
    result.append(index)
    mod = moda(keys, values)
    result.append(mod)
    print("Moda =", mod)
    med = mediana(keys, values)
    result.append(med)
    print("Mediana =", med)
    average = average_value(values, index)
    result.append(average)
    print("Average: ", average)
    #print("Roz: ", numbers1[len(numbers1)-1][1] - numbers1[0][0])
    deviaciya = deviazia(values, index)
    print("Deviazia: ",deviaciya)
    result.append(deviaciya)
    variansa = varianza(deviaciya, values)
    result.append(variansa)
    print("Varinsa =", variansa)
    stand =  standart(variansa)
    print("Standart =", stand)
    result.append(stand)
    variaciya = variaziya(stand, average)
    result.append(variaciya)
    print("Variaziya =", variaciya)
    dispersy = dispersiya(deviaciya, values)
    result.append(dispersy)
    print("Dispersiya =", dispersy)
    moments = momenty(values, index, average)
    result.append(moments)
    print("Momenty =", moments)
    exce = excess(moments)
    print("Ekszess =",excess(moments))
    result.append(exce)
    asym = asymetria(moments)
    result.append(asym)
    print("Asymetria =", asymetria(moments))
    result.append(keys)
    result.append(values)
    exponent = Exponent_rozpodil(keys,average)
    print("Exponent rozpodil =", exponent)
    result.append(exponent)
    npi = NPI(exponent,values)
    print("Npi =",npi)
    result.append(npi)
    x2_empirichna = x2_empir(values,npi)
    print("Empirichna =",x2_empirichna)
    result.append(x2_empirichna)
    x2_kritichna = x2_kritic(values, accuracy)
    print("Kritichna =", x2_kritichna)
    result.append(x2_kritichna)
    checking = check(x2_empirichna, x2_kritichna)
    print("Check =", checking)
    result.append(checking)
    return result

def drawa(keys, values):
    draw_diagram(keys, values)
#def empirychna(X, N, Z):
    #sumN=0
    #for i in N:
     #   sumN += i
    #dictionary = dict()
    #id = 0
    #for i in range(len(N)):
        #if id == 0:
         #   dictionary.update({'0':f"x<={X[0][0]}"})
        #    id += 1
       # else:
      #      dictionary.update({f"{(N[i]*'')/(sumN*(X[i][1]-X[i][0]}"})

if __name__ == '__main__':
    start = float(input("Enter the starting number: "))
    end = float(input("Enter the finishing number: "))
    amount = int(input("Enter the amount of numbers: "))
    accuracy = float(input("Enter the accuracy"))
    numbers1 = [random.uniform(start, end) for i in range(amount)]
    numbers1.sort()
   # print(numbers1)
    inter =Inter(len(numbers1), numbers1[0], numbers1[len(numbers1)-1])
    keys = []
    a = start
    while(a+inter < end):
        keys.append((a, a+inter))
        a=a+inter
    keys.append((a, end))
    values = [0 for i in range(len(keys))]
    for i in numbers1:
        for j in range(len(keys)):
            if i >=keys[j][0] and i < keys[j][1]:
                values[j] += 1
    index = [0 for i in range(len(keys))]
    for i in range(len(keys)):
        index[i] = (keys[i][0]+keys[i][1])/2
   # print("Ряд:", numbers1)
    print("X:", keys)
    print("N:", values)
    print("Z:", index)
    average = average_value(values, index)
    print("Average: ", average)
    #print("Roz: ", numbers1[len(numbers1)-1][1] - numbers1[0][0])
    deviaciya = deviazia(values, index)
    print("Deviazia: ",deviaciya)
    variansa = varianza(deviaciya, values)
    print("Varinsa =", variansa)
    stand =  standart(variansa)
    print("Standart =", stand)
    variaciya = variaziya(stand, average)
    print("Variaziya =", variaciya)
    dispersy = dispersiya(deviaciya, values)
    print("Dispersiya =", dispersy)
    moments = momenty(values, index, average)
    print("Momenty =", moments)
    draw_diagram(keys, values)
    mod = moda(keys, values)
    print("Moda =", mod)
    med = mediana(keys, values)
    print("Mediana =", med)
    print("Ekszess =",excess(moments))
    print("Asymetria =", asymetria(moments))
    exponent = Exponent_rozpodil(keys, average)
    print("Exponent rozpodil =", exponent)
    npi = NPI(exponent,values)
    print("N*pi =", npi)
    x2_empirichna = x2_empir(values,npi)
    print("Empirichna =", x2_empirichna)
    x2_kritichna = x2_kritic(values, accuracy)
    print("Kritichna =", x2_kritichna)
    checking = check(x2_empirichna, x2_kritichna)
    print("Check =", checking)