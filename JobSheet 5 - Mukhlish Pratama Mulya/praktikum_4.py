class DataProcessor:
    def __init__(self, processor_id):
        self.processor_id = processor_id

    def process(self, *args, **kwargs):
        print(f"\n--- {self.processor_id} Memproses ---")
        if args: print(f"Posisi: {args}")
        if kwargs: print(f"Keyword: {kwargs}")

if __name__ == "__main__":
    dp = DataProcessor("DP-001")
    dp.process(10, 20, status="Aktif")