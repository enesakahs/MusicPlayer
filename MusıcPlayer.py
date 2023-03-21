import tkinter as tk
import pygame
from tkinter.filedialog import askopenfilename
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Müzik Çalar")
        self.root.geometry("400x200")

        # Çalma listesi
        self.playlist = tk.Listbox(root, bg="black", fg="white", width=60, selectbackground="gray", selectforeground="black")
        self.playlist.pack(pady=10)

        # Müzik çaları başlat
        pygame.init()
        pygame.mixer.init()

        # Play butonu
        self.play_button = tk.Button(root, text="Oynat", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=10)

        # Duraklat butonu
        self.pause_button = tk.Button(root, text="Duraklat", command=self.pause_music)
        self.pause_button.pack(side=tk.LEFT)

        # İleri sar butonu
        self.forward_button = tk.Button(root, text="İleri Sar", command=self.forward_music)
        self.forward_button.pack(side=tk.LEFT)

        # Müzik ekle butonu
        self.add_button = tk.Button(root, text="Müzik Ekle", command=self.add_music)
        self.add_button.pack(side=tk.LEFT, padx=10)

        # Müzik sil butonu
        self.delete_button = tk.Button(root, text="Müzik Sil", command=self.delete_music)
        self.delete_button.pack(side=tk.LEFT)

    def add_music(self):
        # Dosya açma iletkisi
        music_file = askopenfilename(defaultextension=".mp3", filetypes=[("MP3 Dosyaları", "*.mp3"), ("Tüm Dosyalar", "*.*")])

        # Eğer bir dosya seçilmişse, çalma listesine ekle
        if music_file:
            self.playlist.insert(tk.END,music_file)

    def delete_music(self):
        # Seçilen müzik dosyasını çalma listesinden sil
        selected_music = self.playlist.curselection()
        self.playlist.delete(selected_music)

    def play_music(self):
        # Seçilen müzik dosyasını yükle ve çal
        selected_music = self.playlist.curselection()
        music_file = self.playlist.get(selected_music)
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()

    def pause_music(self):
        # Müzik çalmayı duraklat
        pygame.mixer.music.pause()

    def forward_music(self):
        # Müziği 5 saniye ileri sar
        current_pos = pygame.mixer.music.get_pos() // 1000
        pygame.mixer.music.set_pos(current_pos + 5)

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()

# Pygame'i kapat
pygame.quit()
