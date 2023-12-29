class Admin:
    def __init__(self, ID_Admin, Username, Password):
        self.ID_Admin = ID_Admin
        self.Username = Username
        self.Password = Password

class Customer:
    def __init__(self, id_customer, nama, email, telepon, alamat):
        self.id_customer = id_customer
        self.nama = nama
        self.email = email
        self.telepon = telepon
        self.alamat = alamat

class ProdukMobil:
    def __init__(self, ID_Mobil, Merk, Model, Tahun, Harga, Stok):
        self.ID_Mobil = ID_Mobil
        self.Merk = Merk
        self.Model = Model
        self.Tahun = Tahun
        self.Harga = Harga
        self.Stok = Stok

class ProdukService:
    def __init__(self, ID_ProdukService, Nama, Model, Harga, Stok):
        self.ID_ProdukService = ID_ProdukService
        self.Nama = Nama
        self.Model = Model
        self.Harga = Harga
        self.Stok = Stok

class TransaksiService:
    def __init__(self, ID_Service, ID_Customer, ID_ProdukService, Nomor_Kendaraan, Nama_Kendaraan, Keterangan, TotalService, TanggalService):
        self.ID_Service = ID_Service
        self.ID_Customer = ID_Customer
        self.ID_ProdukService = ID_ProdukService
        self.Nomor_Kendaraan = Nomor_Kendaraan
        self.Nama_Kendaraan = Nama_Kendaraan
        self.Keterangan = Keterangan
        self.TotalService = TotalService
        self.TanggalService = TanggalService
        
class TransaksiPembelianMobil:
    def __init__(self, ID_Customer, ID_Mobil, Jumlah, TotalHarga, TanggalPembelian, Status):
        self.ID_Customer = ID_Customer
        self.ID_Mobil = ID_Mobil
        self.Jumlah = Jumlah
        self.TotalHarga = TotalHarga
        self.TanggalPembelian = TanggalPembelian
        self.Status = Status
