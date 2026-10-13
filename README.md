# Todo API & Uçtan Uca DevOps CI/CD ve İzleme Mimarisi

Bu proje, Kırklareli Üniversitesi Yazılım Mühendisliği Zorunlu Yaz Stajı (MYDOS Teknoloji) kapsamında geliştirilmiştir[cite: 3, 5]. Projenin temel amacı; Python/Flask tabanlı bir **Todo API** uygulamasının versiyon kontrol sisteminden başlayarak konteynerleştirilmesi, otomatik CI/CD süreçlerine dahil edilmesi ve canlı ortamda sürekli izlenerek alarm mekanizmalarıyla güvence altına alınmasıdır[cite: 20, 24].

---

## 🛠️ Kullanılan Teknolojiler ve Araçlar

* **İşletim Sistemi:** Ubuntu Server (Oracle VirtualBox üzerinde)[cite: 10]
* **Sürüm Kontrolü & CI:** Git, GitHub, GitHub Actions[cite: 13, 14]
* **Konteyner mimarisi:** Docker, Dockerfile, Docker Compose, Gunicorn[cite: 21, 22]
* **Sürekli Dağıtım (CD):** Jenkins (Declarative Jenkinsfile Pipeline)[cite: 24, 25]
* **Sistem & Servis İzleme (Monitoring):** Zabbix Server, Zabbix Agent[cite: 26]
* **Bildirim Sistemi:** Gmail SMTP (Generic SMTP / STARTTLS)[cite: 28]

---

## 🏗️ Proje Mimarisi ve Çalışma Akışı

Proje, yazılım geliştirme sürecinden canlı ortam izlemesine kadar uçtan uca 4 ana aşamadan oluşmaktadır[cite: 29, 30]:

### 1. Sürüm Kontrolü ve Entegrasyon (Git & GitHub Actions)
* Geliştirmeler `feature` dallarında yürütülmüş, ana kod bütünlüğü korunarak `master` dalına birleştirilmiştir (`merge conflict` yönetimi uygulanmıştır)[cite: 15, 16].
* GitHub'a yapılan her `push` işleminde GitHub Actions workflow'u otomatik olarak tetiklenerek kod kontrolü ve ortam doğrulaması gerçekleştirilir[cite: 14, 18].

### 2. Konteynerleştirme (Docker & Docker Compose)
* Todo API uygulaması, bağımlılıklarıyla birlikte `Dockerfile` kullanılarak izole bir imaj haline getirilmiştir[cite: 21].
* `docker-compose.yml` yapılandırması ile uygulama servisleri `Gunicorn` WSGI sunucusu üzerinden ayağa kaldırılmış ve 5000 portu dış dünyaya açılmıştır[cite: 21, 22].
* Docker Bridge Network mimarisi kullanılarak servisler arası güvenli iletişim sağlanmıştır[cite: 23].

### 3. Sürekli Dağıtım Otomasyonu (Jenkins Pipeline)
* Repository üzerinde tanımlanan `Jenkinsfile` bildirimsel (declarative) boru hattı sayesinde kod değişiklikleri otomatik olarak algılanır[cite: 25].
* Jenkins; kaynak kodu çeker, Docker imajını yeniden derler, eski konteyneri durdurur ve Docker Compose ile güncel servisi canlıya alır[cite: 24, 25].

### 4. İzleme ve Otomatik Alarm (Zabbix & SMTP)
* Ubuntu sunucusu üzerinde çalışan Zabbix Server ve Agent bileşenleri kurulmuştur[cite: 26].
* `net.tcp.service[,todo-api,5000]` anahtarı ile Todo API servisinin 5000 TCP portu 1 dakikalık periyotlarla taranır[cite: 26, 27].
* Serviste kesinti yaşanması durumunda (port değeri = 0), **"High"** önem seviyesinde *"Todo API is DOWN"* alarmı (trigger) devreye girer[cite: 27].
* Zabbix Trigger Action, Gmail SMTP entegrasyonu üzerinden stajyer e-posta adresine anlık uyarı bildirimi gönderir[cite: 28].

---

## 🚀 Projeyi Yerel Ortamda Çalıştırma

1. **Depoyu klonlayın:**
   ```bash
   git clone [https://github.com/sabawoonrahman942-netizen/todo-api-project.git](https://github.com/sabawoonrahman942-netizen/todo-api-project.git)
   cd todo-api-project
