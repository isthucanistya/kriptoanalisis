def preprocess(kal):
    #ubah bentuk huruf dalam kalimat menjadi huruf kecil
    kal = kal.lower()
    #menghapus tanda baca dan spasi dalam kalimat
    bad_chars = ['!', ".", ",", "?", " "]
    for i in bad_chars:
        kal = kal.replace(i, '')
    return kal

def count(kalimat, huruf):
    # variabel untuk menghitung kemunculan huruf
    hitung = 0
    # pengulangan untuk setiap data pada kalimat
    for huruf1 in kalimat:
        # jika bilangan terdapat pada kalimat
        # maka hitung ditambah 1
        if huruf1 == huruf:
            hitung += 1
    return hitung

kal = str(input("Masukkan Kalimat: "))
kal = preprocess(kal)
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for huruf in alpabet:
    if count(kal, huruf)!=0:
        print("Munculnya Huruf ", huruf, "=", count(kal, huruf), " kali")