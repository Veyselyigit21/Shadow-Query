# 🛡️ Web Security Toolkit (LocalLLM Edition)

Bu depo (repository), ofansif siber güvenlik süreçlerini otomatize etmek amacıyla geliştirilmiş Python araçlarını içerir.

Proje, geleneksel kaba kuvvet (brute-force) tarayıcılarının aksine **"Stealth First" (Önce Gizlilik)** prensibiyle çalışır. WAF (Web Application Firewall) tespitini minimize etmek için akıllı durdurma mekanizmalarına ve insan davranışını taklit eden özelliklere sahiptir.

Tüm araçların geliştirme sürecinde, **Local AI (Yerel Yapay Zeka)** modelleri (**WhiteRabbitNeo** ve **Dolphin**) ile pair-programming yapılmış; mantık akışı ve hata yönetimi algoritmaları bu modellerin desteğiyle optimize edilmiştir.

---

## 🧰 Modüller ve Özellikler

Bu proje şu an için birbirini tamamlayan iki ana modülden oluşmaktadır:

### 1. 🕵️‍♂️ Stealth SQL Injection Scanner (v4.1)
Gelişmiş, gizlilik odaklı bir SQL zafiyet tarayıcısıdır.
* **Stealth Mode:** WAF engellemesini önlemek için "İlk Zafiyette Durma" (Stop-on-Found) özelliği.
* **Gelişmiş Tespit:** Sadece hata mesajlarını (Error-Based) değil, sunucu tepki sürelerini (Time-Based) ölçerek kör noktaları yakalar.
* **OOB Desteği:** Out-of-Band saldırı vektörlerini (DNS/HTTP Interaction) destekler.
* **Safe Payload:** Veritabanına zarar vermeyen, sadece okuma/tespit odaklı payload yapısı.

### 2. ⚡ Multi-Threaded Admin Panel Finder (v1.0)
Hedef sitelerin yönetim panellerini tespit etmek için kullanılan hızlı keşif aracı.
* **Yüksek Hız:** `ThreadPoolExecutor` ile çoklu iş parçacığı (Multi-threading) mimarisi.
* **Akıllı Analiz:** HTTP 200 (OK) ve 302 (Redirect) durum kodlarını analiz ederek "False Positive" sonuçları eler.
* **User-Agent Spoofing:** Taramayı gerçek bir tarayıcı gibi göstererek gizlilik sağlar.

---

## 🔄 Entegre Kullanım Senaryosu (Attack Chain)

Bu toolkit, bir sızma testi (Pentest) senaryosunda **Keşif (Reconnaissance)** ve **Sömürü (Exploitation)** aşamalarını birleştirmek için tasarlanmıştır.

**Hedef:** Sistemde yetkisiz erişim (Unauthorized Access) elde etmek veya Authentication Bypass zafiyetini doğrulamak.

1.  **Adım (Keşif):** `Admin Panel Finder` aracı ile hedef sitenin yönetim paneli giriş noktası (Örn: `/admin/login.php`) tespit edilir.
2.  **Adım (Analiz):** Bulunan giriş panelindeki input alanları (örn: `name="uname"`, `name="pass"`) analiz edilir ve scanner'a tanımlanır.
3.  **Adım (Sömürü):** `SQL Injection Scanner` tespit edilen panele yönlendirilir.
    * Araç, giriş formunda **Authentication Bypass** (Kimlik Doğrulama Atlatma) zafiyeti arar.
    * Başarılı olursa, parola bilinmese dahi sisteme **Admin yetkileriyle** giriş yapılması simüle edilir.

> **Eğitim Notu:** Bu senaryo, "SQL Injection ile Authentication Bypass" zafiyetinin (CWE-287) ne kadar kritik olduğunu ve `Prepared Statements` kullanılmamasının risklerini göstermektedir.

---

## ⚙️ Kurulum

Araçların çalışması için Python 3 ve `requests` kütüphanesi gereklidir.

```bash
# Gerekli kütüphaneyi yükleyin
pip install requests

