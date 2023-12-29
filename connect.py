import mysql.connector

class Database:
    def __init__(self, host="localhost", user="root", passwd="", database="db_dealer"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.connect()

    def connect(self):
        try:
            self.db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd
            )
            self.cur = self.db.cursor()

            # Pindahkan inisialisasi koneksi ke database ke sini
            self.db.database = self.database
            self.cur.execute(f"USE {self.database}")

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.create_database()
            else:
                raise

    def create_database(self):
        try:
            create_db_query = f"CREATE DATABASE {self.database}"
            create_db_cursor = self.db.cursor()
            create_db_cursor.execute(create_db_query)
            create_db_cursor.close()

            # Setelah membuat database, gunakan database yang baru dibuat
            self.db.database = self.database
            self.cur.execute(f"USE {self.database}")

        except mysql.connector.Error as err:
            print(f"Gagal membuat database: {err}")
            raise

    def create_tables(self):
        self.create_table_admin()
        self.create_table_customer()
        self.create_table_produk_mobil()
        self.create_table_produk_service()
        self.create_table_transaksi_pembelian_mobil()
        self.create_table_transaksi_service()

    def create_table_admin(self):
        query = '''
            CREATE TABLE IF NOT EXISTS admin (
                id_admin INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_customer(self):
        query = '''
            CREATE TABLE IF NOT EXISTS customer (
                id_customer INT AUTO_INCREMENT PRIMARY KEY,
                nama VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                telepon VARCHAR(15) NOT NULL,
                alamat VARCHAR(255) NOT NULL
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_produk_mobil(self):
        query = '''
            CREATE TABLE IF NOT EXISTS produk_mobil (
                id_mobil INT AUTO_INCREMENT PRIMARY KEY,
                merk VARCHAR(255) NOT NULL,
                model VARCHAR(255) NOT NULL,
                tahun INT NOT NULL,
                harga INT(10) NOT NULL,
                stok INT NOT NULL
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_produk_service(self):
        query = '''
            CREATE TABLE IF NOT EXISTS produk_service (
                id_produk_service INT AUTO_INCREMENT PRIMARY KEY,
                nama VARCHAR(255) NOT NULL,
                model VARCHAR(255) NOT NULL,
                harga INT(10) NOT NULL,
                stok INT NOT NULL
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_transaksi_service(self):
        query = '''
                CREATE TABLE IF NOT EXISTS transaksi_service (
                id_service INT AUTO_INCREMENT PRIMARY KEY,
                id_customer INT NOT NULL,
                id_produk_service INT NOT NULL,
                nomor_kendaraan VARCHAR(255) NOT NULL,
                nama_kendaraan VARCHAR(255) NOT NULL,
                keterangan TEXT,
                total_service INT(10) NOT NULL,
                tanggal_service DATE NOT NULL,
                status VARCHAR(50) NOT NULL,  
                FOREIGN KEY (id_customer) REFERENCES customer(id_customer),
                FOREIGN KEY (id_produk_service) REFERENCES produk_service(id_produk_service)
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def create_table_transaksi_pembelian_mobil(self):
        query = '''
            CREATE TABLE IF NOT EXISTS transaksi_pembelian_mobil (
                id_customer INT NOT NULL,
                id_mobil INT NOT NULL,
                jumlah INT NOT NULL,
                total_harga INT(10) NOT NULL,
                tanggal_pembelian DATE NOT NULL,
                status VARCHAR(20) NOT NULL,
                FOREIGN KEY (id_customer) REFERENCES customer(id_customer),
                FOREIGN KEY (id_mobil) REFERENCES produk_mobil(id_mobil)
            );
        '''
        self.cur.execute(query)
        self.db.commit()

    def close_connection(self):
        self.cur.close()
        self.db.close()

if __name__ == "__main__":
    db = Database()
    db.create_tables()
    db.close_connection()
