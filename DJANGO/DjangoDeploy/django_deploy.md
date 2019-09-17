# Django Deployment to Ubuntu 18.04

### sshd service Yeniliyoruz

```
# sudo systemctl reload sshd
```

# Basit Güvenlik Duvarı Kurulumu

Güvenlik duvarında hangi kayıtlı uygulamalar var

```
# sudo ufw app list
```

OpenSSH İzin verin

```
### sudo ufw allow OpenSSH
```

### Güvenlik duvarını etkinleştirelim

```
# sudo ufw enable
```

### Durumu Kontrol Edelim

```
# sudo ufw status
```

Artık yazılımı kurmaya başlayabiliriz

# Yazılım

## Paketleri Güncelleyelim

```
# sudo apt update
# sudo apt upgrade
```

## Python3 Postgre ve nginx Yükleyelim

```
# sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

# Postgres Veritabanı & Kullanıcı Kurulumu

```
# sudo -u postgres psql
```

Artık pg kabuğuna giriş yapmalıyız

### Veritabanı Oluşturalım

```
CREATE DATABASE btre_prod;
```

### Kullanıcı oluşturalım

```
CREATE USER dbadmin WITH PASSWORD 'abc123!';
```

### Varsayılan kodlamayı ve yalıtım şemasını ayarlayalım(Django tarafından önerilir)

```
ALTER ROLE dbadmin SET client_encoding TO 'utf8';
ALTER ROLE dbadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE dbadmin SET timezone TO 'UTC';
```

### Kullanıcıya veritabanı izni verelim

```
GRANT ALL PRIVILEGES ON DATABASE btre_prod TO dbadmin;
```

### Postgres'den çıkalım

```
\q
```

# Sanal Ortam

Python3-venv paketini kurmamız gerekiyor

```
# sudo apt install python3-venv
```

### Proje dizini oluşturalım

```
# mkdir proje_dizini
# cd proje_dizini
```

### Sanal Ortam Oluşturalım

```
# python3 -m venv ./venv
```

### Ortamı Aktifleştirelim

```
# source venv/bin/activate
```

# Git & Upload

### Pip bağımlılıkları

Local makinamızda requirements.txt dosyası oluşturalım. Pip bağımlılıkları için gerekli

```
$ pip freeze > requirements.txt
```

Repomuza local projeyi pushluyoruz

### Git reposunu sunucudaki proje_dizini'ne klonlayalım

```
# git clone https://github.com/yourgithubname/btre_project.git
```

## Pip bağımlılıklarını yükleyelim

Tek tek elle yüklemek çok zor olur :) 

```
# pip install -r requirements.txt
```

# Local Ayarlar İçin

Bu kodu sunucudaki projemizin settings.py içine yazın. Sunucuya özel ayarlar için

```
try:
    from .local_settings import *
except ImportError:
    pass
```

 **local_settings.py** adında bir dosyayı settings.py dosyanızın yanına oluşturun. Asıl projeniz içerisinden bunları alacaksınız.

- SECRET_KEY
- ALLOWED_HOSTS
- DATABASES
- DEBUG
- EMAIL\_\*

## Migration'ları yapın
```
# python manage.py makemigrations
# python manage.py migrate
```

## Uygulamamız için Admin oluşturalım

```
# python manage.py createsuperuser
```

## Static dosyalarını toplayalım
```
python manage.py collectstatic
```

### Hatalar için 8000 portunu aktif edelim

```
# sudo ufw allow 8000
```

## Server'i çalıştıralım

```
# python manage.py runserver 0.0.0.0:8000
```

### Sitenizi test edin SUNUCU_IP_ADRESINIZ:8000


# Gunicorn yükleyelim

Gunicorn yükleyelim

```
# pip install gunicorn
```

requirements.txt dosyasına ekleyelim

```
# pip freeze > requirements.txt
```

### Gunicorn'u test edelim
Burada sunucu ip adresinizi girip :8000 portuna gitmelisiniz
settings.py / local_settings.py içerisinde allowed host kısmına sunucu ip adresinizi girmelisiniz
```
# gunicorn --bind 0.0.0.0:8000 proje_adiniz.wsgi
```

Resimleriniz vs. gitmiş olacak.

### Server'i durduralım ve sanal ortamı deaktif edelim

```
ctrl-c
# deactivate
```

### gunicorn.socket Dosyasını Açalım

```
# sudo nano /etc/systemd/system/gunicorn.socket
```

### Bu kodu kopyalayın ve kaydedip çıkın

```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

