
num_player = int(input("Nhập số người chơi: "))
num_card = 52


if num_player <= 4:
    max_card = 13
elif num_player <= 6 :
    max_card = 10
elif num_player <= 8 :
    max_card = 9
elif num_player <= 10:
    max_card = 8
else:
    max_card = num_card // num_player
cards_left = num_card - max_card * num_player
    
print("Số lá bài tối đa cho mỗi người là:", max_card)
print("Số lá bài còn lại của bộ bài là:", cards_left)