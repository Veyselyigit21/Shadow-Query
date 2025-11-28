import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

# 1. Admin Paneli Kontrol Fonksiyonu
def check_admin_panel(url, header):
    try:
        # Siteye istek atıyoruz (Timeout 3 saniye yaptık ki hızlı geçsin)
        response = requests.get(url, headers=header, timeout=3)
        
        # Eğer sayfa varsa (200 OK)
        if response.status_code == 200:
            print(f"[+] BULUNDU! -> {url}")
        # Eğer yönlendirme varsa (302 Found) - Bazen admin paneline atar
        elif response.status_code == 302:
            print(f"[!] YÖNLENDİRME -> {url}")
            
    except requests.RequestException:
        # Hata verirse (site açılmazsa vs.) ekrana yazıp kirletmesin, sessizce geçsin.
        pass

# 2. Tarama Başlatıcı Fonksiyon
def start_scan(target_url, admin_paths):
    print(f"\n[*] Hedef Taranıyor: {target_url}")
    print(f"[*] İş Parçacığı (Hız): 10 Thread")
    print("-" * 40)

    # User-Agent: Kendimizi normal bir Google Chrome gibi tanıtıyoruz (Gizlilik)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Çoklu işlem (Threading) başlatıyoruz
    with ThreadPoolExecutor(max_workers=10) as executor:
        for path in admin_paths:
            # URL ile admin yolunu düzgünce birleştiriyoruz
            full_url = urljoin(target_url, path)
            executor.submit(check_admin_panel, full_url, header)

# --- ANA PROGRAM ---
if __name__ == "__main__":
    try:
        # KULLANICIDAN URL İSTEYEN KISIM
        target_input = input("Hedef URL'yi yapıştırın (Örn: http://site.com): ").strip()

        # URL kontrolü (http yazmayı unuttuysan uyarır)
        if not target_input.startswith("http"):
            print("\n[HATA] URL 'http://' veya 'https://' ile başlamalıdır!")
        else:
            # Eğer URL'nin sonunda / yoksa ekleyelim ki düzgün çalışsın
            if not target_input.endswith('/'):
                target_input += '/'

            # Dosyadan listeyi oku
            with open('admin_paths.txt', 'r') as file:
                # Boş satırları temizleyerek listeyi al
                paths = [line.strip() for line in file if line.strip()]
            
            # Taramayı başlat
            start_scan(target_input, paths)
            
    except FileNotFoundError:
        print("\n[HATA] 'admin_paths.txt' dosyası bulunamadı! Lütfen oluşturun.")
    except KeyboardInterrupt:
        print("\n[!] Tarama kullanıcı tarafından durduruldu.")

    input("\nÇıkmak için Enter'a basın...")