### gunicorn.service Dosyasını açalım

```
# sudo nano /etc/systemd/system/gunicorn.service
```

### Bu kodu yapıştırın ve kaydedip çıkın

```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=linux_oturumundaki_adınız
Group=www-data
WorkingDirectory=/home/linux_oturumundaki_adınız/proje_dizininiz/proje_adiniz
ExecStart=/home/linux_oturumundaki_adınız/proje_dizininiz/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          proje_adiniz.wsgi:application

[Install]
WantedBy=multi-user.target
```

### Gunicorn Socket'i açalım ve aktig edelim

```
# sudo systemctl start gunicorn.socket
# sudo systemctl enable gunicorn.socket
```

### Gunicorn'u test edelim

```
# sudo systemctl status gunicorn.socket
```

### Gunicorn Socketinin varlığını kontrol edelim

```
# file /run/gunicorn.sock
```

# NGINX Kurulumu

### Proje Dizini Kuralım

```
# sudo nano /etc/nginx/sites-available/proje_adiniz
```

### Bu kodu kopyalayın ve kaydedip çıkın

```
server {
    listen 80;
    server_name SUNUCU_IP_ADRESINIZ;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/linux_oturumundaki_adınız/proje_dizininiz/proje_adiniz;
    }
    
    location /media/ {
        root /home/linux_oturumundaki_adınız/proje_dizininiz/proje_adiniz;    
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

### Etkin sitelerin olduğu dizine gidin ve yeni yapılandırmanızı etkinleştirin

```
# sudo ln -s /etc/nginx/sites-available/proje_adiniz /etc/nginx/sites-enabled
```

### NGINX config'i Test Edelim

```
# sudo nginx -t
```

### NGINX Yeniden Başlatalım

```
# sudo systemctl restart nginx
```

### 8000 portunu güvenlik duvarından kaldırın ve normal trafiğe izin vermek için güvenlik duvarını açın

```
# sudo ufw delete allow 8000
# sudo ufw allow 'Nginx Full'
```

### Resimler vs. Medya dosyaları yüklemek için maximum yükleme boyutuna ihtiyacınız olacak

Nginx conf dosyasını açın

```
# sudo nano /etc/nginx/nginx.conf
```

### Bunu http {} alanına ekleyin


```
client_max_body_size 20M;
```

### NGINX Yenileyelim

```
# sudo systemctl restart nginx
```

### Medya Dosyası Sorunu

media klasörünü silip komple baştan başlatmanızı öneririm(proje_dizini)
```
# sudo rm -rf media/photos
```

# Domain Kurulumu

Domaininizi kayıt edin

```
@  kayıt  SUNUCU_IP_ADRESINIZ
www  CNAME  example.com
```

### Sunucudaki local_settings.py dosyanıza gidin ve allowed hosts kısmına domainizi ve ip adresinizi ekleyin

```
ALLOWED_HOSTS = ['SUNUCU_IP_ADRESINIZ', 'örnek.com', 'www.örnek.com']
```

### Düzenleyelim /etc/nginx/sites-available/proje_adiniz

```
server {
    listen: 80;
    server_name xxx.xxx.xxx.xxx örnek.com www.örnek.com;
}
```

### NGINX & Gunicorn Yenileyelim

```
# sudo systemctl restart nginx
# sudo systemctl restart gunicorn
```
