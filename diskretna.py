import random
import matplotlib.pyplot as plt
import statistics
import math
from tkinter import *
import pylab

def draw_diagram(numbers2):
    x = range(len(numbers2))
    ax = plt.gca()
    plt.xlabel("Xi")
    plt.ylabel("Ni")
    ax.bar(x, numbers2.values(), align='edge')
    ax.set_xticks(x)
    ax.set_xticklabels(numbers2.keys())

def draw_empiric(numbers2):
    x = range(len(numbers2))
    ax = plt.gca()
    ax.bar(x, numbers2.values(), align='edge')
    ax.set_xticks(x)
    ax.set_xticklabels(numbers2.keys())

def draw_polygon(numbers, a, b):
    plt.xlabel("Xi")
    plt.ylabel("Ni")
    values = [i for i in range(a, b+1)]
    quantities = [0 for i in range(a, b+1)]
    for value in numbers:
     quantities[values.index(value)] += 1
    plt.plot(values, quantities)

def search_quantili(numbers2):
    n = len(numbers2)
    res = []
    if n%4 == 0: #kvartil
        kvartil = []
        for i in range(1, 4):
            kvartil.append(numbers2[int(i*n/4)-1])
        print("Inter kvartil=", kvartil[len(kvartil)-1]-kvartil[0])
        print(kvartil)
        res.append(kvartil[len(kvartil)-1]-kvartil[0])
        res.append(kvartil)

    if(n%10 == 0): #Decil
        decil = []
        for i in range(1, 10):
            decil.append(numbers2[int(i*n/10)-1])
        print("Inter decil=", decil[len(decil)-1]-decil[0])
        print(decil)
        res.append(decil[len(decil)-1]-decil[0])
        res.append(decil)
    if(n%100 == 0): #centil
        centil = []
        for i in range(1, 100):
            centil.append(numbers2[int(i*n/100)-1])
        print("Inter centil=", centil[len(centil)-1]-centil[0])
        print(centil)
        res.append(centil[len(centil)-1]-centil[0])
        res.append(centil)

    if(n%1000 == 0 ): #milililililililili...
        mililili = []
        for i in range(1, 1000):
            mililili.append(numbers2[int(i*n/1000)-1])
        print("Inter mililili5=", mililili[len(mililili)-1]-mililili[0])
        print(mililili)
        res.append(mililili[len(mililili)-1]-mililili[0])
        res.append(mililili)
    return res
def search_mediana(numbers):
    index = len(numbers)//2
    if len(numbers)%2==0:
        mediana = (numbers[index]+numbers[index+1])//2
    else:
        mediana = numbers[index]
    return mediana

def search_mod(numbers):
    value_list = list(numbers)
    return max([(value_list.count(x),x) for x in set(value_list)]) #return the last value

def search_mid_value(numbers1):
    sum = 0
    for i in numbers1:
        sum+=i
    sum = sum / len(numbers1)
    return sum

def search_rozmax(numbers):
    min_value = min(numbers.keys())
    max_value = max(numbers.keys())
    return max_value-min_value

def search_variance(numbers):
    dev = statistics.variance(numbers)
    return dev

def start_moments(numbers2, n):
    moments = []
    for k in range(0, 4):
        sum = 0

        for i, j in numbers2.items():
            sum+=j*(i**(k+1))
        sum /= n
        moments.append(sum)
    return moments

def moments(moments):
    Moments = []
    M2 = moments[1] - (moments[0]**2)
    M3 = moments[2] - 3*moments[1]*moments[0] + 2*(moments[0]**3)
    M4 = moments[3] - 4*moments[2]*moments[0] + 6*moments[1]*(moments[0]**2) + 3*(moments[0]**4)
    Moments.append(M2)
    Moments.append(M3)
    Moments.append(M4)
    return Moments

def asimetriya(Moments):
    A = Moments[1]/(Moments[0]**(3/2))
    return A

def exces(Moments):
    E = (Moments[2]/(Moments[0]**2)) - 3
    return E

def emphirichna_funcziya(numbers2, n):
    sum = 0
    dictionary = dict()
    temp = 0
    id = 0
    for i, j in numbers2.items():
        if id == 0:
            dictionary.update({'0':f"x<{i}"})
            id += 1
        else:
            dictionary.update({f"{sum}/{n}":f"{temp}<=x<{i}"})
        sum+=j
        if sum == n:
            dictionary.update({'1':f"x>={i}"})
        temp = i
    return dictionary
numbers1=[]
numbers2={}
start1 = 0
end1 = 0

def rozpodil_Puassona(numbers2, sum):
    pi = 0
    arr = []
    for i in range(1,len(numbers2)+1):
        pi=(math.pow(sum,i)*math.pow(math.e,(-sum)))/math.factorial(i)
        arr.append(pi)
    return arr

def NPI(pi,N):
    result = []
    for p in pi:
        result.append(N*p)
    return result

# def NPI_check(numbers2,npi):
#     result = []
#     for i in npi:
#         if(len(numbers2.values()) < 5 or i <= 10):
#             result.append(i+(i+1))
#         else:
#             result.append(i)
#     return result

def x2_empir(numbers2,npi):
    sum = 0
    for i,j in zip(numbers2.values(),npi):
        sum += (math.pow((i-j),2)/j)
        print("i = ",i,"j = ", j, "sum = ",sum)
    return sum

