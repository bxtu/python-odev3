class Personel:
    def __init__(self, adi, departman, calisma_yili, maas):
        self.adi = adi
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel_nesnesi):
        self.personel_listesi.append(personel_nesnesi)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("Adı:", personel.adi)
            print("Departmanı:", personel.departman)
            print("Çalışma Yılı:", personel.calisma_yili)
            print("Maaşı:", personel.maas)
            print()

    def maas_zammi(self, personel_nesnesi, zam_orani):
        personel_nesnesi.maas *= (1 + zam_orani / 100)

    def personel_cikart(self, personel_nesnesi):
        self.personel_listesi.remove(personel_nesnesi)

# Personel nesneleri oluşturalım
personel1 = Personel("Ahmet", "Muhasebe", 5, 5000)
personel2 = Personel("Ayşe", "İnsan Kaynakları", 3, 4500)

# Firma nesnesi oluşturalım
firma = Firma()

firma.personel_ekle(personel1)
firma.personel_ekle(personel2)

print("Tüm Personeller:")
firma.personel_listele()

#firma.maas_zammi(personel1, 10)  # Ahmet'in maaşı %10 arttırıldı

#print("\nMaaşı Artırılan Personeller:")
#firma.personel_listele()

#firma.personel_cikart(personel2)  # Ayşe firmadan çıkarıldı

#print("\nGüncellenmiş Personel Listesi:")
#firma.personel_listele()
