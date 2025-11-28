# 🛡️ LocalAI SQL Injection Scanner v4.1 (Stealth Edition)

Bu proje python tabanlı gelişmiş bir SQL Injection tarama aracıdır.

Geleneksel tarayıcıların aksine, **"Stealth First" (Önce Gizlilik)** prensibiyle çalışır ve WAF (Güvenlik Duvarı) tespitini minimize etmek için akıllı durdurma mekanizmasına sahiptir.

## 🚀 Özellikler

* **🕵️‍♂️ Stealth Mode (Gizli Mod):** İlk zafiyet tespit edildiği anda taramayı durdurur. Bu sayede gereksiz gürültü yapmaz ve IP engellenme riskini düşürür.
* **⏱️ Time-Based Detection:** Sadece hata mesajlarına bakmaz, sunucunun tepki süresini (Response Time) ölçerek kör (Blind) SQL açıklarını tespit eder.
* **📡 OOB (Out-of-Band) Desteği:** DNS ve HTTP etkileşimli payloadları destekler (Listener entegrasyonu ile).
* **🤖 AI-Generated Logic:** Kod mantığı ve hata yakalama algoritmaları, ofansif siber güvenlik için eğitilmiş LLM'ler tarafından optimize edilmiştir.
* **📝 Custom Payload:** `payloads.txt` üzerinden tamamen özelleştirilebilir saldırı vektörleri.

## ⚙️ Kurulum

Bu aracı çalıştırmak için Python 3 ve `requests` kütüphanesi gereklidir.

```bash
# Gerekli kütüphaneyi yükleyin
pip install requests