from connect import Database
from query import Query
from prettytable import PrettyTable

class Menu:
    def __init__(self):
        self.db = Database()
        self.query = Query(self.db)
        
    def main_menu(self):
        while True:
            print("\n===== Dealer Mobil Menu =====")
            print("1. Registrasi Admin Dealer")
            print("2. Admin Dealer")
            print("3. Customer")
            print("4. Keluar")

            choice = input("Pilih menu (1-4): ")

            if choice == "1":
                self.registrasi_admin_dealer()
            elif choice == "2":
                self.login_admin_dealer()
            elif choice == "3":
                self.menu_customer()
            elif choice == "4":
                print("Terimakasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def registrasi_admin_dealer(self):
        print("\n===== Registrasi Admin Dealer =====")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        # Insert pendaftaran admin dealer 
        self.query.insert_admin(username, password)
        print("Admin Dealer berhasil diregistrasi!")

    def login_admin_dealer(self):
        print("\n===== Login Admin Dealer =====")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        # Periksa apakah username dan password sesuai dengan catatan/database admin dealer
        if self.query.login_admin(username, password):
            print("Login berhasil!")
            self.menu_admin_dealer()
        else:
            print("Username atau password salah. Silakan coba lagi.")

    def menu_admin_dealer(self):
        while True:
            print("\n===== Menu Admin Dealer =====")
            print("a. Mobil")
            print("b. Service")
            print("c. Data Customer")
            print("d. Transaksi Mobil")
            print("e. Transaksi Service")
            print("f. Kembali ke Menu Utama")
            print("g. Keluar")

            choice_admin_dealer = input("Pilih menu (a-g): ")

            if choice_admin_dealer == "a":
                self.menu_mobil()
            elif choice_admin_dealer == "b":
                self.menu_service()
            elif choice_admin_dealer == "c":
                self.menu_data_customer()
            elif choice_admin_dealer == "d":
                self.menu_transaksi_mobil()
            elif choice_admin_dealer == "e":
                self.menu_transaksi_service()
            elif choice_admin_dealer == "f":
                self.main_menu()
            elif choice_admin_dealer == "g":
                print("Terimakasih!")
                exit()
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def menu_customer(self):
        while True:
            print("\n===== Menu Customer =====")
            print("a. Data Customer")
            print("b. Transaksi Mobil")
            print("c. Transaksi Service")
            print("d. Kembali ke Menu Utama")
            print("e. Keluar")

            choice_customer = input("Pilih menu (a-e): ")

            if choice_customer == "a":
                self.menu_data_customer()
            elif choice_customer == "b":
                self.menu_transaksi_mobil()
            elif choice_customer == "c":
                self.menu_transaksi_service()
            elif choice_customer == "d":
                self.main_menu()
            elif choice_customer == "e":
                print("Terimakasih!")
                exit()
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def menu_mobil(self):
        while True:
            print("\n===== Menu Mobil =====")
            print("a. Tambah Mobil")
            print("b. Tampilkan Mobil")
            print("c. Ubah Mobil")
            print("d. Hapus Mobil")
            print("e. Kembali Ke Menu")

            choice_mobil = input("Pilih menu (a-e): ")

            if choice_mobil == "a":
                self.tambah_mobil()
            elif choice_mobil == "b":
                self.tampilkan_mobil()
            elif choice_mobil == "c":
                self.ubah_mobil()
            elif choice_mobil == "d":
                self.hapus_mobil()
            elif choice_mobil == "e":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambah_mobil(self):
        print("\n===== Tambah Mobil =====")
        merk = input("Merk: ")
        model = input("Model: ")
        tahun = input("Tahun: ")
        harga = input("Harga: ")
        stok = input("Stok: ")

        # Ubah pemanggilan ke metode insert_produk_mobil
        self.query.insert_produk_mobil(merk, model, tahun, harga, stok)
        print("Mobil berhasil ditambahkan!")

    def tampilkan_mobil(self):
        try:
            print("\n===== Daftar Mobil =====")

            # Menggunakan fungsi get_produk_mobil_data dari query
            mobil_list = self.query.get_produk_mobil_data()

            if mobil_list:
                # Membuat objek PrettyTable
                table = PrettyTable()
                table.field_names = ["ID", "Merk", "Model", "Tahun", "Harga", "Stok"]

                # Menambahkan data mobil ke dalam tabel
                for mobil in mobil_list:
                    table.add_row([mobil['id_mobil'], mobil['merk'], mobil['model'], mobil['tahun'], mobil['harga'], mobil['stok']])

                # Mencetak tabel
                print(table)
            else:
                print("Tidak ada data mobil.")
        except Exception as e:
            print(f"Error: {e}")
            
    def ubah_mobil(self):
        try:
            print("\n===== Ubah Data Mobil =====")
            id_mobil = int(input("Masukkan ID Mobil yang akan diubah: "))

            # Dapatkan data mobil sebelum diubah menggunakan fungsi baru
            mobil_sebelum_diubah = self.query.get_produk_mobil_by_id(id_mobil)

            if mobil_sebelum_diubah:
                print("Data Mobil Sebelum Diubah:")
                print(f"ID: {mobil_sebelum_diubah['id_mobil']}, Merk: {mobil_sebelum_diubah['merk']}, Model: {mobil_sebelum_diubah['model']}, Tahun: {mobil_sebelum_diubah['tahun']}, Harga: {mobil_sebelum_diubah['harga']}, Stok: {mobil_sebelum_diubah['stok']}")

                # Tambahkan logika untuk mengubah mobil
                merk = input("Merk (kosongkan jika tidak diubah): ")
                model = input("Model (kosongkan jika tidak diubah): ")
                tahun = input("Tahun (kosongkan jika tidak diubah): ")
                harga = input("Harga (kosongkan jika tidak diubah): ")
                stok = input("Stok (kosongkan jika tidak diubah): ")

                # Ubah mobil hanya jika input tidak kosong
                if merk or model or tahun or harga or stok:
                    # Panggil fungsi untuk mengubah mobil dengan parameter yang sesuai
                    self.query.update_produk_mobil(
                        id_mobil,
                        merk if merk else mobil_sebelum_diubah['merk'],
                        model if model else mobil_sebelum_diubah['model'],
                        tahun if tahun else mobil_sebelum_diubah['tahun'],
                        harga if harga else mobil_sebelum_diubah['harga'],
                        stok if stok else mobil_sebelum_diubah['stok']
                    )

                    print("Data Mobil Berhasil Diubah!")
                else:
                    print("Tidak ada perubahan data mobil.")
            else:
                print(f"ID Mobil {id_mobil} tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")

    def hapus_mobil(self):
        try:
            print("\n===== Hapus Data Mobil =====")
            id_mobil = int(input("Masukkan ID Mobil yang akan dihapus: "))

            # Dapatkan data mobil sebelum dihapus menggunakan fungsi baru
            mobil_sebelum_dihapus = self.query.get_produk_mobil_by_id(id_mobil)

            if mobil_sebelum_dihapus:
                print("Data Mobil Sebelum Dihapus:")
                print(f"ID: {mobil_sebelum_dihapus['id_mobil']}, Merk: {mobil_sebelum_dihapus['merk']}, Model: {mobil_sebelum_dihapus['model']}, Tahun: {mobil_sebelum_dihapus['tahun']}, Harga: {mobil_sebelum_dihapus['harga']}, Stok: {mobil_sebelum_dihapus['stok']}")

                konfirmasi = input("Apakah Anda yakin ingin menghapus data mobil ini? (y/n): ").lower()

                if konfirmasi == 'y':
                    # Panggil fungsi untuk menghapus mobil
                    self.query.delete_produk_mobil(id_mobil)
                    print("Data Mobil Berhasil Dihapus!")
                else:
                    print("Penghapusan data mobil dibatalkan.")
            else:
                print(f"ID Mobil {id_mobil} tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")

    def menu_service(self):
        while True:
            print("\n===== Menu Service =====")
            print("a. Tambah Data Service")
            print("b. Tampilkan Data Service")
            print("c. Ubah Data Service")
            print("d. Hapus Data Service")
            print("e. Kembali Ke Menu")

            choice_service = input("Pilih menu (a-e): ")

            if choice_service == "a":
                self.tambah_service()
            elif choice_service == "b":
                self.tampilkan_service()
            elif choice_service == "c":
                self.ubah_service()
            elif choice_service == "d":
                self.hapus_service()
            elif choice_service == "e":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambah_service(self):
        try:
            print("\n===== Tambah Data Service =====")
            nama = input("Nama Service: ")
            model = input("Model Service: ")
            harga = input("Harga Service: ")
            stok = input("Stok Service: ")

            # Panggil fungsi untuk menambah data service
            self.query.insert_produk_service(nama, model, harga, stok)
            print("Data Service Berhasil Ditambahkan!")
        except Exception as e:
            print(f"Error: {e}")

    def tampilkan_service(self):
        try:
            print("\n===== Daftar Layanan Service =====")

            # Menggunakan fungsi get_service_data dari query
            service_list = self.query.get_service_data()

            if service_list:
                # Membuat objek PrettyTable
                table = PrettyTable()
                table.field_names = ["ID", "Nama", "Model", "Harga", "Stok"]

                # Menambahkan data service ke dalam tabel
                for service in service_list:
                    table.add_row([service['id_produk_service'], service['nama'], service['model'], service['harga'], service['stok']])

                # Mencetak tabel
                print(table)
            else:
                print("Tidak ada data layanan service.")
        except Exception as e:
            print(f"Error: {e}")


    def ubah_service(self):
        try:
            print("\n===== Ubah Data Layanan Service =====")
            id_service = int(input("Masukkan ID Layanan Service yang akan diubah: "))

            # Dapatkan data layanan berdasarkan ID
            current_service = self.query.get_service_by_id(id_service)

            if current_service:
                print("Data Layanan Service Sebelum Diubah:")
                print(f"ID: {current_service['id_produk_service']}, Nama: {current_service['nama']}, Model: {current_service['model']}, Harga: {current_service['harga']}, Stok: {current_service['stok']}")

                # Meminta input untuk perubahan (kosongkan jika tidak diubah)
                nama_baru = input(f"Masukkan Nama Baru (kosongkan jika tidak diubah) ({current_service['nama']}): ") or current_service['nama']
                model_baru = input(f"Masukkan Model Baru (kosongkan jika tidak diubah) ({current_service['model']}): ") or current_service['model']
                harga_baru = int(input(f"Masukkan Harga Baru (kosongkan jika tidak diubah) ({current_service['harga']}): ") or current_service['harga'])
                stok_baru = int(input(f"Masukkan Stok Baru (kosongkan jika tidak diubah) ({current_service['stok']}): ") or current_service['stok'])

                # Panggil fungsi update_service
                self.query.update_produk_service(id_service, nama_baru, model_baru, harga_baru, stok_baru)

                print("Data Layanan Service berhasil diubah!")
            else:
                print("ID Layanan Service tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")

    def hapus_service(self):
        try:
            print("\n===== Hapus Layanan Service =====")
            id_service = int(input("Masukkan ID Layanan Service yang akan dihapus: "))

            # Dapatkan data layanan berdasarkan ID
            current_service = self.query.get_service_by_id(id_service)

            if current_service:
                print("Data Layanan Service yang akan dihapus:")
                print(f"ID: {current_service['id_produk_service']}, Nama: {current_service['nama']}, Model: {current_service['model']}, Harga: {current_service['harga']}, Stok: {current_service['stok']}")

                konfirmasi = input("Apakah Anda yakin ingin menghapus layanan ini? (y/n): ").lower()

                if konfirmasi == 'y':
                    # Panggil fungsi delete_service
                    self.query.delete_produk_service(id_service)
                    print("Data Layanan Service berhasil dihapus!")
                else:
                    print("Penghapusan layanan dibatalkan.")
            else:
                print("ID Layanan Service tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")

    def menu_data_customer(self):
        while True:
            print("\n===== Menu Data Customer =====")
            print("a. Tambah Data Customer")
            print("b. Tampilkan Data Customer")
            print("c. Ubah Data Customer")
            print("d. Hapus Data Customer")
            print("e. Kembali Ke Menu")

            choice_customer = input("Pilih menu (a-e): ")

            if choice_customer == "a":
                self.tambah_customer()
            elif choice_customer == "b":
                self.tampilkan_customer()
            elif choice_customer == "c":
                self.ubah_customer()
            elif choice_customer == "d":
                self.hapus_customer()
            elif choice_customer == "e":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambah_customer(self):
        try:
            print("\n===== Tambah Customer =====")
            nama = input("Nama: ")
            email = input("Email: ")
            telepon = input("Nomor Telepon: ")
            alamat = input("Alamat: ")

            # Panggil fungsi insert_customer
            self.query.insert_customer(nama, email, telepon, alamat)
            print("Customer berhasil ditambahkan!")
        except Exception as e:
            print(f"Error: {e}")

    def tampilkan_customer(self):
        try:
            print("\n===== Daftar Customer =====")

            # Menggunakan fungsi get_customer_data dari query untuk mendapatkan data customer
            customer_list = self.query.get_customer_data()

            if customer_list:
                # Membuat objek PrettyTable
                table = PrettyTable()
                table.field_names = ["ID", "Nama", "Email", "Telepon", "Alamat"]

                # Menambahkan data customer ke dalam tabel
                for customer in customer_list:
                    table.add_row([customer.id_customer, customer.nama, customer.email, customer.telepon, customer.alamat])

                # Mencetak tabel
                print(table)
            else:
                print("Tidak ada data customer.")
        except Exception as e:
            print(f"Error: {e}")

    def ubah_customer(self):
        try:
            print("\n===== Ubah Data Customer =====")
            id_customer = input("Masukkan ID Customer yang akan diubah: ")

            # Menggunakan fungsi get_customer_by_id dari query
            current_customer = self.query.get_customer_by_id(id_customer)

            if current_customer:
                print(f"Data Customer Sebelum Diubah: {current_customer}")

                # Input data baru
                nama_baru = input(f"Masukkan Nama Baru (kosongkan jika tidak diubah) ({current_customer['nama']}): ") or current_customer['nama']
                email_baru = input(f"Masukkan Email Baru (kosongkan jika tidak diubah) ({current_customer['email']}): ") or current_customer['email']
                telepon_baru = input(f"Masukkan Telepon Baru (kosongkan jika tidak diubah) ({current_customer['telepon']}): ") or current_customer['telepon']
                alamat_baru = input(f"Masukkan Alamat Baru (kosongkan jika tidak diubah) ({current_customer['alamat']}): ") or current_customer['alamat']

                # Menggunakan fungsi update_customer dari query
                self.query.update_customer(id_customer, nama_baru, email_baru, telepon_baru, alamat_baru)
                print("Data Customer berhasil diubah!")
            else:
                print("Data Customer tidak ditemukan.")
        except Exception as e:
            print(f"Error: {e}")

    def hapus_customer(self):
        try:
            print("\n===== Hapus Data Customer =====")
            id_customer = int(input("Masukkan ID Customer yang akan dihapus: "))

            # Tampilkan data customer sebelum dihapus
            current_customer = self.query.get_customer_by_id(id_customer)
            if current_customer:
                print("\nData Customer Sebelum Dihapus:")
                print(f"ID: {current_customer['id_customer']}, Nama: {current_customer['nama']}, Email: {current_customer['email']}, Telepon: {current_customer['telepon']}, Alamat: {current_customer['alamat']}")
                
                # Konfirmasi pengguna untuk menghapus data
                konfirmasi = input("Apakah Anda yakin ingin menghapus data customer ini? (y/n): ")
                if konfirmasi.lower() == 'y':
                    self.query.hapus_customer(id_customer)
                    print("Data Customer berhasil dihapus!")
                else:
                    print("Penghapusan data dibatalkan.")
            else:
                print("Data Customer tidak ditemukan.")
        except ValueError:
            print("ID Customer harus berupa bilangan bulat.")
        except Exception as e:
            print(f"Error: {e}")
            
    def menu_transaksi_mobil(self):
        while True:
            print("\n===== Menu Transaksi Mobil =====")
            print("a. Beli Mobil")
            print("b. Tampilkan Data Transaksi Mobil")
            print("c. Tampilkan Data Seluruh Transaksi Mobil")
            print("d. Kembali Ke Menu")

            choice_transaksi_mobil = input("Pilih menu (a-d): ")

            if choice_transaksi_mobil == "a":
                self.beli_mobil()
            elif choice_transaksi_mobil == "b":
                self.tampilkan_transaksi_mobil()
            elif choice_transaksi_mobil == "c":
                self.tampilkan_seluruh_transaksi_mobil()
            elif choice_transaksi_mobil == "d":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def beli_mobil(self):
        try:
            print("\n===== Pembelian Mobil =====")

            # Menampilkan daftar mobil
            mobil_list = self.query.get_produk_mobil_data()
            if not mobil_list:
                print("Tidak ada mobil yang tersedia.")
                return

            # Menampilkan daftar mobil
            print("\n===== Daftar Mobil =====")
            table = PrettyTable()
            table.field_names = ["ID", "Merk", "Model", "Tahun", "Harga", "Stok"]

            for mobil in mobil_list:
                table.add_row([mobil['id_mobil'], mobil['merk'], mobil['model'], mobil['tahun'], mobil['harga'], mobil['stok']])

            print(table)

            # Meminta input ID Mobil yang akan dibeli
            id_mobil = input("Masukkan ID Mobil yang akan dibeli: ")
            # Periksa keberadaan ID Mobil
            if not self.query.check_produk_mobil_exists(id_mobil):
                print("ID Mobil tidak valid atau tidak ditemukan.")
                return
            # Dapatkan data mobil
            mobil = self.query.get_produk_mobil_by_id(id_mobil)

            # Meminta input jumlah pembelian
            jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
            # Periksa stok mobil
            if jumlah_pembelian > mobil['stok']:
                print("Jumlah pembelian melebihi stok mobil yang tersedia.")
                return
            elif jumlah_pembelian <= 0:
                print("Jumlah pembelian harus lebih dari 0.")
                return

            # Meminta input ID Customer yang akan membeli
            id_customer = input("Masukkan ID Customer yang akan membeli: ")

            # Periksa keberadaan ID Customer
            if not self.query.check_customer_exists(id_customer):
                print("ID Customer tidak valid atau tidak ditemukan.")
                return

            # Meminta input tanggal pembelian
            tanggal_pembelian = input("Masukkan tanggal pembelian (YYYY-MM-DD): ")

            # Hitung total harga
            total_harga = jumlah_pembelian * mobil['harga']

            # Menampilkan struk pembelian
            print("\n===== Struk Pembelian =====")
            print(f"ID Mobil: {mobil['id_mobil']}")
            print(f"Merk: {mobil['merk']}")
            print(f"Model: {mobil['model']}")
            print(f"Tahun: {mobil['tahun']}")
            print(f"Harga: {mobil['harga']}")
            print(f"Jumlah Pembelian: {jumlah_pembelian}")
            print(f"Total Harga: {total_harga}")

            # Mendapatkan data pelanggan
            pelanggan = self.query.get_customer_data_by_id(id_customer)

            # Menampilkan informasi pelanggan
            print(f"Nama Pelanggan: {pelanggan['nama']}")
            print(f"Email Pelanggan: {pelanggan['email']}")
            print(f"Telepon Pelanggan: {pelanggan['telepon']}")
            print(f"Alamat Pelanggan: {pelanggan['alamat']}")
            print(f"Tanggal Pembelian: {tanggal_pembelian}")

            # Konfirmasi pembelian
            konfirmasi = input("Konfirmasi pembelian (y/n): ").lower()
            if konfirmasi == 'y':
                # Update status transaksi_pembelian_mobil
                self.query.update_status_pembelian_mobil(id_customer, id_mobil, jumlah_pembelian, total_harga, tanggal_pembelian, 'Berhasil')

                # Kurangi stok mobil
                self.query.kurangi_stok_mobil(id_mobil, jumlah_pembelian)

                print("Pembelian berhasil!")
            else:
                print("Pembelian dibatalkan.")

        except Exception as e:
            print(f"Error: {e}")
            
    def tampilkan_transaksi_mobil(self):
        try:
            # Meminta input ID Customer
            id_customer = input("Masukkan ID Customer: ")

            # Periksa keberadaan ID Customer
            if not self.query.check_customer_exists(id_customer):
                print("ID Customer tidak valid atau tidak ditemukan.")
                return

            # Mengambil data transaksi pembelian mobil berdasarkan ID Customer
            transaksi_list = self.query.get_transaksi_pembelian_mobil_by_customer(id_customer)

            if not transaksi_list:
                print("Tidak ada transaksi pembelian mobil untuk ID Customer tersebut.")
                return

            # Membuat objek PrettyTable
            table = PrettyTable()
            table.field_names = ["ID Mobil", "Merk", "Model", "Jumlah Pembelian", "Total Harga", "Tanggal Pembelian", "Status"]

            # Menambahkan data transaksi ke dalam tabel
            for transaksi in transaksi_list:
                table.add_row([transaksi['id_mobil'], transaksi['merk'], transaksi['model'],
                               transaksi['jumlah'], transaksi['total_harga'],
                               transaksi['tanggal_pembelian'], transaksi['status']])

            # Mencetak tabel
            print("\n===== Transaksi Pembelian Mobil =====")
            print(table)

        except Exception as e:
            print(f"Error: {e}")

    def tampilkan_seluruh_transaksi_mobil(self):
        try:
            print("\n===== Seluruh Transaksi Pembelian Mobil =====")

            # Menggunakan fungsi get_seluruh_transaksi_pembelian_mobil dari query
            transaksi_list = self.query.get_seluruh_transaksi_pembelian_mobil()

            if transaksi_list:
                # Membuat objek PrettyTable
                table = PrettyTable()
                table.field_names = ["ID Customer", "ID Mobil", "Merk", "Model", "Jumlah", "Total Harga", "Tanggal Pembelian", "Status"]

                # Menambahkan data transaksi ke dalam tabel
                for transaksi in transaksi_list:
                    table.add_row([
                        transaksi['id_customer'],
                        transaksi['id_mobil'],
                        transaksi['merk'],
                        transaksi['model'],
                        transaksi['jumlah'],
                        transaksi['total_harga'],
                        transaksi['tanggal_pembelian'],
                        transaksi['status']
                    ])

                # Mencetak tabel
                print(table)
            else:
                print("Tidak ada transaksi pembelian mobil.")

        except Exception as e:
            print(f"Error: {e}")

    def menu_transaksi_service(self):
        while True:
            print("\n===== Menu Transaksi Service =====")
            print("a. Service Mobil")
            print("b. Tampilkan Data Transaksi Service")
            print("c. Tampilkan Data Seluruh Transaksi Service")
            print("d. Kembali Ke Menu")

            choice_transaksi_service = input("Pilih menu (a-d): ")

            if choice_transaksi_service == "a":
                self.service_mobil()
            elif choice_transaksi_service == "b":
                self.tampilkan_transaksi_service()
            elif choice_transaksi_service == "c":
                self.tampilkan_seluruh_transaksi_service()
            elif choice_transaksi_service == "d":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def service_mobil(self):
        # Tampilkan semua produk/jasa dari tabel produk_service
        produk_services = self.query.get_produk_services()
        for produk_service in produk_services:
            print(f"ID: {produk_service['id_produk_service']}, Nama: {produk_service['nama']}, Model: {produk_service['model']}, Harga: {produk_service['harga']}, Stok: {produk_service['stok']}")

        # Input pilihan pengguna
        id_produk_service = int(input("Masukkan ID Produk/Jasa yang akan dipilih: "))
        jumlah_beli_service = int(input("Masukkan Jumlah Beli/Service: "))

        # Periksa stok service
        selected_service = self.query.get_produk_service_by_id(id_produk_service)
        if jumlah_beli_service > selected_service['stok']:
            print("Jumlah pembelian melebihi stok service yang tersedia.")
            return
        elif jumlah_beli_service <= 0:
            print("Jumlah pembelian harus lebih dari 0.")
            return

        id_customer = int(input("Masukkan ID Customer: "))
        # Periksa keberadaan ID Customer
        if not self.query.check_customer_exists(id_customer):
            print("ID Customer tidak valid atau tidak ditemukan.")
            return
            
        nomor_kendaraan = input("Masukkan Nomor Kendaraan: ")
        nama_kendaraan = input("Masukkan Nama Kendaraan: ")
        keterangan = input("Masukkan Keterangan: ")
        tanggal_service = input("Masukkan Tanggal Service (YYYY-MM-DD): ")

        # Hitung total harga berdasarkan id_produk_service dan jumlah_beli_service
        total_harga = self.query.hitung_total_harga(id_produk_service, jumlah_beli_service)

        # Tampilkan struk pembelian/service beserta total harga
        print(f"\n=====Struk Pembelian/Service=====\n"
              f"ID Produk/Service: {id_produk_service}\n"
              f"Jumlah Beli/Service: {jumlah_beli_service}\n"
              f"Total Harga: {total_harga}")

        # Konfirmasi pembelian
        konfirmasi = input("Konfirmasi pembelian/service (y/n): ")
        if konfirmasi.lower() == 'y':
            # Perbarui tabel transaksi_service dan set status menjadi "Berhasil"
            self.query.insert_transaksi_service(id_customer, id_produk_service, nomor_kendaraan, nama_kendaraan, keterangan, total_harga, tanggal_service, "Berhasil")

            # Kurangi stok pada tabel produk_service
            self.query.update_stok_produk_service(id_produk_service, jumlah_beli_service)

            print("Pembelian/Service berhasil dicatat.")
        else:
            print("Pembelian/Service dibatalkan.")
          
    def tampilkan_transaksi_service(self):
        try:
            # Mendapatkan data pelanggan
            id_customer = input("Masukkan ID Customer untuk menampilkan transaksi service: ")
            if not self.query.check_customer_exists(id_customer):
                print("ID Customer tidak valid atau tidak ditemukan.")
                return

            # Menampilkan transaksi service berdasarkan ID customer
            transaksi_service_list = self.query.get_transaksi_service_by_customer(id_customer)

            if not transaksi_service_list:
                print(f"Tidak ada transaksi service untuk ID Customer {id_customer}.")
                return

            # Menampilkan hasil query dalam tabel
            print("\n===== Transaksi Service =====")
            table = PrettyTable()
            table.field_names = ["ID", "ID Customer", "ID Produk Service", "Nomor Kendaraan", "Nama Kendaraan", "Keterangan", "Total Service", "Tanggal Service", "Status"]

            for transaksi_service in transaksi_service_list:
                table.add_row([transaksi_service[0], transaksi_service[1], transaksi_service[2],
                               transaksi_service[3], transaksi_service[4], transaksi_service[5],
                               transaksi_service[6], transaksi_service[7], transaksi_service[8]])

            print(table)

        except Exception as e:
            print(f"Error: {e}")

    def tampilkan_seluruh_transaksi_service(self):
        try:
            # Menampilkan seluruh transaksi service
            transaksi_service_list = self.query.get_all_transaksi_service()

            if not transaksi_service_list:
                print("Tidak ada transaksi service yang tersedia.")
                return

            # Menampilkan hasil query dalam tabel
            print("\n===== Seluruh Transaksi Service =====")
            table = PrettyTable()
            table.field_names = ["ID", "ID Customer", "ID Produk Service", "Nomor Kendaraan", "Nama Kendaraan", "Keterangan", "Total Service", "Tanggal Service", "Status"]

            for transaksi_service in transaksi_service_list:
                table.add_row([transaksi_service[0], transaksi_service[1], transaksi_service[2],
                               transaksi_service[3], transaksi_service[4], transaksi_service[5],
                               transaksi_service[6], transaksi_service[7], transaksi_service[8]])

            print(table)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
    
