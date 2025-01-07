import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.ttk import Progressbar
from tkinter import simpledialog
import yt_dlp as youtube_dl
import threading
from ftplib import FTP
import subprocess
import json

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Downloader")
        self.root.geometry("800x750")

        # Add scrollable frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self.main_frame)
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Load FTP credentials
        self.config_file = 'config.json'
        self.load_config()

        # Text Area for links
        tk.Label(self.scrollable_frame, text="Paste Video Links (one per line):").pack(pady=5)
        self.link_text = tk.Text(self.scrollable_frame, height=10)
        self.link_text.pack(pady=5, padx=10, fill=tk.BOTH)

        # Save As Button
        self.save_path = tk.StringVar()
        tk.Button(self.scrollable_frame, text="Save As (Local)", command=self.choose_save_path).pack(pady=5)
        tk.Label(self.scrollable_frame, textvariable=self.save_path).pack(pady=5)

        # FTP Details
        tk.Label(self.scrollable_frame, text="FTP Server:").pack(pady=5)
        tk.Label(self.scrollable_frame, text="Host:").pack()
        self.ftp_host = tk.Entry(self.scrollable_frame, width=50)
        self.ftp_host.insert(0, self.config.get('ftp_host', ''))
        self.ftp_host.pack(pady=2)

        tk.Label(self.scrollable_frame, text="Username:").pack()
        self.ftp_user = tk.Entry(self.scrollable_frame, width=50)
        self.ftp_user.insert(0, self.config.get('ftp_user', ''))
        self.ftp_user.pack(pady=2)

        tk.Label(self.scrollable_frame, text="Password:").pack()
        self.ftp_password = tk.Entry(self.scrollable_frame, width=50, show='*')
        self.ftp_password.insert(0, self.config.get('ftp_password', ''))
        self.ftp_password.pack(pady=2)

        self.ftp_directory = '/home/miclauscatalin/Downloads/ownvidown/'

        # Buttons
        tk.Button(self.scrollable_frame, text="Download", command=self.start_download).pack(pady=10)
        tk.Button(self.scrollable_frame, text="Update yt-dlp", command=self.update_yt_dlp).pack(pady=5)
        tk.Button(self.scrollable_frame, text="Start Over", command=self.restart_app).pack(pady=5)

        # Progress Bar Section
        self.progress_bars = []
        self.ftp_progress = []
        self.downloaded_links = set()

    def choose_save_path(self):
        path = filedialog.askdirectory()
        if path:
            self.save_path.set(path)

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = {}

    def save_config(self):
        self.config['ftp_host'] = self.ftp_host.get()
        self.config['ftp_user'] = self.ftp_user.get()
        self.config['ftp_password'] = self.ftp_password.get()
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file)

    def upload_to_ftp(self, file_path, index):
        try:
            self.ftp_progress[index].set(f"Uploading {os.path.basename(file_path)} to FTP...")
            self.root.update_idletasks()

            # Connect to FTP
            ftp = FTP(self.ftp_host.get(), timeout=30)
            ftp.login(user=self.ftp_user.get(), passwd=self.ftp_password.get())
            ftp.set_pasv(True)
            ftp.cwd(self.ftp_directory)

            # Upload file with progress
            with open(file_path, 'rb') as file:
                ftp.storbinary(f'STOR {os.path.basename(file_path)}', file)

            ftp.quit()

            # Remove file after successful upload
            os.remove(file_path)
            self.ftp_progress[index].set(f"Upload complete for {os.path.basename(file_path)}. File deleted locally.")
            self.root.update_idletasks()
        except Exception as e:
            self.ftp_progress[index].set(f"FTP upload failed for {os.path.basename(file_path)}.")
            messagebox.showerror("FTP Error", f"Failed to upload to FTP: {e}")

    def start_download(self):
        links = self.link_text.get("1.0", tk.END).strip().split('\n')
        save_path = self.save_path.get()

        if not links or not save_path:
            messagebox.showerror("Error", "Please provide video links and select save path.")
            return

        for i, link in enumerate(links):
            if link.strip() and link.strip() not in self.downloaded_links:
                self.downloaded_links.add(link.strip())
                self.create_progress_bar(i, link)
                threading.Thread(target=self.download_video, args=(link.strip(), save_path, i)).start()

    def create_progress_bar(self, index, link):
        tk.Label(self.scrollable_frame, text=f"Downloading: {link}").pack()
        pb = Progressbar(self.scrollable_frame, orient=tk.HORIZONTAL, length=500, mode='determinate')
        pb.pack(pady=5)
        self.progress_bars.append(pb)

        progress_text = tk.StringVar()
        progress_text.set("")
        tk.Label(self.scrollable_frame, textvariable=progress_text).pack()
        self.ftp_progress.append(progress_text)

    def download_video(self, url, save_path, index):
        def progress_hook(d):
            if d['status'] == 'downloading':
                percentage = ''.join(filter(str.isdigit, d['_percent_str']))
                self.progress_bars[index]['value'] = float(percentage)
                self.root.update_idletasks()

        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
                'progress_hooks': [progress_hook],
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0'
                }
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info_dict)

            self.upload_to_ftp(filename, index)
        except Exception as e:
            messagebox.showerror("Download Error", f"Failed to download {url}: {e}")

    def update_yt_dlp(self):
        subprocess.run(["pip", "install", "yt-dlp", "-U", "--break-system-packages"], check=True)

    def restart_app(self):
        self.root.destroy()
        subprocess.run(["python3", __file__])

if __name__ == '__main__':
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()
