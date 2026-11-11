nama = input("Nama : ")

if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    target = 0
    print("Nama mahasiswa tidak terdaftar dalam sistem.")

if target > 0:
    print(f"Targetku {target}!")
    
    percobaan = 0
    berhasil_lulus = False
    
    while percobaan < 3:
        percobaan += 1
        nilai = int(input(f"Nilai {percobaan} : "))
        
        if nilai >= target:
            berhasil_lulus = True
            break
            
    print("\nOutput yang Diharapkan:")
    if berhasil_lulus:
        print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
    else:
        print(f"{nama} tidak lulus setelah 3 kali percobaan!")