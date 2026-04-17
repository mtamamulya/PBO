class Employee:
    def __init__(self, name, salary):
        # Atribut privat dengan double underscore (__)
        # Ini mencegah akses atau perubahan langsung dari luar kelas
        self.__name = name
        self.__salary = salary

    def update_salary(self, increase):
        """Method untuk menaikkan gaji dengan validasi."""
        if increase > 0:
            self.__salary += increase
            print(f"Gaji telah dinaikkan sebesar {increase}.")
        else:
            print("Nilai kenaikan harus lebih dari 0.")

    def set_salary(self, new_salary):
        """Method untuk mengubah gaji dengan validasi."""
        if new_salary >= 0:
            self.__salary = new_salary
            print(f"Gaji diatur ulang menjadi {new_salary}.")
        else:
            print("Gaji tidak dapat bernilai negatif.")

    def get_salary(self):
        """Method untuk mendapatkan informasi gaji."""
        return self.__salary

    def get_employee_info(self):
        """Method untuk menampilkan informasi karyawan secara menyeluruh."""
        return f"Employee: {self.__name}, Gaji: {self.__salary}"

# --- Contoh Penggunaan ---
if __name__ == "__main__":
    # Membuat objek Employee
    employee1 = Employee("John Doe", 50000)

    # Tampilkan informasi awal
    print(employee1.get_employee_info())

    # Update gaji (Kenaikan)
    employee1.update_salary(5000)
    print(f"Gaji setelah kenaikan: {employee1.get_salary()}")

    # Atur ulang gaji (Overwriting)
    employee1.set_salary(60000)
    print(f"Informasi terbaru: {employee1.get_employee_info()}")

    # CATATAN:
    # print(employee1.__salary) # Ini akan menyebabkan AttributeError