import tkinter as tk
from tkinter import ttk, messagebox
import time

# Fungsi untuk mengubah durasi Pomodoro
def set_pomodoro_duration():
    global pomodoro_duration
    pomodoro_duration = int(pomodoro_entry.get()) * 60

# Fungsi untuk mengubah durasi istirahat
def set_break_duration():
    global break_duration
    break_duration = int(break_entry.get()) * 60

# Fungsi untuk menghitung waktu Pomodoro
def start_pomodoro_timer():
    global is_break, remaining_seconds, running_timer
    if is_break:
        remaining_seconds = break_duration
        countdown(remaining_seconds, "Waktu Istirahat Selesai!\nMulai Pomodoro lagi?")
    else:
        remaining_seconds = pomodoro_duration
        countdown(remaining_seconds, "Pomodoro Selesai!\nWaktunya Istirahat!")

# Fungsi untuk menghitung waktu mundur
def countdown(seconds, message):
    global is_break, running_timer
    is_break = not is_break
    running_timer = True
    while seconds and running_timer:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=timeformat)
        root.update()
        time.sleep(1)
        seconds -= 1

    if running_timer:
        messagebox.showinfo("Pomodoro", message)

# Fungsi untuk menjeda atau melanjutkan timer
def toggle_pause():
    global running_timer
    running_timer = not running_timer

# Membuat jendela utama
root = tk.Tk()
root.title("Pomodoro Timer")

# Membuat tombol "Mulai Pomodoro"
start_button = tk.Button(root, text="Mulai Pomodoro", command=start_pomodoro_timer)
start_button.pack()

# Membuat input untuk mengatur durasi Pomodoro
pomodoro_label = tk.Label(root, text="Durasi Pomodoro (menit):")
pomodoro_label.pack()
pomodoro_entry = ttk.Entry(root)
pomodoro_entry.pack()
pomodoro_entry.insert(0, "25")  # Default durasi Pomodoro

# Membuat tombol "Terapkan" untuk durasi Pomodoro
pomodoro_button = ttk.Button(root, text="Terapkan", command=set_pomodoro_duration)
pomodoro_button.pack()

# Membuat input untuk mengatur durasi istirahat
break_label = tk.Label(root, text="Durasi Istirahat (menit):")
break_label.pack()
break_entry = ttk.Entry(root)
break_entry.pack()
break_entry.insert(0, "5")  # Default durasi istirahat

# Membuat tombol "Terapkan" untuk durasi istirahat
break_button = ttk.Button(root, text="Terapkan", command=set_break_duration)
break_button.pack()

# Membuat tampilan countdown
time_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
time_label.pack(pady=20)

# Membuat tombol "Jeda/Lanjutkan"
pause_button = tk.Button(root, text="Jeda/Lanjutkan", command=toggle_pause)
pause_button.pack()

# Inisialisasi variabel break, status timer, dan durasi default
is_break = False
running_timer = False
pomodoro_duration = 1500  # Default durasi Pomodoro (25 menit)
break_duration = 300     # Default durasi istirahat (5 menit)

root.mainloop()
