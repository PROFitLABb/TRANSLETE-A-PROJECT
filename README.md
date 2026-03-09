# 🎤 Echo-Translate Pro: Yapay Zeka Destekli Anlık Sesli Tercüman

Profesyonel seviye, tam özellikli sesli tercüman uygulaması. Mikrofon, metin ve ses dosyası desteği ile 15 farklı dile çeviri yapın!

## 🚀 Özellikler

### 🎤 Sesli Çeviri
- **Gerçek Zamanlı Mikrofon Desteği**: PyAudio ile doğrudan mikrofon erişimi
- **Otomatik Dil Algılama**: Konuştuğunuz dili otomatik tanır
- **Gürültü Azaltma**: Arka plan seslerini filtreler
- **Ayarlanabilir Dinleme Süresi**: 5-30 saniye arası özelleştirilebilir

### ⌨️ Metin Çevirisi
- **Hızlı Metin Girişi**: Klavye ile anında çeviri
- **Çoklu Dil Desteği**: 15 farklı dil
- **Otomatik Kaynak Dil Algılama**: Hangi dilden yazdığınızı otomatik anlar

### 📁 Ses Dosyası Desteği
- **Dosya Yükleme**: WAV, MP3, OGG formatlarını destekler
- **Toplu İşlem**: Birden fazla ses dosyasını çevirebilir

### 📊 İstatistikler ve Geçmiş
- **Detaylı İstatistikler**: Toplam çeviri sayısı, en çok kullanılan dil
- **Çeviri Geçmişi**: Tüm çevirilerinizi kayıt altına alır
- **JSON Export**: Geçmişinizi JSON formatında indirebilirsiniz
- **Dil Dağılımı**: Hangi dilleri ne kadar kullandığınızı görün

### 🎨 Kullanıcı Arayüzü
- **Modern Tasarım**: Gradient renkler ve profesyonel görünüm
- **4 Sekmeli Arayüz**: Sesli, Metin, Dosya, İstatistikler
- **Responsive Layout**: Geniş ekran desteği
- **Gerçek Zamanlı İstatistikler**: Üst panelde canlı veriler

### 🔊 Ses Ayarları
- **Konuşma Hızı Kontrolü**: 0.5x - 2.0x arası ayarlanabilir
- **Gürültü Azaltma**: Açılıp kapatılabilir
- **Yüksek Kalite TTS**: Google Text-to-Speech motoru

## 🌍 Desteklenen Diller (15 Dil)

- İngilizce 🇬🇧
- Fransızca 🇫🇷
- Almanca 🇩🇪
- İspanyolca 🇪🇸
- İtalyanca 🇮🇹
- Rusça 🇷🇺
- Japonca 🇯🇵
- Çince 🇨🇳
- Korece 🇰🇷
- Arapça 🇸🇦
- Portekizce 🇵🇹
- Hollandaca 🇳🇱
- Yunanca 🇬🇷
- İsveççe 🇸🇪
- Lehçe 🇵🇱

## 📋 Gereksinimler

```bash
pip install -r requirements.txt
```

Gerekli kütüphaneler:
- streamlit
- SpeechRecognition
- PyAudio
- googletrans==4.0.0-rc1
- gTTS
- Pillow

## 🎯 Kurulum ve Kullanım

### Hızlı Başlangıç (Windows)

1. Kurulum:
```bash
setup.bat
```

2. Çalıştırma:
```bash
run_full.bat
```

### Manuel Kurulum

1. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

2. Uygulamayı başlatın:
```bash
streamlit run app_full.py
```

3. Tarayıcınızda açın:
```
http://localhost:8501
```

## 💡 Kullanım Kılavuzu

### Sesli Çeviri:
1. "🎤 Sesli Çeviri" sekmesine gidin
2. Yan menüden hedef dili seçin
3. "Çeviriye Başla" butonuna tıklayın
4. Mikrofona konuşun
5. Çeviri otomatik olarak görüntülenecek ve seslendirilecektir

### Metin Çevirisi:
1. "⌨️ Metin Çevirisi" sekmesine gidin
2. Metin kutusuna yazın
3. "Metni Çevir" butonuna tıklayın

### Ses Dosyası:
1. "📁 Ses Dosyası" sekmesine gidin
2. WAV, MP3 veya OGG dosyası yükleyin
3. "Ses Dosyasını Çevir" butonuna tıklayın

### İstatistikler:
1. "📊 İstatistikler" sekmesine gidin
2. Çeviri geçmişinizi ve istatistiklerinizi görün
3. JSON formatında dışa aktarabilirsiniz

## 🛠️ Teknolojiler

- **Streamlit**: Modern web arayüzü
- **SpeechRecognition**: Google Speech API ile ses tanıma
- **PyAudio**: Mikrofon erişimi
- **Google Translate API**: Derin öğrenme tabanlı çeviri
- **gTTS**: Google Text-to-Speech motoru
- **Pillow**: Görsel işleme desteği

## 📝 Özellik Listesi

✅ Mikrofon ile sesli çeviri
✅ Metin girişi ile çeviri
✅ Ses dosyası yükleme ve çeviri
✅ 15 farklı dil desteği
✅ Otomatik dil algılama
✅ Gürültü azaltma
✅ Konuşma hızı kontrolü
✅ Çeviri geçmişi
✅ Detaylı istatistikler
✅ JSON export
✅ Modern ve responsive tasarım
✅ Gerçek zamanlı ses sentezi
✅ Dil dağılımı grafikleri

## 🔧 Sorun Giderme

**PyAudio kurulum hatası (Windows):**
```bash
pip install pipwin
pipwin install pyaudio
```

**Mikrofon çalışmıyor:**
- Tarayıcı izinlerini kontrol edin
- Sistem ses ayarlarından mikrofon erişimini doğrulayın
- Windows Gizlilik Ayarları > Mikrofon'dan izin verin

**Çeviri hatası:**
- İnternet bağlantınızı kontrol edin
- Google Translate API'sine erişim olduğundan emin olun

**Ses çıkmıyor:**
- Tarayıcı ses ayarlarını kontrol edin
- Sistem ses seviyesini artırın

## 📊 Performans

- Ortalama çeviri süresi: 2-3 saniye
- Ses tanıma doğruluğu: %90+
- Desteklenen ses formatları: WAV, MP3, OGG
- Maksimum ses süresi: 15 saniye (ayarlanabilir)

## 🎨 Ekran Görüntüleri

Uygulama şunları içerir:
- 4 sekmeli modern arayüz
- Gradient renkli başlık
- Gerçek zamanlı istatistik kartları
- Renkli çeviri kutuları
- Detaylı geçmiş görünümü

## 📄 Lisans

Bu proje eğitim amaçlıdır.

## 🤝 Katkıda Bulunma

Önerileriniz ve katkılarınız için issue açabilirsiniz.

---

**Echo-Translate Pro v3.0** | Yapay Zeka Destekli Çeviri Sistemi
🎤 Sesli Çeviri | ⌨️ Metin Çevirisi | 📁 Dosya Desteği | 📊 İstatistikler
