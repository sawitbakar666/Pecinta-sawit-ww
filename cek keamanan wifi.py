import re
import subprocess
import platform

# ===============================
# CEK KEKUATAN PASSWORD WIFI
# ===============================
def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+=-]", password):
        score += 1

    if score <= 2:
        return "❌ Lemah"
    elif score == 3:
        return "⚠️ Sedang"
    else:
        return "✅ Kuat"


# ===============================
# CEK PERANGKAT DI JARINGAN (ARP)
# ===============================
def scan_devices():
    os_name = platform.system()

    print("\n📡 Memindai perangkat di jaringan...\n")

    try:
        if os_name == "Windows":
            output = subprocess.check_output("arp -a", shell=True).decode()
        else:
            output = subprocess.check_output(["arp", "-a"]).decode()

        print(output)
    except Exception as e:
        print("Gagal memindai perangkat:", e)


# ===============================
# REKOMENDASI KEAMANAN WIFI
# ===============================
def wifi_security_tips():
    print("\n🔐 Rekomendasi Keamanan Wi-Fi:")
    print("- Gunakan enkripsi WPA3 atau WPA2")
    print("- Nonaktifkan WPS")
    print("- Ganti password minimal 12 karakter")
    print("- Update firmware router")
    print("- Gunakan MAC filtering (opsional)")
    print("- Periksa perangkat asing secara berkala")


# ===============================
# PROGRAM UTAMA
# ===============================
def main():
    print("=" * 40)
    print("   WIFI SECURITY CHECKER (LEGAL)")
    print("=" * 40)

    password = input("\nMasukkan password Wi-Fi untuk dicek: ")
    result = check_password_strength(password)
    print("Kekuatan Password:", result)

    scan_devices()
    wifi_security_tips()


if __name__ == "__main__":
    main()
