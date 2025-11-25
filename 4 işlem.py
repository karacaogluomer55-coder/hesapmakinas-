sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("Ikinci sayiyi giriniz: "))
secim = input("Yapmak istediginiz islemi seciniz Toplama(+), Cikarma(-), Carpma(*), Bolme(/): ")
toplama = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma = sayi1 * sayi2
bolme = sayi1 / sayi2 
if secim == "+":
    print("Toplama isleminin sonucu: ", toplama)
elif secim == "-":
    print("Cikarma isleminin sonucu: ", cikarma)
elif secim == "*":
    print("Carpma isleminin sonucu: ", carpma)
elif secim == "/":
    print("Bolme isleminin sonucu: ", bolme)
else:
    print("Gecersiz islem secimi!")