from tkinter import *
from tkinter import Scale, Tk, Frame, Label, Button
from tkinter.ttk import Notebook
import diskretna
from nepererv import *
from nepererv import drawa
import nepererv

root = None
hello_label = None
start_label = None
start_box = None
end_label = None
end_box = None
amount_label = None
amount_box = None
accuracy_label = None
accuracy_box = None
button_add = None

def main_window():
    global root, hello_label
    root = Tk()
    root.title("Main")
    root.geometry("400x400+400+400")
    menubar = Menu(root)
    filemenu = Menu(menubar)
    filemenu.add_command(label="Дискретна", command=descrete)
    filemenu.add_command(label="Неперервна", command=nepererv)
    filemenu.add_command(label="Розподіл Пуассона", command=creating_table_Puasson)
    filemenu.add_command(label="Експонентний розподіл", command=creating_table_Exponent)
    menubar.add_cascade(label="Обрати", menu=filemenu)
    menubar.add_cascade(label="Вийти", command=root.destroy)
    hello_label = Label(root, text="Щоб продовжити натисніть Обрати\n Щоб завершити натисніть Вийти", font = "Helvetica 15 bold")
    hello_label.pack()
    root.config(menu=menubar)
    root.mainloop()


def descrete():
    global root, start_label, start_box, end_label, end_box, amount_label, amount_box, button_add
    root = Tk()
    root.geometry("720x600+300+300")
    start_label = Label(root, text="Старт: ", font = "Helvetica 15 bold")
    start_box = Entry(root)
    start_label.place(x=3, y=3)
    start_box.place(x=200, y=3)

    end_label = Label(root, text="Кінець: ", font = "Helvetica 15 bold")
    end_box = Entry(root)
    end_label.place(x=3, y=30)
    end_box.place(x=200, y=30)

    amount_label = Label(root, text="Кількість: ", font = "Helvetica 15 bold")
    amount_box = Entry(root)
    amount_label.place(x=3, y=60)
    amount_box.place(x=200, y=60)

    button_add = Button(root, text="Генерувати", command=run_descrete_button_pushed, font = "Helvetica 15 bold")
    button_add.place(x=10, y=100)


def run_descrete_button_pushed():
    global root, start_box, end_box, amount_box
    start = str(start_box.get())
    end = str(end_box.get())
    amount = str(amount_box.get())
    start = int(start)
    end = int(end)
    amount = int(amount)
    results = diskretna.run(start, end, amount)
    info = Label(root, text="Ряд:\n Частоти: ")
    info.place(x=10, y=140)

    resinfo = []
    for i in results[0].keys():
        resinfo.append(i)
    res_info = Label(root, text=str(resinfo))
    res_info.place(x=140, y=140)
    resinfo = []
    for i in results[0].values():
        resinfo.append(i)
    second_info = Label(root, text=str(resinfo))
    second_info.place(x=140, y=160)

    mediana = results[1]
    mediana_label = Label(root, text=str("Медіана: " + str(mediana)))
    mediana_label.place(x=10, y=190)
    moda = Label(root, text=str("Мода: " + str(results[2])))
    moda.place(x=100, y=190)
    Label(root, text=str("Середнє значення: " + str(results[3]))).place(x=190, y=190)
    Label(root, text=str("Розмах: " + str(results[4]))).place(x=10, y=210)
    Label(root, text=str("Девіація: " + str(results[5]))).place(x=10, y=230)
    Label(root, text=str("Варіанса: " + str(results[6]))).place(x=10, y=250)
    Label(root, text=str("Стандарт: " + str(results[7]))).place(x=10, y=270)
    Label(root, text=str("Дисперсія: " + str(results[8]))).place(x=10, y=290)
    Label(root, text=str("Варіація: " + str(results[9]))).place(x=10, y=310)
    try:
        result = str("Інтерквантильна широта: ") + str(results[10][0])
        Label(root, text=str(result)).place(x=10, y=330)
    except:
        res = Label(root, text="Не існує значень ").place(x=10, y=330)
    try:
        result = str("Інтердецильна широта: ") + str(results[10][2])
        Label(root, text=str(result)).place(x=10, y=350)
    except:
        res = Label(root, text="Не існує значень ").place(x=10, y=350)
    try:
        result = str("Інтерцентильна широта: ") + str(results[10][4])
        Label(root, text=str(result)).place(x=10, y=370)
    except:
        res = Label(root, text="Не існує значень ").place(x=10, y=370)
    try:
        result = str("Інтермілілільна широта: ") + str(results[10][6])
        Label(root, text=str(result)).place(x=10, y=390)
    except:
        res = Label(root, text="Не існує значень ").place(x=10, y=390)
    Label(root, text=str("Початкові моменти: " + str(results[11]))).place(x=10, y=410)
    Label(root, text=str("Середні моменти: " + str(results[12]))).place(x=10, y=430)
    Label(root, text=str("Асиметрія: " + str(results[13]))).place(x=10, y=450)
    Label(root, text=str("Ексцес: " + str(results[14]))).place(x=10, y=470)
    Label(root, text=str("Емпірична: ")+str(results[15])).place(x=10, y=490)
    diskretna.draw()

