import os
os.system('pip install pytube')

def Menu():
    print("""                     ,----,             
                   ,/   .`|             
                 ,`   .'  :   ,---,     
        ,---,  ;    ;     / .'  .' `\   
       /_ ./|.'___,/    ,',---.'     \  
 ,---, |  ' :|    :     | |   |  .`\  | 
/___/ \.  : |;    |.';  ; :   : |  '  | 
 .  \  \ ,' '`----'  |  | |   ' '  ;  : 
  \  ;  `  ,'    '   :  ; '   | ;  .  | 
   \  \    '     |   |  ' |   | :  |  ' 
    '  \   |     '   :  | '   : | /  ;  
     \  ;  ;     ;   |.'  |   | '` ,/   
      :  \  \    '---'    ;   :  .'     
       \  ' ; By : Sadewa |   ,.'       
        `--` 081266638780 '---'         \n""")
    print("Pilihan Menu:\n1. Download Video\n2. Download PLaylist\n0. Keluar")
    pilihan = input("\nMasukkan nomor => ")
    if pilihan == "1":
        pil1()
    elif pilihan == "2":
        pil2()
    elif pilihan == "0":
        exit()
    else:
        print("Tidak ada pilihan: ")
        Menu()

def pil1():
    from pytube import YouTube
    link = input("Masukkan Link = ")
    print("Loading... Tekan CTRL + C untuk berhenti")
    YouTube(link).streams.first().download()
    os.system('clear')
    Menu()

def pil2():
    from pytube import Playlist
    linkpl = input("Masukkan link playlist = ")
    playlist = Playlist(linkpl)
    for video in playlist.videos:
        print(video.title)
        video.streams.first().download()
        Menu()

Menu()
