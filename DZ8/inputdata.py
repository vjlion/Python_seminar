from data_create import *  
def input_data():  
    lastname = last_name()     
    firstname = first_name()     
    phonenum = phone()   
    
    with open('D:\course_python\sem7\phonebook.txt',"a",encoding="utf-8") as file:      
        
        file.write(f"\n{lastname}\t{firstname}\t{phonenum}")     
         
def print_data():    
    with open('D:\course_python\sem7\phonebook.txt', "r", encoding="utf-8") as data: 
        data_new = data.read() 
        print(data_new)
def search():     
    lookfor = input("кого ищем? ") 
    bool_1=False    
    with open('D:\course_python\sem7\phonebook.txt', "r", encoding="utf-8") as data:         
        for line in data:             
            if lookfor in line:                 
                print(line)  
                bool_1=True
        if bool_1==False:
            print(" такой записи нет ")
def load():     
    new_phonebook = input("введите ссылку: ")     
    with open(new_phonebook, "r", encoding="utf-8") as data:         
        with open('D:\course_python\sem7\phonebook.txt', "a+", encoding="utf-8") as data_1:             
            data_1.write("\n")
            for line in data:                 
                if line not in data_1:                     
                    data_1.write(line)  
def delete_line():
    line_str=input("Введите запись, которую нужно удалить: ")          
    with open('D:\course_python\sem7\phonebook.txt', "r", encoding="utf-8") as data:     
        lines=data.readlines()
        with open('D:\course_python\sem7\phonebook.txt', "w", encoding="utf-8") as data1:     
            for line in lines:
                if line_str not in line:
                    data1.write(line)
                else:
                    print(line)
                    ask=input("Желаете удалить эту строку (y,n) : ")
                    while ask not in ("y","n"):
                        print("ввод некорректный")
                        ask=input("Желаете удалить эту строку (y,n) : ")
                    if ask=="n":
                        data1.write(line)
                        


""" for i in range(len(data.readlines())): 
            data_temp=data.readline()   
            if line_str != data_temp:
                data.write(data_temp)
            else:
                print(data_temp)
                a=int(input("точно удалить эту запись ?(да-1, нет-2)"))
                if a==2:
                    data.write(data_temp) 
""" 
def change_line():
    line_str=input("Введите запись, которую нужно изменить: ")          
    with open('D:\course_python\sem7\phonebook.txt', "r", encoding="utf-8") as data:     
        lines=data.readlines()
        with open('D:\course_python\sem7\phonebook.txt', "w", encoding="utf-8") as data1:     
            for line in lines:
                if line_str not in line:
                    data1.write(line)  
                else :
                    ask=input("Что хотите поменять (1,2,3) : ")
                    while ask not in ("1","2","3"):
                        print("ввод некорректный")
                        ask=input("Что хотите поменять (1,2,3) : ")
                    new_data=input("Введите новые данные : ")    
                    line_list=line.split()
                    line_list[int(ask)-1]=new_data
                    data1.write("\t".join(line_list)+"\n")  

                    
                    # lastname = input("Введите новые данные (Фамилия): ")     
                    # name = input("Введите новые данные (Имя): ")    
                    # phone = input("Введите новые данные (Телефон: ")    
                    # #data1.write("\n")       
                    # data1.write(f"{lastname}\t{name}\t{phone}")      

                     
print_data()