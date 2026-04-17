class BankAccount:
    def __init__(self, owner, balance):
        # Atribut dengan double underscore (__) dianggap "private" di Python
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        """Method untuk menambahkan saldo."""
        if amount > 0:
            self.__balance += amount
            print(f"Rp {amount:,} telah ditambahkan ke akun {self.__owner}.")
        else:
            print("Jumlah deposit harus lebih dari 0.")

    def withdraw(self, amount):
        """Method untuk menarik saldo."""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Rp {amount:,} telah ditarik dari akun {self.__owner}.")
        else:
            print("Saldo tidak mencukupi atau jumlah penarikan tidak valid.")

    def get_balance(self):
        """Method untuk mendapatkan informasi saldo terkini."""
        return self.__balance

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek BankAccount
    alice_account = BankAccount(owner="Alice", balance=1000000)

    # Deposit uang
    alice_account.deposit(500000)   # Berhasil
    alice_account.deposit(-100000)  # Gagal (validasi)

    # Withdraw uang
    alice_account.withdraw(300000)  # Berhasil
    alice_account.withdraw(2000000) # Gagal (saldo tidak cukup)

    # Mendapatkan saldo melalui method resmi
    current_balance = alice_account.get_balance()
    print(f"Saldo terakhir Alice: Rp {current_balance:,}")

    # Catatan: Mencoba mengakses alice_account.__balance secara langsung akan Error
    # karena Python melakukan 'Name Mangling' untuk melindungi atribut tersebut.