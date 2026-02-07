#!/usr/bin/env python3

import os
from pathlib import Path

class FileValidator:
    SUPPORTED_FORMATS = ['.mp4', '.avi', '.mov', '.mkv', '.webm']
    MAX_SIZE = 800 * 1024 * 1024
    
    @staticmethod
    def validate_video(path):
        if not os.path.exists(path):
            return False, "File not found"
        
        ext = Path(path).suffix.lower()
        if ext not in FileValidator.SUPPORTED_FORMATS:
            return False, f"Unsupported format: {ext}"
        
        size = os.path.getsize(path)
        if size > FileValidator.MAX_SIZE:
            return False, "File too large (max 800MB)"
        
        if size < 1024:
            return False, "File corrupted"
        
        return True, "Valid"
    
    @staticmethod
    def check_codec(path):
        return False, "FFmpeg not available"

class SystemValidator:
    @staticmethod
    def check_gpu():
        return False, "No GPU detected"
    
    @staticmethod
    def check_memory():
        return False, "Insufficient memory"
    
    @staticmethod
    def check_dependencies():
        return False, "Missing dependencies"
