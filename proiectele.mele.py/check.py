import subprocess
import sys

def install_packages():
    """Instalează toate pachetele necesare"""
    packages = [
        'requests',
        'pyyaml', 
        'pandas',
        'schedule',
        'pytz',
        'python-dateutil'
    ]
    
    for package in packages:
        print(f"Instalare {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    print("\n✅ Instalare completă! Acum poți:")
    print("1. Copiază fișierele YAML în folderul config/")
    print("2. Adaugă cheile tale API în config.yaml")
    print("3. Rulează: python src/main.py")

if __name__ == "__main__":
    install_packages()