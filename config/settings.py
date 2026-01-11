#!/usr/bin/env python3

class Settings:
    APP_NAME = "Sora 2 Clean Pro"
    VERSION = "4.2.1"
    
    DEFAULT_ALGORITHM = "Sora 2 Signature Match"
    DEFAULT_QUALITY = "Maximum"
    DEFAULT_INPAINTING = "AI-Powered"
    
    MAX_FILE_SIZE = 800 * 1024 * 1024
    SUPPORTED_FORMATS = ['.mp4', '.avi', '.mov', '.mkv', '.webm']
    
    OUTPUT_DIR = "output"
    CACHE_DIR = "cache"
    MODELS_DIR = "models"
    
    GPU_ENABLED = True
    CUDA_DEVICE = 0
    
    DETECTION_THRESHOLD = 0.75
    INPAINTING_STRENGTH = 0.85
    
    @staticmethod
    def get_config():
        return {
            'app_name': Settings.APP_NAME,
            'version': Settings.VERSION,
            'gpu_enabled': Settings.GPU_ENABLED,
            'detection_threshold': Settings.DETECTION_THRESHOLD
        }