def nepererv():
    global root, start_box, end_box, amount_box
    root = Tk()
    root.geometry("720x600+300+300")
    start_label = Label(root, text="Старт: ", font = "Helvetica 15 bold")
    start_box = Entry(root)
    start_label.place(x=3, y=3)
    start_box.place(x=200, y=3)

    end_label = Label(root, text="Кінець:", font = "Helvetica 15 bold")
    end_box = Entry(root)
    end_label.place(x=3, y=30)
    end_box.place(x=200, y=30)

    amount_label = Label(root, text="Кількість:", font = "Helvetica 15 bold")
    amount_box = Entry(root)
    amount_label.place(x=3, y=60)
    amount_box.place(x=200, y=60)

    button_add = Button(root, text="Генерувати", command=run_nepererv_button_pushed, font = "Helvetica 15 bold")
    button_add.place(x=10, y=100)

def run_nepererv_button_pushed():
    global root, start_box, end_box, amount_box
    start = str(start_box.get())
    end = str(end_box.get())
    amount = str(amount_box.get())
    start = float(start)
    end = float(end)
    amount = int(amount)
    results =runstat(start, end, amount)
    Label(root, text="Ряд: ").place(x=10, y=190)
    Label(root, text="X: "+ str(results[0])).place(x=10, y=210)
    Label(root, text="N: "+ str(results[1])).place(x=10, y=230)
    Label(root, text="Z: "+ str(results[2])).place(x=10, y=250)
    Label(root, text="Мода: "+ str(results[3])).place(x=10, y=270)
    Label(root, text="Медіана: "+ str(results[4])).place(x=10, y=290)
    Label(root, text="Середнє значення: "+ str(results[5])).place(x=10, y=310)
    Label(root, text="Девіація: "+ str(results[6])).place(x=10, y=330)
    Label(root, text="Варіанса: "+ str(results[7])).place(x=10, y=350)
    Label(root, text="Стандарт: "+ str(results[8])).place(x=10, y=370)
    Label(root, text="Варіація: "+ str(results[9])).place(x=10, y=390)
    Label(root, text="Дисперсія: "+ str(results[10])).place(x=10, y=410)
    Label(root, text="Моменти: "+ str(results[11])).place(x=10, y=430)
    Label(root, text="Асиметрія: "+ str(results[12])).place(x=10, y=450)
    Label(root, text="Ексцес: "+ str(results[13])).place(x=10, y=470)
    drawa(results[14],results[15])

