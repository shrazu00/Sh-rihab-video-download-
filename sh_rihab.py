import os
import sys

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    print("\033[1;32m" + "="*40)
    print("  ███████╗██╗  ██╗    ██████╗ ██╗██╗  ██╗ █████╗ ██████╗ ")
    print("  ██╔════╝██║  ██║    ██╔══██╗██║██║  ██║██╔══██╗██╔══██╗")
    print("  ███████╗███████║    ██████╔╝██║███████║███████║██████╔╝")
    print("  ╚════██║██╔══██║    ██╔══██╗██║██╔══██║██╔══██║██╔══██╗")
    print("  ███████║██║  ██║    ██║  ██║██║██║  ██║██║  ██║██████╔╝")
    print("  ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ")
    print("="*40)
    print("  [ DEVELOPER : SH RIHAB ]")
    print("="*40 + "\033[0m")

def download_video(url, is_tiktok=False):
    print(f"\n\033[1;33m⏳ Downloading started...\033[0m")
    if is_tiktok:
        cmd = f"yt-dlp -P /sdcard/Download/ {url}"
    else:
        cmd = f"yt-dlp -P /sdcard/Download/ -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' {url}"
    
    os.system(cmd)
    print("\n\033[1;32m✅ Download complete! Check your phone's Download folder.\033[0m")
    input("\nPress Enter to return to main menu...")

def download_audio(url):
    print(f"\n\033[1;33m⏳ Downloading audio and converting to MP3...\033[0m")
    cmd = f"yt-dlp -P /sdcard/Download/ -x --audio-format mp3 {url}"
    os.system(cmd)
    print("\n\033[1;32m✅ Audio download complete! Check your phone's Download folder.\033[0m")
    input("\nPress Enter to return to main menu...")

def main():
    while True:
        banner()
        print("\033[1;36m[1]\033[0m YouTube Video Download")
        print("\033[1;36m[2]\033[0m TikTok Video Download (No Watermark)")
        print("\033[1;36m[3]\033[0m Audio Download (MP3)")
        print("\033[1;31m[0]\033[0m Exit")
        print("="*40)
        
        choice = input("\033[1;33m👉 Select your option (0-3): \033[0m")
        
        if choice == '1':
            url = input("\n🔗 Enter YouTube Video Link: ")
            if url: download_video(url, is_tiktok=False)
        elif choice == '2':
            url = input("\n🔗 Enter TikTok Video Link: ")
            if url: download_video(url, is_tiktok=True)
        elif choice == '3':
            url = input("\n🔗 Enter Audio Link (YouTube/TikTok): ")
            if url: download_audio(url)
        elif choice == '0':
            print("\n\033[1;32mThank you for using this tool! Goodbye.\033[0m")
            sys.exit()
        else:
            print("\n\033[1;31m❌ Invalid option! Please try again.\033[0m")
            import time
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[1;31mTool has been stopped.\033[0m")
        sys.exit()
