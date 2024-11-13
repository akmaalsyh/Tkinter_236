import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input, menghitung rata-rata, dan menentukan prodi
def hasil_prediksi():
    try:
        total_nilai = 0  # Inisialisasi variabel untuk jumlah total nilai
        for entry in entries:
            nilai = int(entry.get())  # Mengonversi input menjadi integer
            if not (0 <= nilai <= 100):  # Memastikan nilai antara 0-100
                raise ValueError("Nilai harus antara 0 dan 100.")
            total_nilai += nilai  # Menambahkan nilai ke total

        # Menghitung rata-rata nilai
        rata_rata = total_nilai / len(entries)
        
        # Menentukan prodi berdasarkan rata-rata nilai
        if rata_rata >= 80:
            prodi = "Teknologi Informasi"
        elif 60 <= rata_rata < 80:
            prodi = "Pendidikan Bahasa"
        elif 50 <= rata_rata < 60:
            prodi = "Pertanian"
        else:
            prodi = "Tidak ada prodi yang cocok"
        
        # Menampilkan prodi dan rata-rata pada label hasil
        hasil_label.config(text=f"Prediksi Prodi: {prodi} (Rata-rata: {rata_rata:.2f})")
        
    except ValueError as ve:
        # Menampilkan pesan error jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul aplikasi
root.geometry("500x600")  # Ukuran jendela utama
root.configure(bg="#f0f0f0")  # Warna latar belakang

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)  # Padding vertikal untuk judul

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)  # Padding untuk frame input

entries = []  # Daftar untuk menyimpan entri nilai
for i in range(10):
    # Label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label pada kolom pertama
    
    # Entry untuk input nilai mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan entry pada kolom kedua
    entries.append(entry)  # Menyimpan entry ke dalam list untuk diakses nanti

# Tombol untuk memproses hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)  # Padding vertikal untuk tombol

# Label untuk menampilkan hasil prediksi prodi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)  # Padding vertikal untuk label hasil

# Menjalankan aplikasi
root.mainloop()
