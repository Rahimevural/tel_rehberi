tel_rehberi = dict()


def tel_no_ekle(x):
    print("*** numara ekleme ekranına hoşgeldiniz***")
    numara_isim_al = input("lütfen kayıt edilecek kişinin ismini giriniz : ")
    numara_no_al = input("lütfen telefon numarası gririn ")

    x= tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f"{numara_isim_al} adlı kişi telefon listeine eklendi ")


def tel_rehberi_goster(x):
    kisi_sayisi = len(x)
    print(f" rehberdeki kişi sayısı {kisi_sayisi}")
    print("Rehbere hosgeldiniz")

    for i,j in x.items():
        print(i,":",j)
    input ("devam edilsin mi ?")   


def no_sil(x):
    print("kişi silme ekranına hosgeldiniz")
    silinecek_kisi = input("silinecek kişiyi yazın: ")
    x = tel_rehberi.pop(silinecek_kisi)
    input ("devam edilsin mi ?")   


while True:
    print("*** HOSGELDİNİZ ***")
    print("*** seçim yapınız ***")
    secim_yap = int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n"))

    if secim_yap ==1 :
        tel_no_ekle(tel_rehberi)
    elif secim_yap ==2 :
            no_sil(tel_rehberi)

    elif secim_yap ==3:
        tel_rehberi_goster(tel_rehberi)

    else:
        print("lütfen uygun tuslara basınız")            
