class rekeningBank:
    def __init__(self,saldo):
        self.__saldo = 1000000

    def tampilkan_saldo(self):
        print(f"Saldo awal: {self.__saldo}")

    def tarik_saldo(self):
        tarik = int(input("Jumlah yang ingin ditarik: "))
        if self.__saldo >= tarik:
            self.__saldo -= tarik
            print(f"Tarik {tarik} berhasil! Saldo sekarang: {self.__saldo}")
        else:
            print("Saldo anda tidak mencukupi!")
    
    def setor_saldo(self):
        setor = int(input("Jumlah yang ingin disetorkan: "))
        if setor >= 0 :
            self.__saldo += setor
            print(f"Setor {setor} berhasil!. Saldo Sekarang: {self.__saldo}")
        else:
            print("Setor gagal!, jumlah setor harus lebih besar dari 0")


nasabah1 = rekeningBank(1000000)
nasabah1.tampilkan_saldo()
nasabah1.tarik_saldo()
nasabah1.setor_saldo()
