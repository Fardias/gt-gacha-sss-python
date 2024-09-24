import random

msg = "SELAMAT DATANG DI GAME GACHA SUMMER FEST GROWTOPIAS V1.1"
print("**************************************************************")
print(f"** {msg} **")
print("**************************************************************")
player_name = input("Masukkan nama player: ")
print(f"Selamat datang {player_name}!")

prize_position = random.randint(1, 5)

design_sss = "|?|"
hide_sss_prize = [design_sss] * 5

show_sss_prize = hide_sss_prize.copy()
show_sss_prize[prize_position - 1] = "|✨|"


print('''
Disini ada 5 Super Summer Surprise    
Tugas kamu adalah menebak manakah diantaranya yang isinya adalah Neptune's Trident
'''
)
for i in range(len(hide_sss_prize)):
    print(hide_sss_prize[i], end=" ")
print("\n")
prize_name = "Neptune's Trident"
count_play_lose = 0
count_play_win = 0
diamond_lock = 15

while True:

    if diamond_lock <= 0:
        print("Maaf, diamond lock anda habis")
        print(f"Jawaban anda benar sebanyak {count_play_win} kali")
        print(f"Jawaban anda salah sebanyak {count_play_lose} kali")
        break


    while True:

        print(f"Sisa Diamond Lock = {diamond_lock}")
        player_choice = int(input("Masukkan pilihanmu (1-5) (cost 5 DL): "))
        sure_choice = input("Apakah anda yakin? (y/n): ")

        if sure_choice.lower() == "y":
            diamond_lock -= 5
            break
        
    print("\n")
    print(f"Item {prize_name} berada di posisi {prize_position}\n")
    for i in range(len(show_sss_prize)):
            print(show_sss_prize[i], end=" ")           
    print("\n")
    
    if player_choice == prize_position:
        print(f"Selamat {player_name}, anda benar!")
        
        count_play_win += 1
    else:
        print("Maaf, anda salah!")
        count_play_lose += 1

    if count_play_lose >= 2:
        print("jir rungkad wkowkkwokowk")

    if count_play_win >= 2:
        print("gacor kangg wkowkkwokowk")

    print("\n")
    choice_again = input("Apakah anda ingin bermain lagi? (y/n): ")
    if choice_again.lower() != "y":
        print("Terima kasih telah bermain!")
        break
