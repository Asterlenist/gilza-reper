import subprocess
print("""
      __________
     /          \\
    / RRRRRRR    \\
   /  RR     RR   |
   |  RR     RR   |
   |  RRRRRR      |
   |  RRR  RRRRR  |
   |  RRR  RRRRR  |EPER @ASTER2025 Russian
""")
# База репутаций и флаги с пояснениями
db = {
    "firefox": ["+-rep", "-U"],
    "brave": ["-rep", "-S"],
    "google-chrome": ["-rep", "-A", "-nOS"],
    "opera": ["-rep", "-A", "-nOS"],
    "skype": ["-rep", "-A", "-nOS"],
    "vscode": ["-rep", "-S"],
    "teamviewer": ["-rep", "-nOS"],
    "zoom": ["-rep", "-A", "-nOS"],
    "kitty": ["+rep"],
    "vlc": ["+rep"],
    "nvidia": ["-rep", "-nOS"],
    "discord": ["-rep", "-nOS"],
    "librewolf": ["++rep", "-L"],
    "librewolf-bin": ["++rep", "-L"],
    "mpv": ["++rep", "-L"],
    "spotify": ["-rep", "-nOS"],
    "slack": ["-rep", "-nOS"],
    "microsoft-edge": ["-rep", "-A", "-nOS"],
    "steam": ["+-rep", "-nOS"],
    "tor-browser": ["++rep"],
    "neovim": ["++rep", "-L"],
    "libreoffice-fresh": ["+rep", "-ST"],
    "libreoffice-stable": ["++rep", "-L"],
}

flags_info = {
    "-S": "Программа шпионила раньше",
    "-U": "Есть обновления безопасности",
    "-R": "Рекомендуются безопасные альтернативы",
    "-nOS": "Программа не Open Source / системный софт",
    "-L": "Респект от линуксоидов",
    "-ST": "Хороший софт",

}

excluded = ["nvidia", "windows", "macos"]  # Системный или закрытый софт

def get_installed_packages():
    result = subprocess.run(["pacman", "-Qq"], capture_output=True, text=True)
    return result.stdout.splitlines()

def check_packages(installed):
    for prog in installed:
        if prog in excluded:
            print(f"[{prog}] Исключено из проверки: системный или закрытый софт (-nOS)")
            continue
        if prog in db:
            reputations = db[prog]
            for r in reputations:
                if r in flags_info:
                    print(f"[{prog}] {r}: {flags_info[r]}")
                else:
                    print(f"[{prog}] {r}")

def main():
    installed = get_installed_packages()
    check_packages(installed)

if __name__ == "__main__":
    main()
