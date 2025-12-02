# 🛡️ Web Security Toolkit (LocalLLM Edition)

Bu depo (repository), ofansif siber güvenlik süreçlerini otomatize etmek ve zafiyet doğrulama (PoC) süreçlerini öğrenmek amacıyla geliştirilmiş Python araçlarını içerir.

Proje, **SQL Injection** ve **XSS (Cross-Site Scripting)** zafiyetlerini tespit etmekten, bu zafiyetlerin sömürülmesi (exploitation) ve doğrulanması (verification) aşamalarına kadar uçtan uca bir laboratuvar ortamı sunar.

Tüm araçların geliştirme sürecinde, **Local AI (Yerel Yapay Zeka)** modelleri (**WhiteRabbitNeo** ve **Dolphin**) ile pair-programming yapılmış; mantık akışı ve hata yönetimi algoritmaları bu modellerin desteğiyle optimize edilmiştir.

---

## 🧰 Modüller ve Özellikler

Bu proje birbirini tamamlayan 4 ana modülden oluşmaktadır:

### 1. 🕵️‍♂️ Vulnerability Scanner & Generator (v6.0)
SQLi ve XSS zafiyetlerini tarayan ana motordur.
* **Dual Core:** Hem SQL Injection (Time/Error Based) hem de Reflected XSS taraması yapar.
* **Stealth Mode:** WAF/Firewall tespitini önlemek için "İlk Zafiyette Durma" özelliği.
* **Payload Generator:** XSS tespit edildiğinde, manuel test için otomatik saldırı senaryoları (Cookie Stealer, Keylogger kodları) üretir.

### 2. 📡 C2 Listener (Veri Yakalayıcı)
XSS saldırıları sonucu sızdırılan verileri yakalamak için çalışan hafif bir sunucudur.
* **Data Exfiltration:** Hedef tarayıcıdan çalınan Cookie (Oturum) ve Tuş vuruşlarını (Keylogger) dinler.
* **Loglama:** Yakalanan verileri anlık olarak konsola ve dosyaya kaydeder.

### 3. 🤖 Exploit Verifier (Selenium Bot)
Tespit edilen XSS açıklarını "gerçek bir tarayıcı" üzerinde doğrulayan otomasyon aracıdır.
* **Browser Automation:** Selenium kullanarak Chrome tarayıcısını açar ve saldırıyı simüle eder.
* **PoC Doğrulama:** JavaScript'in (`alert` vb.) gerçekten çalışıp çalışmadığını kanıtlar.

### 4. ⚡ Admin Panel Finder
* **Multi-Thread:** Yönetim panellerini çoklu iş parçacığı ile hızlıca keşfeder.
* **Akıllı Analiz:** HTTP 200/302 durumlarını analiz ederek gizli giriş kapılarını bulur.

---

## 🔄 Entegre Kullanım Senaryoları (Attack Chains)

### Senaryo A: SQL Injection ile Yetki Yükseltme
1.  **Keşif:** `Admin Panel Finder` ile giriş paneli bulunur.
2.  **Sömürü:** `Scanner v6.0` (SQL Modu) ile panel taranır.
3.  **Sonuç:** Authentication Bypass zafiyeti ile şifresiz Admin girişi sağlanır.

### Senaryo B: XSS ile Oturum Çalma (Session Hijacking)
1.  **Tespit:** `Scanner v6.0` (XSS Modu) zafiyeti bulur ve "Cookie Stealer" payload'ı üretir.
2.  **Hazırlık:** `listener.py` başlatılarak dinleme moduna geçilir.
3.  **Doğrulama:** `exploit_verifier.py` (veya manuel test) ile payload hedefe gönderilir.
4.  **Sonuç:** Listener ekranına kurbanın Oturum Çerezi (Session Cookie) düşer.

---

## ⚙️ Kurulum

Araçların çalışması için Python 3 ve aşağıdaki kütüphaneler gereklidir.
*(Selenium, tarayıcı otomasyonu için eklenmiştir)*

```bash
# Gerekli tüm kütüphaneleri yükleyin
pip install requests selenium webdriver-manager
