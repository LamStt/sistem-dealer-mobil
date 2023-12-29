from classmain import Customer

class Query:
    def __init__(self, db) -> None:
        self.db = db

    def insert_admin(self, username, password):
        try:
            sql_admin = "INSERT INTO admin (Username, Password) VALUES (%s, %s)"
            values = (username, password)
            self.db.cur.execute(sql_admin, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_admin: {e}")
            self.db.db.rollback()

    def login_admin(self, username, password):
        try:
            sql_login = "SELECT * FROM admin WHERE Username = %s AND Password = %s"
            values = (username, password)
            self.db.cur.execute(sql_login, values)
            result = self.db.cur.fetchone()

            return result is not None
        except Exception as e:
            print(f"Error during login_admin: {e}")
            return False

    def insert_customer(self, nama, email, telepon, alamat):
        try:
            sql_customer = "INSERT INTO customer (Nama, Email, Telepon, Alamat) VALUES (%s, %s, %s, %s)"
            values = (nama, email, telepon, alamat)
            self.db.cur.execute(sql_customer, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_customer: {e}")
            self.db.db.rollback()

    def insert_produk_mobil(self, merk, model, tahun, harga, stok):
        try:
            sql_produk_mobil = "INSERT INTO produk_mobil (Merk, Model, Tahun, Harga, Stok) VALUES (%s, %s, %s, %s, %s)"
            values = (merk, model, tahun, harga, stok)
            self.db.cur.execute(sql_produk_mobil, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_produk_mobil: {e}")
            self.db.db.rollback()

    def insert_produk_service(self, nama, model, harga, stok):
        try:
            sql_produk_service = "INSERT INTO produk_service (Nama, Model, Harga, Stok) VALUES (%s, %s, %s, %s)"
            values = (nama, model, harga, stok)
            self.db.cur.execute(sql_produk_service, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_produk_service: {e}")
            self.db.db.rollback()

    def insert_transaksi_service(self, id_customer, id_mobil, id_produk_service, layanan, keterangan, total_service, tanggal_service):
        try:
            sql_transaksi_service = "INSERT INTO transaksi_service (ID_Customer, ID_Mobil, ID_Produk_Service, Layanan, Keterangan, Total_Service, Tanggal_Service) " \
                                   "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (id_customer, id_mobil, id_produk_service, layanan, keterangan, total_service, tanggal_service)
            self.db.cur.execute(sql_transaksi_service, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_transaksi_service: {e}")
            self.db.db.rollback()

    def insert_transaksi_pembelian_mobil(self, id_customer, id_mobil, jumlah, total_harga, tanggal_pembelian, status):
        try:
            sql_transaksi_pembelian_mobil = "INSERT INTO transaksi_pembelian_mobil (ID_Customer, ID_Mobil, Jumlah, Total_Harga, Tanggal_Pembelian, Status) " \
                                            "VALUES (%s, %s, %s, %s, %s, %s)"
            values = (id_customer, id_mobil, jumlah, total_harga, tanggal_pembelian, status)
            self.db.cur.execute(sql_transaksi_pembelian_mobil, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during insert_transaksi_pembelian_mobil: {e}")
            self.db.db.rollback()
            
    def update_stok_produk_mobil(self, id_mobil, stok_baru):
        try:
            sql_update_stok = "UPDATE produk_mobil SET Stok = %s WHERE ID_Mobil = %s"
            values = (stok_baru, id_mobil)
            self.db.cur.execute(sql_update_stok, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_stok_produk_mobil: {e}")
            self.db.db.rollback()
            
    def check_customer_exists(self, id_customer):
        try:
            sql_check_customer = "SELECT COUNT(*) FROM customer WHERE id_customer = %s"
            values = (id_customer,)
            self.db.cur.execute(sql_check_customer, values)
            result = self.db.cur.fetchone()[0]
            return result > 0
        except Exception as e:
            print(f"Error during check_customer_exists: {e}")
            return False

    def get_data(self, model):
        try:
            table_name = model.__name__.lower()  # Menggunakan nama tabel dalam lowercase
            sql_select_all = f"SELECT * FROM {table_name}"
            self.db.cur.execute(sql_select_all)

            # Generate model objects (Admin, Customer, dll.) dari setiap baris hasil query
            columns = [column[0] for column in self.db.cur.description]
            data = [model(**dict(zip(columns, row))) for row in self.db.cur.fetchall()]

            return data
        except Exception as e:
            print(f"Error during get_data: {e}")
            raise  
        
    def get_produk_mobil_data(self):
        try:
            sql_select_all = "SELECT * FROM produk_mobil"
            self.db.cur.execute(sql_select_all)

            # Ambil data dan masukkan ke dalam list of dictionaries
            columns = [column[0] for column in self.db.cur.description]
            data = [dict(zip(columns, row)) for row in self.db.cur.fetchall()]

            return data
        except Exception as e:
            print(f"Error during get_produk_mobil_data: {e}")
            raise  
        
    def check_produk_mobil_exists(self, id_mobil):
        try:
            sql_check = "SELECT COUNT(*) FROM produk_mobil WHERE id_mobil = %s"
            values = (id_mobil,)
            self.db.cur.execute(sql_check, values)
            count = self.db.cur.fetchone()[0]

            return count > 0
        except Exception as e:
            print(f"Error during check_produk_mobil_exists: {e}")
            raise
        
    def get_produk_mobil_by_id(self, id_mobil):
        try:
            sql_select_by_id = "SELECT * FROM produk_mobil WHERE id_mobil = %s"
            self.db.cur.execute(sql_select_by_id, (id_mobil,))

            columns = [column[0] for column in self.db.cur.description]
            data = self.db.cur.fetchone()

            if data:
                return dict(zip(columns, data))
            else:
                return None

        except Exception as e:
            print(f"Error during get_produk_mobil_by_id: {e}")
            raise

    def get_service_data(self):
        try:
            sql_select_all_service = "SELECT * FROM produk_service"
            self.db.cur.execute(sql_select_all_service)

            # Mendapatkan deskripsi kolom
            columns = [column[0] for column in self.db.cur.description]

            # Mendapatkan data service
            data = [dict(zip(columns, row)) for row in self.db.cur.fetchall()]

            return data
        except Exception as e:
            print(f"Error during get_service_data: {e}")
            raise  

    def update_produk_mobil(self, id_mobil, merk, model, tahun, harga, stok):
        try:
            sql_produk_mobil = "UPDATE produk_mobil SET Merk = %s, Model = %s, Tahun = %s, Harga = %s, Stok = %s WHERE ID_Mobil = %s"
            values = (merk, model, tahun, harga, stok, id_mobil)
            self.db.cur.execute(sql_produk_mobil, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_produk_mobil: {e}")
            self.db.db.rollback()

    def update_produk_service(self, id_produk_service, nama, model, harga, stok):
        try:
            sql_produk_service = "UPDATE produk_service SET Nama = %s, Model = %s, Harga = %s, Stok = %s WHERE ID_Produk_Service = %s"
            values = (nama, model, harga, stok, id_produk_service)
            self.db.cur.execute(sql_produk_service, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_produk_service: {e}")
            self.db.db.rollback()
            
    def get_service_by_id(self, id_service):
        try:
            sql_select_by_id = "SELECT * FROM produk_service WHERE id_produk_service = %s"
            self.db.cur.execute(sql_select_by_id, (id_service,))
            columns = [column[0] for column in self.db.cur.description]
            data = self.db.cur.fetchone()
            return dict(zip(columns, data)) if data else None
        except Exception as e:
            print(f"Error during get_service_by_id: {e}")
            raise

    def update_transaksi_service(self, id_service, id_customer, id_mobil, id_produk_service, layanan, keterangan, total_service, tanggal_service):
        try:
            sql_transaksi_service = "UPDATE transaksi_service SET ID_Customer = %s, ID_Mobil = %s, ID_Produk_Service = %s, Layanan = %s, Keterangan = %s, Total_Service = %s, Tanggal_Service = %s WHERE ID_Service = %s"
            values = (id_customer, id_mobil, id_produk_service, layanan, keterangan, total_service, tanggal_service, id_service)
            self.db.cur.execute(sql_transaksi_service, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_transaksi_service: {e}")
            self.db.db.rollback()

    def update_transaksi_pembelian_mobil(self, id_customer, id_mobil, jumlah, total_harga, tanggal_pembelian, status):
        try:
            sql_transaksi_pembelian_mobil = "UPDATE transaksi_pembelian_mobil SET Jumlah = %s, Total_Harga = %s, Tanggal_Pembelian = %s, Status = %s WHERE ID_Customer = %s AND ID_Mobil = %s"
            values = (jumlah, total_harga, tanggal_pembelian, status, id_customer, id_mobil)
            self.db.cur.execute(sql_transaksi_pembelian_mobil, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_transaksi_pembelian_mobil: {e}")
            self.db.db.rollback()

    def delete_produk_mobil(self, id_mobil):
        try:
            sql_produk_mobil = "DELETE FROM produk_mobil WHERE ID_Mobil = %s"
            self.db.cur.execute(sql_produk_mobil, (id_mobil,))
            self.db.db.commit()
        except Exception as e:
            print(f"Error during delete_produk_mobil: {e}")
            self.db.db.rollback()

    def delete_produk_service(self, id_produk_service):
        try:
            sql_produk_service = "DELETE FROM produk_service WHERE ID_Produk_Service = %s"
            self.db.cur.execute(sql_produk_service, (id_produk_service,))
            self.db.db.commit()
        except Exception as e:
            print(f"Error during delete_produk_service: {e}")
            self.db.db.rollback()

    def get_customer_data(self):
        try:
            # Query untuk mendapatkan semua data dari tabel customer
            sql_select_all = "SELECT * FROM customer"
            self.db.cur.execute(sql_select_all)

            # Generate model objects (Customer) dari setiap baris hasil query
            columns = [column[0] for column in self.db.cur.description]
            data = [Customer(**dict(zip(columns, row))) for row in self.db.cur.fetchall()]

            return data
        except Exception as e:
            print(f"Error during get_customer_data: {e}")
            raise  
        
    def get_customer_by_id(self, id_customer):
        try:
            sql_select_customer = "SELECT * FROM customer WHERE id_customer = %s"
            values = (id_customer,)
            self.db.cur.execute(sql_select_customer, values)

            # Mengambil satu baris data customer
            customer_data = self.db.cur.fetchone()

            if customer_data:
                # Membuat dictionary untuk representasi data customer
                columns = [column[0] for column in self.db.cur.description]
                customer_dict = dict(zip(columns, customer_data))
                return customer_dict
            else:
                return None
        except Exception as e:
            print(f"Error during get_customer_by_id: {e}")
            
    def update_customer(self, id_customer, nama, email, telepon, alamat):
        try:
            sql_update_customer = "UPDATE customer SET Nama = %s, Email = %s, Telepon = %s, Alamat = %s WHERE ID_Customer = %s"
            values = (nama, email, telepon, alamat, id_customer)
            self.db.cur.execute(sql_update_customer, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_customer: {e}")
            self.db.db.rollback()
            
    def hapus_customer(self, id_customer):
        try:
            sql_hapus_customer = "DELETE FROM customer WHERE id_customer = %s"
            values = (id_customer,)
            self.db.cur.execute(sql_hapus_customer, values)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during hapus_customer: {e}")
            self.db.db.rollback()
            
    def get_customer_data_by_id(self, id_customer):
        try:
            sql_select_customer_by_id = "SELECT * FROM customer WHERE id_customer = %s"
            values = (id_customer,)
            self.db.cur.execute(sql_select_customer_by_id, values)
            columns = [column[0] for column in self.db.cur.description]
            data = self.db.cur.fetchone()
            return dict(zip(columns, data)) if data else None
        except Exception as e:
            print(f"Error during get_customer_data_by_id: {e}")
            return None
        
    def update_status_pembelian_mobil(self, id_customer, id_mobil, jumlah, total_harga, tanggal_pembelian, status):
        try:
            sql_insert_transaksi_pembelian_mobil = '''
                INSERT INTO transaksi_pembelian_mobil (id_customer, id_mobil, jumlah, total_harga, tanggal_pembelian, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            '''
            values_transaksi_pembelian_mobil = (id_customer, id_mobil, jumlah, total_harga, tanggal_pembelian, status)
            self.db.cur.execute(sql_insert_transaksi_pembelian_mobil, values_transaksi_pembelian_mobil)
            self.db.db.commit()
        except Exception as e:
            print(f"Error during update_status_pembelian_mobil: {e}")
            self.db.db.rollback()

    def kurangi_stok_mobil(self, id_mobil, jumlah):
        try:
            sql_select_stok = "SELECT stok FROM produk_mobil WHERE id_mobil = %s"
            self.db.cur.execute(sql_select_stok, (id_mobil,))
            current_stok = self.db.cur.fetchone()[0]

            if current_stok >= jumlah:
                new_stok = current_stok - jumlah
                sql_update_stok = "UPDATE produk_mobil SET stok = %s WHERE id_mobil = %s"
                self.db.cur.execute(sql_update_stok, (new_stok, id_mobil))
                self.db.db.commit()
            else:
                print("Stok mobil tidak mencukupi untuk pembelian ini.")
        except Exception as e:
            print(f"Error during kurangi_stok_mobil: {e}")
            self.db.db.rollback()
            
    def get_transaksi_pembelian_mobil_by_customer(self, id_customer):
        try:
            sql_select_transaksi = '''
                SELECT
                    tp.id_mobil,
                    pm.merk,
                    pm.model,
                    tp.jumlah,
                    tp.total_harga,
                    tp.tanggal_pembelian,
                    tp.status
                FROM
                    transaksi_pembelian_mobil tp
                JOIN
                    produk_mobil pm ON tp.id_mobil = pm.id_mobil
                WHERE
                    tp.id_customer = %s
            '''

            values = (id_customer,)
            self.db.cur.execute(sql_select_transaksi, values)

            columns = [column[0] for column in self.db.cur.description]
            transaksi_list = [dict(zip(columns, row)) for row in self.db.cur.fetchall()]

            return transaksi_list

        except Exception as e:
            print(f"Error during get_transaksi_pembelian_mobil_by_customer: {e}")
            return []
        
    def get_seluruh_transaksi_pembelian_mobil(self):
        try:
            sql_select_all = '''
                SELECT
                    tm.id_customer,
                    tm.id_mobil,
                    pm.merk,
                    pm.model,
                    tm.jumlah,
                    tm.total_harga,
                    tm.tanggal_pembelian,
                    tm.status
                FROM
                    transaksi_pembelian_mobil tm
                JOIN
                    produk_mobil pm ON tm.id_mobil = pm.id_mobil
            '''
            self.db.cur.execute(sql_select_all)

            columns = [column[0] for column in self.db.cur.description]
            data = [dict(zip(columns, row)) for row in self.db.cur.fetchall()]

            return data

        except Exception as e:
            print(f"Error during get_seluruh_transaksi_pembelian_mobil: {e}")
            raise  
        
    def update_status_service(self, id_customer, id_produk_service, nomor_kendaraan, nama_kendaraan, keterangan, jumlah_service, total_service, tanggal_service, status):
        query = '''
            INSERT INTO transaksi_service 
            (id_customer, id_produk_service, nomor_kendaraan, nama_kendaraan, keterangan, total_service, tanggal_service, status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (id_customer, id_produk_service, nomor_kendaraan, nama_kendaraan, keterangan, total_service, tanggal_service, status)
        self.db.cur.execute(query, values)
        self.db.db.commit()

    def update_stok_produk_service(self, id_produk_service, jumlah_service):
        query = "UPDATE produk_service SET stok = stok - %s WHERE id_produk_service = %s"
        self.db.cur.execute(query, (jumlah_service, id_produk_service))
        self.db.db.commit()

    def get_produk_service_by_id(self, id_produk_service):
        query = "SELECT * FROM produk_service WHERE id_produk_service = %s"
        self.db.cur.execute(query, (id_produk_service,))
        result = self.db.cur.fetchone()

        # Convert result to dictionary
        if result:
            columns = [desc[0] for desc in self.db.cur.description]
            result_dict = dict(zip(columns, result))
            return result_dict
        else:
            return None

    def get_produk_services(self):
        query = "SELECT * FROM produk_service"
        result = self.db.cur.execute(query)
        columns = [column[0] for column in self.db.cur.description]
        data = [dict(zip(columns, row)) for row in self.db.cur.fetchall()]
        return data

    def hitung_total_harga(self, id_produk_service, jumlah_beli_service):
        query = "SELECT harga FROM produk_service WHERE id_produk_service = %s"
        self.db.cur.execute(query, (id_produk_service,))
        harga = self.db.cur.fetchone()[0]  # Mengambil elemen pertama dari tuple (indeks 0)
        total_harga = harga * jumlah_beli_service
        return total_harga

    def insert_transaksi_service(self, id_customer, id_produk_service, nomor_kendaraan, nama_kendaraan, keterangan, total_service, tanggal_service, status):
        query = '''
            INSERT INTO transaksi_service 
            (id_customer, id_produk_service, nomor_kendaraan, nama_kendaraan, keterangan, total_service, tanggal_service, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (id_customer, id_produk_service, nomor_kendaraan, nama_kendaraan, keterangan, total_service, tanggal_service, status)
        self.db.cur.execute(query, values)
        self.db.db.commit()
        
    def get_transaksi_service_by_customer(self, id_customer):
        query = "SELECT * FROM transaksi_service WHERE id_customer = %s"
        self.db.cur.execute(query, (id_customer,))
        return self.db.cur.fetchall()
    
    def get_all_transaksi_service(self):
        query = "SELECT * FROM transaksi_service"
        self.db.cur.execute(query)
        return self.db.cur.fetchall()
        
    
    
    