def creating_table_Puasson():
    global root, start_label, start_box, end_label, end_box, amount_label, amount_box, accuracy_label, accuracy_box, button_add
    root = Tk()
    root.geometry("720x600+300+300")
    start_label = Label(root, text="Старт: ", font="Helvetica 15 bold", bg="pink")
    start_box = Entry(root)
    start_label.place(x=3, y=3)
    start_box.place(x=200, y=3)

    end_label = Label(root, text="Кінець: ", font="Helvetica 15 bold", bg="pink")
    end_box = Entry(root)
    end_label.place(x=3, y=30)
    end_box.place(x=200, y=30)

    amount_label = Label(root, text="Кількість: ", font="Helvetica 15 bold", bg="pink")
    amount_box = Entry(root)
    amount_label.place(x=3, y=60)
    amount_box.place(x=200, y=60)

    accuracy_label = Label(root, text="Точність(0,01/0,05): ", font="Helvetica 15 bold", bg="pink")
    accuracy_box = Entry(root)
    accuracy_label.place(x = 3, y = 90)
    accuracy_box.place(x = 215, y = 95)

    button_add = Button(root, text="Створити вибірку", command=run_Puasson, fg="black", bg="pink", font="Helvetica 15 bold")
    button_add.place(x=10, y=130)

def run_Puasson():
    global root, start_box, end_box, amount_box, accuracy_box
    start = str(start_box.get())
    end = str(end_box.get())
    amount = str(amount_box.get())
    accuracy = str(accuracy_box.get())
    start = int(start)
    end = int(end)
    amount = int(amount)
    accuracy = float(accuracy)
    results = diskretna.run(start, end, amount, accuracy)
    info = Label(root, text="Ряд:\n Частоти: ")
    info.place(x=10, y=210)

    resinfo = []
    for i in results[0].keys():
        resinfo.append(i)
    res_info = Label(root, text=str(resinfo))
    res_info.place(x=140, y=210)
    resinfo = []
    for i in results[0].values():
        resinfo.append(i)
    second_info = Label(root, text=str(resinfo))
    second_info.place(x=140, y=230)
    Label(root, text=str("Середнє значення: " + str(results[3]))).place(x=10, y=260)
    Label(root, text=str("Розподіл Пуассона.\n\nPi: " + str(results[17]))).place(x=10, y=280)
    Label(root, text=str("N * Pi: " + str(results[18]))).place(x=10, y=340)
    Label(root, text=str("X емпіричне: " + str(results[19]))).place(x=10, y=370)
    Label(root, text=str("X критичне: " + str(results[20]))).place(x=10, y=400)
    Label(root, text=str("Порівняння: " + str(results[21]))).place(x=10, y=420)



