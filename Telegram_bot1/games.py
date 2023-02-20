
import random
matrix = [1,2,3,4,5,6,7,8,9]

def show_matrix():
    return f'{matrix[0]} {matrix[1]} {matrix[2]} \n{matrix[3]} {matrix[4]} {matrix[5]} \n{matrix[6]} {matrix[7]} {matrix[8]}'
    
    # print(matrix[0], matrix[1], matrix[2])
    # print(matrix[3], matrix[4], matrix[5])
    # print(matrix[6], matrix[7], matrix[8])
    # print("\n")

   
def check_win():
    if matrix[0] == matrix[1] == matrix[2]:
        print(f"Победили {matrix[0]}")
        return 1
    elif matrix[3] == matrix[4] == matrix[5]:
        print(f"Победили {matrix[3]}")
        return 1
    elif matrix[6] == matrix[7] == matrix[8]:
        print(f"Победили {matrix[6]}")
        return 1
    elif matrix[0] == matrix[3] == matrix[6]:
        print(f"Победили {matrix[0]}")
        return 1
    elif matrix[1] == matrix[4] == matrix[7]:
        print(f"Победили {matrix[1]}")
        return 1
    elif matrix[2] == matrix[5] == matrix[8]:
        print(f"Победили {matrix[2]}")
        return 1
    elif matrix[0] == matrix[4] == matrix[8]:
        print(f"Победили {matrix[0]}")
        return 1
    elif matrix[2] == matrix[4] == matrix[6]:
        print(f"Победили {matrix[2]}")
        return 1
    else: return 0
    
    
def player(text):
    while True:
        try:
            number = int(input("Введите номер ячейки, чтобы поставить крестик: "))
            if (matrix[number-1] != "X") and matrix[number-1] != "O": 
                matrix[number-1] = "X"
                break
            else: print("Ячейка уже занята")
                
        except:
            print("Неверный ввод, попробуйте снова")
            break
       
       

def comp_player(matrix):
    for i in range(0, len(matrix)):
        if (matrix[i] != "X") and matrix[i] != "O":
            matrix[i] = "O"
            return

# print(show_matrix())
# while True:
  
#     player()
#     print(show_matrix())
#     if check_win() == 1:
#         break
#     print()
   
#     comp_player(matrix)
#     print(show_matrix())
#     if check_win() == 1:
#         break
#     print()
    
file_input = "DBase.txt"


#показать случайный анекдот из файла
def file_view(file_name):
    result = []
    with open(file_name, "r", encoding="utf8") as data:
        for line in data:
            result.append(line.strip('\n')) 
        return result
    

def random_string():
    list_joke = []
    list_joke = file_view(file_input)
    rand_index = random.randint(0, len(list_joke) - 1)
    print(list_joke[rand_index])
    
# random_string()


