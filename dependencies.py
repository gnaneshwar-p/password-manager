import subprocess

def install_packages():
    packages = ['cryptography', 'tk']
    for package in packages:
        try:
            subprocess.check_call(['pip', 'install', package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")

if __name__ == "__main__":
    install_packages()
