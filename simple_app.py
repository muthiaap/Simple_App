import multiprocessing
from datetime import datetime

class Pegawai:

    def __init__(self, nama, nik, tahun_masuk, jenjang, divisi, penilaian):
        self.nama = nama
        self.__nik = nik
        self.tahun_masuk = tahun_masuk
        #menghitung masa kerja pegawai
        self.masa_kerja = datetime.now().year - self.tahun_masuk
        self.jenjang = jenjang
        self.divisi = divisi
        self.penilaian = penilaian

    def get_nik(self):
        return self.__nik

    #jika pegawai pithing, penilaian bertambah 10 poin
    def pithing(self):
        self.penilaian += 10

    #jika pegawai terlambat, penilaian berkurang 2 poin
    def terlambat(self):
        self.penilaian -= 2

    #pegawai naik gaji jika masa kerja >= 2 dan penilaian > 70
    def cek_naik_gaji(self):
        if self.masa_kerja >= 2 and self.penilaian > 70:
            return True
        else:
            return False


def parallel_cek_naik_gaji(pegawai):
    if pegawai.cek_naik_gaji():
        print(f"{pegawai.nama} layak naik gaji.")
    else:
        print(f"{pegawai.nama} tidak layak naik gaji.")

p1 = Pegawai("Muthia Aisyah Putri", "1234567890", 2019, "AMGR", "Data Engineer", 65)
p2 = Pegawai("Ikhwanul Muslimim", "6543210965", 2018, "MGR", "Data Scientist", 71)
p3 = Pegawai("Moch Fahrudin", "6574323421", 2023, "AVP", "Accounting", 85)
p4 = Pegawai("Putriani", "2346543721", 2020, "OS", "HR", 79)

p1.pithing()
p2.terlambat()
p2.terlambat()
p3.pithing()
p1.terlambat()
p4.terlambat()

if __name__ == "__main__":
    # Proses parallel untuk mengecek kenaikan gaji pegawai
    process1 = multiprocessing.Process(target=parallel_cek_naik_gaji, args=(p1,))
    process2 = multiprocessing.Process(target=parallel_cek_naik_gaji, args=(p2,))
    process3 = multiprocessing.Process(target=parallel_cek_naik_gaji, args=(p3,))
    process4 = multiprocessing.Process(target=parallel_cek_naik_gaji, args=(p4,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()