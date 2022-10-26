


data_list = list(range(1,10))
winner = ""
def draw_field(): 
    print("-" * 9)
    for i in range(3):
      print( data_list[0+3*i], "|", data_list[1+3*i], "|", data_list[2+3*i])
      print("-" * 9)

   
def input_player():
    choose_place = int(input('Выберите клетку от 1 до 9: '))
    while choose_place < 1 or choose_place > 9:
        try:
            choose_place = int(input('Выберите клетку от 1 до 9: '))
        except ValueError:
            return choose_place
    player_token = input("Выбирите фигуру 'x' или 'y' ")
    while player_token != "x" and player_token != "y":
            player_token = input("Выбирите фигуру 'x' или 'y' ")
    data_list[choose_place - 1] = player_token
    return data_list

def check_win():
    global winner
    win_cord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for e in win_cord:
        if data_list[e[0]] == data_list[e[1]] == data_list[e[2]]:
          winner = data_list[e[0]]
          return True
        else:
            return False

def data_main():
    while input("Начать игру -> любая кнопка, конец игры -> end: ").strip() != 'end':
        try:
            draw_field()
            input_player()
            if (check_win()):
                print(winner)
                return
        except ValueError:
            break

if __name__ == "__main__":
    data_main()
    