# 🛡️ AI-Powered Web Security Toolkit (LocalLLM Edition)
Bu proje python tabanlı gelişmiş bir SQL Injection tarama aracıdır.

Geleneksel tarayıcıların aksine, **"Stealth First" (Önce Gizlilik)** prensibiyle çalışır ve WAF (Güvenlik Duvarı) tespitini minimize etmek için akıllı durdurma mekanizmasına sahiptir.

Bu depo (repository), ofansif siber güvenlik süreçlerini otomatize etmek amacıyla geliştirilmiş Python araçlarını içerir.

Tüm araçların geliştirme sürecinde, **Local AI (Yerel Yapay Zeka)** modelleri (**WhiteRabbitNeo** ve **Dolphin**) ile pair-programming yapılmış; mantık akışı ve hata yönetimi algoritmaları bu modellerin desteğiyle optimize edilmiştir.

## 🧰 Araçlar

Bu proje şu an için iki ana modülden oluşmaktadır:

### 1. 🕵️‍♂️ Stealth SQL Injection Scanner (v4.1)
Gelişmiş bir SQL zafiyet tarayıcısıdır.
* **Özellikler:** Time-Based & Error-Based tespit, OOB (Out-of-Band) desteği.
* **Stealth Mode:** WAF/Firewall tespitini önlemek için "İlk Zafiyette Durma" (Stop-on-Found) özelliği.
* **Custom Payload:** `payloads.txt` üzerinden özelleştirilebilir saldırı vektörleri.

### 2. ⚡ Multi-Threaded Admin Panel Finder (v1.0)
Hedef sitelerin yönetim panellerini tespit etmek için kullanılan hızlı keşif aracı.
* **Özellikler:** Çoklu iş parçacığı (Multi-threading) ile yüksek hızda tarama.
* **Akıllı Tespit:** HTTP 200 (OK) ve 302 (Redirect) durum kodlarını analiz eder.
* **User-Agent Spoofing:** Taramayı gerçek bir tarayıcı gibi göstererek gizlilik sağlar.

---

## ⚙️ Kurulum

Araçların çalışması için Python 3 ve `requests` kütüphanesi gereklidir.

```bash
# Gerekli kütüphaneyi yükleyin
pip install requests
