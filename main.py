import random

msg = "SELAMAT DATANG DI GAME GACHA SUMMER FEST GROWTOPIAS V1.0"
print("**************************************************************")
print(f"** {msg} **")
print("**************************************************************")
player_name = input("Masukkan nama player: ")
print(f"Selamat datang {player_name}!")
print(
    """  
Disini ada 5 Super Summer Surprise    
Tugas kamu adalah menebak manakah diantaranya yang isinya adalah Neptune's Trident

    1
      __\/_          
     |     |     
     | sss |     
     |_____|   
     
     
    2 
      __\/_          
     |     |     
     | sss |     
     |_____|  
     
     
    3
      __\/_          
     |     |     
     | sss |     
     |_____|  
     
     
    4
      __\/_          
     |     |     
     | sss |     
     |_____|  
     
     
    5
      __\/_          
     |     |     
     | sss |     
     |_____|  
      """
)

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

    prize_position = random.randint(1, 5)

    while True:

        print(f"Sisa Diamond Lock = {diamond_lock}")
        player_choice = int(input("Masukkan pilihanmu (1-5) (cost 5 DL): "))
        sure_choice = input("Apakah anda yakin? (y/n): ")

        if sure_choice.lower() == "y":
            diamond_lock -= 5
            break

    print(f"Item {prize_name} berada di posisi {prize_position}")

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

    choice_again = input("Apakah anda ingin bermain lagi? (y/n): ")
    if choice_again.lower() != "y":
        print("Terima kasih telah bermain!")
        break
