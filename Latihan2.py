class persegi_panjang :
    def __init__ (self, panjang, lebar):
        self._panjang = panjang
        self._lebar = lebar
    def tampilan_parameter (self):
        print(f'panjang = {self._panjang}, \nlebar  = {self._lebar}')
    def luas_persegip (self):
        luas = (self._panjang * self._lebar)
        print(f'luas : {luas}')
    def keliling_persegip (self):
        keliling = 2 * (self._panjang + self._lebar)
        print(f'keliling : {keliling}')
        
kotakP = persegi_panjang(5 , 10)
kotakP.tampilan_parameter()
kotakP.luas_persegip()
kotakP.keliling_persegip()