def x2_kritic(numbers2, num):
    n = len(N) - 1
    res = 0
    list1 = [6.6, 9.2, 11.3, 13.3, 15.1, 16.8, 18.5, 20.1, 21.7, 23.2]
    list2 = [3.8, 6.0, 7.8, 9.5, 11.1, 12.6, 14.1, 15.5, 16.9, 18.3]
    if (num == 0.01):
        if (n > len(list1)):
            res = print("Кількість частот більша за 10")
        else:
            res = list1[n]
    elif (num == 0.05):
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

def run(start, end, amount, accuracy):
    global numbers1, numbers2, start1, end1
    start1 = start
    end1=end
    numbers1 = [random.randint(start, end) for i in range(amount)]
    numbers1.sort()
    numbers2 = dict((i, numbers1.count(i))for i in numbers1)
    print("Variaziyniy ryad =",numbers1)
    print("Diskretniy stat rospodil =",numbers2)
    result = []
    result.append(numbers2)
    mediana = search_mediana(numbers1)
    print("Mediana =", mediana)
    result.append(mediana)
    moda = search_mod(numbers1)[1]
    result.append(moda)
    print("Moda =", moda)
    average = search_mid_value(numbers1)
    result.append(average)
    print ("Mid value =", average)
    rozmah = search_rozmax(numbers2)
    result.append(rozmah)
    print("Rozmah =", rozmah)
    deviazia = search_variance(numbers1) * (len(numbers1)-1)
    print("Deviazia =",deviazia)
    result.append(deviazia)
    variance =  search_variance(numbers1)
    result.append(variance)
    print("Variance =", variance)
    standard = math.sqrt(search_variance(numbers1))
    result.append(standard)
    print("Standard =", standard)
    dispercy = deviazia/len(numbers1)
    result.append(dispercy)
    print("Dispercy =", dispercy)
    variazia = standard/average
    result.append(variazia)
    print("Variazia =", variazia)
    # print(numbers1)
    result.append(search_quantili(numbers1))
    start_mom = start_moments(numbers2, len(numbers1))
    print("Start moments =", start_mom)
    result.append(start_mom)
    Mom = moments(start_mom)
    print("Average moments =", Mom)
    result.append(Mom)
    asimetryya = asimetriya(Mom)
    print("Asimetriya =", asimetryya)
    result.append(asimetryya)
    eksces = exces(Mom)
    print("Exces =", eksces)
    result.append(eksces)
    result.append(emphirichna_funcziya(numbers2, len(numbers1)))
    print(emphirichna_funcziya(numbers2, len(numbers1)))
    result.append(emphirichna_funcziya(numbers2, len(numbers1)))
    print("Rozpodil Puasson =", rozpodil_Puassona)
    result.append(rozpodil_Puassona(numbers2, average))
    npi = NPI(rozpodil_Puassona(numbers2, average), len(numbers1))
    print("Npi =", npi)
    result.append(npi)
    x2_empirichna = x2_empir(numbers2,npi)
    print("Empirichna =",x2_empirichna)
    result.append(x2_empirichna)
    x2_kritichna = x2_kritic(numbers2, accuracy)
    print("Kritichna =", x2_kritichna)
    result.append(x2_kritichna)
    checking = check(x2_empirichna, x2_kritichna)
    print("Check =", checking)
    result.append(checking)
    return result

def draw():
    pylab.subplot(2,2,1)
    draw_diagram(numbers2)
    pylab.subplot(2,2,2)
    draw_polygon(numbers1, start1, end1)
    pylab.subplot(2,2,3)
    draw_empiric(emphirichna_funcziya(numbers2, len(numbers1)))
    pylab.show()

if __name__ == "__main__":
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the finishing number: "))
    amount = int(input("Enter the amount of numbers: "))
    accuracy = float(input("Enter the accuracy: "))
    numbers1 = [random.randint(start, end) for i in range(amount)]
    numbers1.sort()
    numbers2 = dict((i, numbers1.count(i))for i in numbers1)
    print("Variaziyniy ryad =",numbers1)
    print("Diskretniy stat rospodil =",numbers2)
    mediana = search_mediana(numbers1)
    print("Mediana =", mediana)
    moda = search_mod(numbers1)[1]
    print("Moda =", moda)
    average = search_mid_value(numbers1)
    print ("Mid value =", average)
    rozmah = search_rozmax(numbers2)
    print("Rozmah =", rozmah)
    deviazia = search_variance(numbers1) * (len(numbers1)-1)
    print("Deviazia =",deviazia)
    variance =  search_variance(numbers1)
    print("Variance =", variance)
    standard = math.sqrt(search_variance(numbers1))
    print("Standard =", standard)
    dispercy = deviazia/len(numbers1)
    print("Dispercy =", dispercy)
    variazia = standard/average
    print("Variazia =", variazia)
    # print(numbers1)
    search_quantili(numbers1)
    start_mom = start_moments(numbers2, len(numbers1))
    print("Start moments =", start_mom)
    Mom = moments(start_mom)
    print("Average moments =", Mom)
    asimetryya = asimetriya(Mom)
    print("Asimetriya =", asimetryya)
    eksces = exces(Mom)
    print("Exces =", eksces)
    emphirichna_funcziya(numbers2, len(numbers1))
    Puasson = rozpodil_Puassona(numbers2, average)
    print("Rozpodil Puasson =", rozpodil_Puassona)
    npi = NPI(rozpodil_Puassona(numbers2, average), len(numbers1))
    print("Npi =", npi)
    x2_empirichna = x2_empir(numbers2,npi)
    print("Empirichna =",x2_empirichna)
    x2_kritichna = x2_kritic(numbers2, accuracy)
    print("Kritichna =", x2_kritichna)
    checking = check(x2_empirichna, x2_kritichna)
    print("Check =", checking)