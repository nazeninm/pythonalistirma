print("""***********************************
GEOMETRİK ŞEKİLİN TİPİNİ BELİRLEME
***********************************
""")
a=input("Tipini Belirlemek İstediğiniz Şekli Yazınız(Üçgen/Dörtgen): ")

if a == "dörtgen" :
    k1=int(input("Birinci kenarı giriniz: "))
    k2=int(input("İkinci kenarı giriniz: "))
    k3=int(input("Üçüncü kenarı giriniz: "))
    k4=int(input("Dördüncü kenarı giriniz: "))
    if k1 == k2 and k2 == k3:
        print("Girdiğiniz şekil bir karedir.")
    else:
        print("Girdiğiniz şekil bir dikdörtgendir.")
elif a == "üçgen":
    k1=int(input("Birinci kenarı giriniz: "))
    k2=int(input("İkinci kenarı giriniz: "))
    k3=int(input("Üçüncü kenarı giriniz: "))
    if abs(k1-k2) < k3 < k1+k2 and abs(k2-k3) < k1 < k2+k3 and abs(k3-k1) < k2 < k3+k1:
       if k1 == k2 and k2 == k3:
           print("Girdiğiniz şekil bir eşkenar üçgendir.")
       elif k1 == k2 or k1 == k3:
            print("Girdiğiniz üçgen ikizkenar üçgendir.")
       else:
           print("Girdiğiniz şekil sıradan bir üçgendir.")


    else:
        print("Girdiğiniz kenar uzunlukları bir üçgen belirtmez.")
