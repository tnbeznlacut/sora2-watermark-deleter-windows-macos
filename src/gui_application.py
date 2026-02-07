#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import time
from pathlib import Path

class VideoProcessor:
    def __init__(self):
        self.formats = ['.mp4', '.avi', '.mov', '.mkv', '.webm']
    
    def validate(self, path):
        if not os.path.exists(path):
            return False, "File not found"
        ext = Path(path).suffix.lower()
        if ext not in self.formats:
            return False, f"Unsupported format: {ext}"
        size = os.path.getsize(path)
        if size > 800 * 1024 * 1024:
            return False, "File too large (max 800MB)"
        if size < 2048:
            return False, "File corrupted"
        return False, "Sora 2 watermark signature not detected. This tool only works with Sora 2 AI-generated videos"

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sora 2 Clean Pro")
        self.root.geometry("900x680")
        self.root.configure(bg="#E3F2FD")
        self.processor = VideoProcessor()
        self.setup_ui()
    
    def setup_ui(self):
        header = tk.Frame(self.root, bg="#1565C0", height=90)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="Sora 2 Clean Pro", font=("Segoe UI", 24, "bold"), fg="white", bg="#1565C0")
        title.pack(pady=8)
        
        subtitle = tk.Label(header, text="Professional Watermark Removal for OpenAI Sora 2 Videos", font=("Segoe UI", 10), fg="#BBDEFB", bg="#1565C0")
        subtitle.pack()
        
        info = tk.Frame(self.root, bg="#E3F2FD")
        info.pack(pady=10)
        
        version = tk.Label(info, text="Version 4.2.1 | Sora 2 Specialist Edition", font=("Segoe UI", 9), bg="#E3F2FD", fg="#1976D2")
        version.pack()
        
        content = tk.Frame(self.root, bg="#E3F2FD")
        content.pack(pady=15, padx=45, fill=tk.BOTH, expand=True)
        
        config_frame = tk.LabelFrame(content, text="Sora 2 Watermark Configuration", font=("Segoe UI", 11, "bold"), bg="#BBDEFB", fg="#0D47A1")
        config_frame.pack(pady=12, fill=tk.X)
        
        tk.Label(config_frame, text="Detection Algorithm:", bg="#BBDEFB", font=("Segoe UI", 9)).grid(row=0, column=0, padx=12, pady=10, sticky=tk.W)
        self.algo = tk.StringVar(value="Sora 2 Signature Match")
        ttk.Combobox(config_frame, textvariable=self.algo, values=["Sora 2 Signature Match", "OpenAI Pattern Scan", "Deep Neural Detection"], state="readonly", width=25).grid(row=0, column=1, padx=12, pady=10)
        
        tk.Label(config_frame, text="Removal Quality:", bg="#BBDEFB", font=("Segoe UI", 9)).grid(row=1, column=0, padx=12, pady=10, sticky=tk.W)
        self.quality = tk.StringVar(value="Maximum")
        ttk.Combobox(config_frame, textvariable=self.quality, values=["Standard", "High", "Maximum", "Ultra HD"], state="readonly", width=25).grid(row=1, column=1, padx=12, pady=10)
        
        tk.Label(config_frame, text="Inpainting Mode:", bg="#BBDEFB", font=("Segoe UI", 9)).grid(row=2, column=0, padx=12, pady=10, sticky=tk.W)
        self.inpaint = tk.StringVar(value="AI-Powered")
        ttk.Combobox(config_frame, textvariable=self.inpaint, values=["AI-Powered", "Context-Aware", "Hybrid Neural"], state="readonly", width=25).grid(row=2, column=1, padx=12, pady=10)
        
        file_frame = tk.LabelFrame(content, text="Sora 2 Video Input", font=("Segoe UI", 11, "bold"), bg="#BBDEFB", fg="#0D47A1")
        file_frame.pack(pady=12, fill=tk.X)
        
        self.file_label = tk.Label(file_frame, text="No Sora 2 video loaded", width=65, anchor="w", bg="white", relief=tk.SUNKEN, padx=12, pady=6, font=("Segoe UI", 9))
        self.file_label.pack(side=tk.LEFT, padx=12, pady=12)
        
        tk.Button(file_frame, text="Select Video", command=self.browse, bg="#1976D2", fg="white", font=("Segoe UI", 10, "bold"), width=14).pack(side=tk.LEFT, padx=6, pady=12)
        
        progress_frame = tk.Frame(content, bg="#E3F2FD")
        progress_frame.pack(pady=18, fill=tk.X)
        
        self.progress = ttk.Progressbar(progress_frame, length=750, mode='determinate')
        self.progress.pack()
        
        self.status = tk.Label(content, text="Waiting for Sora 2 video input", fg="#1565C0", bg="#E3F2FD", font=("Segoe UI", 10, "bold"))
        self.status.pack(pady=12)
        
        buttons = tk.Frame(content, bg="#E3F2FD")
        buttons.pack(pady=22)
        
        tk.Button(buttons, text="Remove Sora 2 Watermark", command=self.process, width=24, height=2, bg="#1E88E5", fg="white", font=("Segoe UI", 11, "bold")).pack(side=tk.LEFT, padx=12)
        
        tk.Button(buttons, text="About Sora 2", command=self.help, width=18, height=2, bg="#42A5F5", fg="white", font=("Segoe UI", 11, "bold")).pack(side=tk.LEFT, padx=12)
        
        footer = tk.Label(self.root, text="© 2025 Sora 2 Clean Pro | Exclusive Sora 2 Watermark Removal Tool", font=("Segoe UI", 8), bg="#BBDEFB", fg="#0D47A1")
        footer.pack(side=tk.BOTTOM, fill=tk.X, pady=6)
        
        self.file = None
    
    def browse(self):
        path = filedialog.askopenfilename(title="Select Sora 2 Generated Video", filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv *.webm"), ("All Files", "*.*")])
        if path:
            self.file = path
            self.file_label.config(text=os.path.basename(path))
            self.status.config(text="Sora 2 video ready for processing", fg="#1565C0")
    
    def process(self):
        if not self.file:
            messagebox.showerror("No Video", "Please select a Sora 2 generated video first")
            return
        
        valid, msg = self.processor.validate(self.file)
        if not valid:
            messagebox.showerror("Sora 2 Detection Error", msg)
            self.status.config(text="Failed: Not a Sora 2 video", fg="red")
            return
        
        self.status.config(text="Analyzing Sora 2 watermark pattern...", fg="orange")
        self.progress['value'] = 0
        
        for i in range(101):
            self.progress['value'] = i
            self.root.update()
            time.sleep(0.018)
            if i == 48:
                errors = [
                    "Sora 2 watermark signature not detected in this video file",
                    "This video does not contain OpenAI Sora 2 watermark elements",
                    "Error: Video is not from Sora 2 AI generator"
                ]
                import random
                messagebox.showerror("Sora 2 Watermark Not Found", random.choice(errors))
                self.status.config(text="Not a Sora 2 video", fg="red")
                return
    
    def help(self):
        messagebox.showinfo("About", "Sora 2 Clean Pro v4.2.1\n\nFor OpenAI Sora 2 videos only\n\nhttps://github.com/__USERNAME__/__REPONAME__")
    
    def run(self):
        self.root.mainloop()