# def creating_table_Normal():
#     global root, start_label, start_box, end_label, end_box, amount_label, amount_box, accuracy_label, accuracy_box, button_add
#     root = Tk()
#     root.geometry("720x600+300+300")
#     start_label = Label(root, text="Старт: ", font="Helvetica 15 bold", bg="aqua")
#     start_box = Entry(root)
#     start_label.place(x=3, y=3)
#     start_box.place(x=200, y=3)
#
#     end_label = Label(root, text="Кінець: ", font="Helvetica 15 bold", bg="aqua")
#     end_box = Entry(root)
#     end_label.place(x=3, y=30)
#     end_box.place(x=200, y=30)
#
#     amount_label = Label(root, text="Кількість: ", font="Helvetica 15 bold", bg="aqua")
#     amount_box = Entry(root)
#     amount_label.place(x=3, y=60)
#     amount_box.place(x=200, y=60)
#
#     accuracy_label = Label(root, text="Точність(0,01/0,05): ", font="Helvetica 15 bold", bg="aqua")
#     accuracy_box = Entry(root)
#     accuracy_label.place(x=3, y=90)
#     accuracy_box.place(x=215, y=95)
#
#     button_add = Button(root, text="Створити вибірку", command=run_Normal, fg="black", bg="aqua",font="Helvetica 15 bold")
#     button_add.place(x=10, y=130)
#
# def run_Normal():
#     global root, start_box, end_box, amount_box, accuracy_box
#     start = str(start_box.get())
#     end = str(end_box.get())
#     amount = str(amount_box.get())
#     accuracy = str(accuracy_box.get())
#     start = float(start)
#     end = float(end)
#     amount = int(amount)
#     accuracy = float(accuracy)
#     results = runstat(start, end, amount, accuracy)
#     Label(root, text="Xi: " + str(results[0])).place(x=10, y=180)
#     Label(root, text="Ni: " + str(results[1])).place(x=10, y=200)
#     Label(root, text="Zi: " + str(results[2])).place(x=10, y=220)
#     Label(root, text="Середнє значення: " + str(results[5])).place(x=10, y=240)
#     Label(root, text="Стандарт: " + str(results[8])).place(x=10, y=260)
#     Label(root, text="Нормальний розподіл.\n\n Pi: " + str(results[16])).place(x=10, y=280)
#     Label(root, text="N * Pi: " + str(results[17])).place(x=10, y=340)
#     Label(root, text="X емпіричне: " + str(results[18])).place(x=10, y=360)
#     Label(root, text="X критичне: " + str(results[19])).place(x=10, y=380)
#     Label(root, text="Порівняння: " + str(results[20])).place(x=10, y=400)


def creating_table_Exponent():
    global root, start_label, start_box, end_label, end_box, amount_label, amount_box, button_add
    root = Tk()
    root.geometry("720x600+300+300")
    start_label = Label(root, text="Старт: ", font="Helvetica 15 bold", bg="orchid")
    start_box = Entry(root)
    start_label.place(x=3, y=3)
    start_box.place(x=200, y=3)

    end_label = Label(root, text="Кінець: ", font="Helvetica 15 bold", bg="orchid")
    end_box = Entry(root)
    end_label.place(x=3, y=30)
    end_box.place(x=200, y=30)

    amount_label = Label(root, text="Кількість: ", font="Helvetica 15 bold", bg="orchid")
    amount_box = Entry(root)
    amount_label.place(x=3, y=60)
    amount_box.place(x=200, y=60)

    accuracy_label = Label(root, text="Точність(0,01/0,05): ", font="Helvetica 15 bold", bg="orchid")
    accuracy_box = Entry(root)
    accuracy_label.place(x=3, y=90)
    accuracy_box.place(x=215, y=95)

    button_add = Button(root, text="Створити вибірку", command=run_Exponent, fg="black", bg="orchid", font="Helvetica 15 bold")
    button_add.place(x=10, y=130)

def run_Exponent():
    global root, start_box, end_box, amount_box, accuracy_box
    start = str(start_box.get())
    end = str(end_box.get())
    amount = str(amount_box.get())
    accuracy = str(accuracy_box.get())
    start = float(start)
    end = float(end)
    amount = int(amount)
    accuracy = float(accuracy)
    results = runstat(start, end, amount, accuracy)
    Label(root, text="Xi: " + str(results[0])).place(x=10, y=180)
    Label(root, text="Ni: " + str(results[1])).place(x=10, y=200)
    Label(root, text="Zi: " + str(results[2])).place(x=10, y=220)
    Label(root, text="Середнє значення: " + str(results[5])).place(x=10, y=240)
    Label(root, text="Стандарт: " + str(results[8])).place(x=10, y=260)
    Label(root, text="Експонентний розподіл.\n\n Pi: " + str(results[16])).place(x=10, y=280)
    Label(root, text="N * Pi: " + str(results[17])).place(x=10, y=340)
    Label(root, text="X емпіричне: " + str(results[18])).place(x=10, y=360)
    Label(root, text="X критичне: " + str(results[19])).place(x=10, y=380)
    Label(root, text="Порівняння: " + str(results[20])).place(x=10, y=400)

main_window()
