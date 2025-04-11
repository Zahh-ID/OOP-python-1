class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama           # Public 
        self._nim = nim            # Protected 
        self.__prodi = prodi       # Private

    def showInfo(self):
        print(f"Nama: {self.nama}, NIM: {self._nim}, Prodi: {self.__prodi}")

    def changeProdi(self, prodi_baru):
        self.__prodi = prodi_baru

    def getProdi(self):
        return self.__prodi


class MataKuliah:
    def __init__(self, nama_mk, kode_mk, sks):
        self.nama_mk = nama_mk     # Public
        self.__kode_mk = kode_mk    # Protected 
        self._sks = sks           # Private

    def showInfo(self):
        print(f"Mata Kuliah: {self.nama_mk}, Kode: {self.__kode_mk}, SKS: {self._sks}")

    def ubah_sks(self, sks_baru):
        self._sks = sks_baru

    def get_sks(self):
        return self._sks


class Dosen:
    def __init__(self, nama, nip, jurusan):
        self.nama = nama           # Public attribute
        self._nip = nip            # Protected attribute
        self.__jurusan = jurusan   # Private 
        
    def showInfo(self):
        print(f"Nama Dosen: {self.nama}, NIP: {self._nip}, Jurusan: {self.__jurusan}")

    def changeJurusan(self, jurusan_baru):
        self.__jurusan = jurusan_baru

    def getJurusan(self):
        return self.__jurusan


mahasiswa1 = Mahasiswa("Asy", "123456", "Informatika")
mahasiswa2 = Mahasiswa("Nazwa", "654321", "Sistem Informasi")
mahasiswa3 = Mahasiswa("Zahh", "987654", " Pendidikan Teknik Informatika")

matkul1 = MataKuliah("Pemrograman", "IF101", 3)
matkul2 = MataKuliah("Basis Data", "SI202", 4)
matkul3 = MataKuliah("Object Oriented Programming", "OOP303", 4)

dosen1 = Dosen("Bu Gress", "112233", "DTEI")
dosen2 = Dosen("Pak Wahyu", "223344", "DTEI")
dosen3 = Dosen("Pak Azhar", "334455", "DTEI")

mahasiswa1.showInfo()
mahasiswa2.showInfo()
mahasiswa3.showInfo()
print("=========================================")
matkul1.showInfo()
matkul2.showInfo()
matkul3.showInfo()
print("=========================================")
dosen1.showInfo()
dosen2.showInfo()
dosen3.showInfo()
