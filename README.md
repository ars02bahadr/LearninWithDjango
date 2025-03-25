# Django Kullanıcı ve Profil Yönetim Sistemi

Bu proje, Django web framework'ü kullanılarak geliştirilmiş kapsamlı bir kullanıcı ve profil yönetim sistemidir. Sistem, kullanıcı rolleri ve tipleri ile birlikte gelişmiş profil yönetimi sağlar.

## Django Nedir?

Django, Python programlama dili ile yazılmış, yüksek seviyeli bir web framework'üdür. "Batteries included" (Piller dahil) felsefesiyle, web uygulamaları geliştirmek için ihtiyaç duyulan tüm temel bileşenleri içerir.

### Django'nun Kullanım Alanları:
- Web uygulamaları geliştirme
- İçerik yönetim sistemleri (CMS)
- Sosyal medya platformları
- E-ticaret siteleri
- API geliştirme
- Bilimsel hesaplama platformları

### Django'nun Avantajları:
- Hızlı geliştirme
- Güvenlik özellikleri
- Ölçeklenebilirlik
- Geniş ekosistem
- Zengin dokümantasyon
- Aktif topluluk desteği

## MVT (Model-View-Template) Mimarisi

Django, MVC (Model-View-Controller) mimarisinin bir varyasyonu olan MVT mimarisini kullanır:

### Model (models.py):
- Veritabanı yapısını tanımlar
- Veri işleme mantığını içerir
- Veritabanı ile etkileşimi sağlar
- Örnek: Kullanıcı profili, blog yazısı, ürün bilgisi

### View (views.py):
- İş mantığını yönetir
- HTTP isteklerini işler
- Model ve Template arasında köprü görevi görür
- Kullanıcı etkileşimlerini yönetir

### Template (templates/):
- Kullanıcı arayüzünü tanımlar
- HTML şablonlarını içerir
- Dinamik içerik gösterimi sağlar
- Kullanıcı deneyimini şekillendirir

## Forms Kullanımı

Django Forms, web formlarını yönetmek için kullanılan güçlü bir araçtır:

### Forms'un Faydaları:
- Form doğrulama
- Güvenlik kontrolleri
- CSRF koruması
- Otomatik HTML oluşturma
- Veri temizleme ve dönüştürme

### Kullanım Alanları:
- Kullanıcı kaydı
- Profil güncelleme
- Veri girişi
- Dosya yükleme
- Arama formları

## Modüler Yapı

Django'nun modüler yapısı şu avantajları sağlar:

### Modülerliğin Faydaları:
- Kod tekrarını önleme
- Bakım kolaylığı
- Yeniden kullanılabilirlik
- Test edilebilirlik
- Ölçeklenebilirlik

### Modüler Bileşenler:
- Apps (Uygulamalar)
- Middleware
- Template tags
- Custom managers
- Custom model fields

## URL Yapısı (urls.py)

URL yapılandırması, web uygulamasının yönlendirme sistemini yönetir:

### URL Yapısının Özellikleri:
- Temiz URL tasarımı
- SEO dostu yapı
- URL parametreleri
- URL pattern matching
- URL namespace'leri

### Kullanım Alanları:
- Sayfa yönlendirme
- API endpoint'leri
- Dinamik URL'ler
- URL parametreleri
- URL filtreleme

## Özellikler

- 👥 Kullanıcı Yönetimi
  - Kayıt olma
  - Giriş yapma
  - Şifre değiştirme
  - E-posta güncelleme

- 👤 Profil Yönetimi
  - Profil fotoğrafı yükleme
  - Telefon numarası ekleme
  - Ad-soyad güncelleme
  - Profil bilgilerini düzenleme

- 🎭 Rol Tabanlı Yetkilendirme
  - Kullanıcı rolleri tanımlama
  - Rol atama ve düzenleme
  - Rol bazlı erişim kontrolü

- 📋 Kullanıcı Tipleri
  - Özelleştirilebilir kullanıcı tipleri
  - Tip bazlı gruplandırma
  - Tip yönetimi

- 🔍 Arama ve Filtreleme
  - Kullanıcı arama
  - Rol ve tip bazlı filtreleme
  - Gelişmiş liste görünümleri

## Teknolojiler

- **Backend:** Django 5.0.3
- **Frontend:** Bootstrap 5
- **Veritabanı:** SQLite (varsayılan)
- **Form İşleme:** django-crispy-forms
- **Resim İşleme:** Pillow
- **Güvenlik:** Django'nun yerleşik güvenlik özellikleri

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/LearninWithDjango.git
cd LearninWithDjango
```

2. Virtual environment oluşturun ve aktif edin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac için
venv\Scripts\activate     # Windows için
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Veritabanı migrasyonlarını yapın:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Projeyi çalıştırın:
```bash
python manage.py runserver
```

## Proje Yapısı

```
LearninWithDjango/
├── mysite/                  # Ana uygulama dizini
│   ├── migrations/         # Veritabanı migrasyon dosyaları
│   ├── static/            # Statik dosyalar (CSS, JS, resimler)
│   ├── templates/         # HTML şablonları
│   ├── admin.py          # Admin panel yapılandırması
│   ├── forms.py          # Form tanımlamaları
│   ├── models.py         # Veritabanı model tanımlamaları
│   ├── urls.py           # URL yapılandırmaları
│   └── views.py          # View fonksiyonları
├── media/                 # Kullanıcı yükleme dosyaları
├── manage.py             # Django yönetim scripti
├── requirements.txt      # Proje bağımlılıkları
└── README.md             # Proje dokümantasyonu
```

## Önemli Dosyalar ve İşlevleri

### models.py
- `UserType`: Kullanıcı tiplerini tanımlar (örn. Admin, Müşteri, Personel)
- `UserRole`: Kullanıcı rollerini tanımlar (örn. Editör, Moderatör)
- `Profile`: Kullanıcı profil bilgilerini ve ilişkilerini içerir

### views.py
- Kullanıcı kaydı ve girişi
- Profil oluşturma ve güncelleme
- Rol ve tip yönetimi
- Kullanıcı ayarları

### forms.py
- `RegisterForm`: Kullanıcı kayıt formu
- `ProfileForm`: Profil düzenleme formu
- `UserSettingsForm`: Kullanıcı ayarları formu
- `UserTypeForm` ve `UserRoleForm`: Tip ve rol yönetim formları

## Güvenlik Özellikleri

- Şifreleme: Django'nun yerleşik şifreleme sistemi
- CSRF koruması
- Oturum yönetimi
- Yetkilendirme kontrolleri
- Güvenli dosya yükleme

## Kullanıcı Arayüzü

- Bootstrap 5 ile modern ve responsive tasarım
- Kullanıcı dostu formlar
- Toast bildirimleri
- Dinamik form doğrulama
- Profil fotoğrafı önizleme

## Varsayılan Admin Kullanıcı Bilgileri
1. Kullanıcı Adı: admin
2. Şifre: Admin1234admin.

## Varsayılan Kullanıcı Bilgileri
1. Kullanıcı Adı:test01,test02,test03
2. Şifre:Test1234test.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## İletişim

Proje ile ilgili sorularınız için [GitHub Issues](https://github.com/kullaniciadi/LearninWithDjango/issues) sayfasını kullanabilirsiniz. 


