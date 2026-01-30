TaskMaster Pro

TaskMaster, Flask ve SQLAlchemy kullanılarak geliştirilmiş, modern arayüzlü ve kullanıcı dostu bir yapılacaklar listesi (To-Do) uygulamasıdır. Bu proje, temel CRUD (Oluşturma, Okuma, Güncelleme, Silme) işlemlerini ve modern web geliştirme pratiklerini içermektedir.

✨ Özellikler
Görev Yönetimi: Görev ekleme, silme ve tamamlama/geri alma.

Tarih Desteği: Her görev için son tarih (deadline) belirleme.

Anlık Bildirimler: İşlem sonuçlarına göre kullanıcıyı bilgilendiren "Flash Messages" sistemi.

Modern UI: Karanlık tema (Dark Mode) destekli, responsive ve şık CSS tasarımı.

OOP Mimarisi: Veritabanı modelleri Nesne Yönelimli Programlama prensipleriyle yapılandırılmıştır.

Güvenli Yapı: Veritabanı dosyaları ve geçici dosyalar .gitignore ile korunmaktadır.

🛠️ Kullanılan Teknolojiler
Backend: Python, Flask

Veritabanı: SQLite & Flask-SQLAlchemy (ORM)

Frontend: HTML5, CSS3 (Flexbox & Animations), FontAwesome İkonları

📦 Kurulum
Projeyi bilgisayarınıza klonlayın:
git clone https://github.com/kullanici_adin/proje_adin.git

Proje dizinine gidin:
cd proje_adin

Gerekli kütüphaneleri yükleyin:
pip install flask flask-sqlalchemy

Uygulamayı çalıştırın:
python app.py

Tarayıcınızda şu adresi açın: http://127.0.0.1:5000

📂 Dosya Yapısı
app.py: Uygulamanın ana mantığı ve rotaları.

db.sqlite: Veritabanı dosyası (Yerel kullanım içindir, repo'da yer almaz).

templates/: HTML şablonları.

static/: CSS dosyaları ve görseller.

.gitignore: Repo'ya dahil edilmeyecek dosyaların listesi.

📝 Lisans
Bu proje eğitim amaçlı geliştirilmiştir. İstediğiniz gibi geliştirebilir ve kullanabilirsiniz.