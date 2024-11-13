import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try: 
        # Memeriksa setiap input nilai
        for entry in entries:
            nilai = int(entry.get())  # Mengonversi input ke integer
            if not (0 <= nilai <= 100):  # Validasi nilai 0-100
                raise ValueError("Nilai harus antara 0 dan 100.")
        # Jika valid, tampilkan hasil prediksi
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError:
        # Menampilkan pesan error jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul jendela
root.geometry("500x600")  # Ukuran jendela
root.configure(bg="#7cc1e4")  # Warna latar belakang

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 18, "bold"), bg="#3c4292", fg="white")
judul_label.pack(pady=20)  # Menambahkan padding di sekitar judul

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#044a2e")  # Frame untuk input
frame_input.pack(pady=10)

entries = []  # Daftar untuk menyimpan entry nilai
for i in range(10):
    # Label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Times New Roman", 12), bg="#044a2e", fg="white")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Penempatan label
    
    # Entry untuk input nilai
    entry = tk.Entry(frame_input, width=10, font=("Times new roman", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Penempatan entry
    entries.append(entry)  # Menyimpan entry ke dalam list

# Tombol untuk memproses hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Times new roman", 12, "bold"), bg="#4CAF50", fg="white")
prediksi_button.pack(pady=30)  # Padding di sekitar tombol

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("imes new roman", 14, "italic", "bold"), fg="blue", bg="#7cc1e4")
hasil_label.pack(pady=20)  # Padding di sekitar label hasil

# Menjalankan aplikasi
root.mainloop()
