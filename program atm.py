import sys

# Data pengguna: no rekening, pin, dan saldo
data_pengguna = {
    "234567": {"pin": 1234, "saldo": 1000000},
    "890123": {"pin": 5678, "saldo": 500000},
    "456789": {"pin": 9012, "saldo": 100000}
}

# Fungsi untuk mengecek saldo
def cek_saldo(nomor_rekening):
    print("-----------------------------------------------")
    print(f"Saldo anda saat ini: Rp.{data_pengguna[nomor_rekening]['saldo']}")
    print("-----------------------------------------------")

# Fungsi untuk tarik tunai
def tarik_tunai(nomor_rekening):
    try:
        jumlah = int(input("Masukkan jumlah yang ingin ditarik: Rp. "))
        if data_pengguna[nomor_rekening]['saldo'] >= jumlah:
            data_pengguna[nomor_rekening]['saldo'] -= jumlah
            print("---------------------------------------------------")
            print(f"Penarikan berhasil! Saldo anda sekarang: Rp.{data_pengguna[nomor_rekening]['saldo']}")
            print("---------------------------------------------------")
        else:
            print("Maaf, saldo anda tidak mencukupi")
    except ValueError:
        print("Jumlah harus berupa angka.")

# Fungsi untuk setor tunai
def setor_tunai(nomor_rekening):
    try:
        jumlah = int(input("Masukkan jumlah setor tunai: Rp. "))
        data_pengguna[nomor_rekening]['saldo'] += jumlah
        print("----------------------------------------------------------------------------------")
        print(f"Setor tunai berhasil! Anda menambahkan Rp.{jumlah}. Saldo anda sekarang: Rp.{data_pengguna[nomor_rekening]['saldo']}")
        print("----------------------------------------------------------------------------------")
    except ValueError:
        print("Jumlah harus berupa angka.")

# Fungsi untuk transfer uang
def transfer_uang(nomor_rekening_pengirim):
    try:
        nomor_rekening_tujuan = input("Masukkan nomor rekening tujuan: ")
        if nomor_rekening_tujuan not in data_pengguna:
            print("Nomor rekening tujuan tidak ditemukan.")
            return

        jumlah = int(input("Masukkan jumlah yang ingin ditransfer: Rp. "))
        if data_pengguna[nomor_rekening_pengirim]['saldo'] >= jumlah:
            data_pengguna[nomor_rekening_pengirim]['saldo'] -= jumlah
            data_pengguna[nomor_rekening_tujuan]['saldo'] += jumlah
            print("-----------------------------------------------")
            print("Transfer berhasil!")
            print(f"Saldo Anda sekarang: Rp.{data_pengguna[nomor_rekening_pengirim]['saldo']}")
            print("-----------------------------------------------")
        else:
            print("Maaf, saldo anda tidak mencukupi")
    except ValueError:
        print("Jumlah harus berupa angka.")

# Login pengguna
def login():
    while True:
        print("|=============================================|")
        print("|   Selamat Datang Di Program ATM Sederhana   |")
        print("|=============================================|")
        nomor_rekening = input("Masukkan nomor rekening : ")
        try:
            PIN = int(input("Masukkan PIN : "))
            if nomor_rekening in data_pengguna and PIN == data_pengguna[nomor_rekening]["pin"]:
                print("-----------------------------------------------")
                print("Login berhasil!")
                print("-----------------------------------------------")
                return nomor_rekening
            else:
                print("-----------------------------------------------")
                print("Nomor Rekening atau PIN salah.")
                print("-----------------------------------------------")
        except ValueError:
            print("-----------------------------------------------")
            print("Nomor rekening dan PIN harus berupa angka!")
            print("-----------------------------------------------")
        except KeyboardInterrupt:
            print("\n-> Terjadi kesalahan input. Program telah dihentikan.")
            sys.exit(0)

# Menu ATM
def menu_atm():
    nomor_rekening = login()
    while True:
        try:
            print("|=============================================|")
            print("|   Selamat Datang Di Program ATM Sederhana   |")
            print("|=============================================|")
            print("| [1]. Cek Saldo                              |")
            print("| [2]. Tarik Tunai                            |")
            print("| [3]. Setor Tunai                            |")
            print("| [4]. Transfer Uang                          |")
            print("| [5]. Keluar                                 |")
            print("|=============================================|")
            pilihan = int(input("Pilih menu (1/2/3/4/5): "))

            if pilihan == 1:
                cek_saldo(nomor_rekening)
            elif pilihan == 2:
                tarik_tunai(nomor_rekening)
            elif pilihan == 3:
                setor_tunai(nomor_rekening)
            elif pilihan == 4:
                transfer_uang(nomor_rekening)
            elif pilihan == 5:
                print("-----------------------------------------------")
                print("Terima Kasih Telah Menggunakan ATM Kami ^-^")
                print("-----------------------------------------------")
                break
            else:
                print("Nomor pilihan tidak ada. Silahkan coba lagi.")
        except ValueError:
            print("Input tidak valid. Pilihan harus berupa angka 1-5.")
        except KeyboardInterrupt:
            print("\n-> Terjadi kesalahan input. Program telah dihentikan.")
            break

# Jalankan aplikasi ATM
if __name__ == "__main__":
    try:
        menu_atm()
    except KeyboardInterrupt:
        print("\n-> Terjadi kesalahan input. Program telah dihentikan.")
        sys.exit(0)