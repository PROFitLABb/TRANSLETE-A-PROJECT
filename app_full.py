import streamlit as st
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
import os
from datetime import datetime
from io import BytesIO
import base64
import json

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Echo-Translate Pro", 
    page_icon="🎤", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Stilleri
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.5em;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.2em;
        opacity: 0.95;
    }
    .stat-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        border: 2px solid rgba(102, 126, 234, 0.1);
    }
    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
    }
    .success-box {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border-left: 5px solid #28a745;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(40, 167, 69, 0.1);
    }
    .success-box h4 {
        margin: 0 0 0.5rem 0;
        color: #155724;
    }
    .info-box {
        background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);
        border-left: 5px solid #17a2b8;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(23, 162, 184, 0.1);
    }
    .info-box h4 {
        margin: 0 0 0.5rem 0;
        color: #0c5460;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        background-color: #f0f2f6;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Başlık
st.markdown("""
<div class="main-header">
    <h1>🎤 Echo-Translate Pro</h1>
    <p>Yapay Zeka Destekli Anlık Sesli Tercüman</p>
</div>
""", unsafe_allow_html=True)

# Yan Menü
st.sidebar.header("⚙️ Ayarlar")

# Dil Seçenekleri
dil_secenekleri = {
    "İngilizce 🇬🇧": "en",
    "Fransızca 🇫🇷": "fr",
    "Almanca 🇩🇪": "de",
    "İspanyolca 🇪🇸": "es",
    "İtalyanca 🇮🇹": "it",
    "Rusça 🇷🇺": "ru",
    "Japonca 🇯🇵": "ja",
    "Çince 🇨🇳": "zh-cn",
    "Korece 🇰🇷": "ko",
    "Arapça 🇸🇦": "ar",
    "Portekizce 🇵🇹": "pt",
    "Hollandaca 🇳🇱": "nl",
    "Yunanca 🇬🇷": "el",
    "İsveççe 🇸🇪": "sv",
    "Lehçe 🇵🇱": "pl",
    "Türkçe 🇹🇷": "tr",
    "Hintçe 🇮🇳": "hi",
    "Farsça 🇮🇷": "fa",
    "İbranice 🇮🇱": "he",
    "Tayca 🇹🇭": "th",
    "Vietnamca 🇻🇳": "vi",
    "Endonezce 🇮🇩": "id",
    "Malayca 🇲🇾": "ms",
    "Ukraynaca 🇺🇦": "uk",
    "Romence 🇷🇴": "ro",
    "Çekçe ��": "cs",
    "Macarca 🇭🇺": "hu",
    "Danca 🇩🇰": "da",
    "Norveççe ��": "no",
    "Fince 🇫�": "fi",
    "Bulgarca 🇧🇬": "bg",
    "Hırvatça ��": "hr",
    "Sırpça 🇷🇸": "sr",
    "Slovakça 🇸🇰": "sk",
    "Slovence 🇸🇮": "sl"
}

secilen_dil = st.sidebar.selectbox("🎯 Hedef Dil:", list(dil_secenekleri.keys()), index=0)
target_lang = dil_secenekleri[secilen_dil]

kaynak_dil_secenekleri = {
    "Türkçe 🇹🇷": "tr-TR",
    "İngilizce 🇬🇧": "en-US",
    "Fransızca 🇫🇷": "fr-FR",
    "Almanca 🇩🇪": "de-DE",
    "İspanyolca 🇪🇸": "es-ES",
    "İtalyanca 🇮🇹": "it-IT",
    "Rusça 🇷🇺": "ru-RU",
    "Japonca 🇯🇵": "ja-JP",
    "Çince 🇨🇳": "zh-CN",
    "Korece 🇰🇷": "ko-KR",
    "Arapça 🇸🇦": "ar-SA",
    "Portekizce 🇵🇹": "pt-PT",
    "Hollandaca 🇳🇱": "nl-NL",
    "Hintçe 🇮🇳": "hi-IN",
    "Tayca 🇹🇭": "th-TH",
    "Vietnamca 🇻🇳": "vi-VN"
}

kaynak_dil = st.sidebar.selectbox("🎙️ Kaynak Dil:", list(kaynak_dil_secenekleri.keys()), index=0)
kaynak_dil_kodu = kaynak_dil_secenekleri[kaynak_dil]

# Ses Ayarları
st.sidebar.markdown("---")
st.sidebar.subheader("🔊 Ses Ayarları")
ses_hizi = st.sidebar.slider("Konuşma Hızı:", 0.5, 2.0, 1.0, 0.1)
gurultu_azaltma = st.sidebar.checkbox("Gürültü Azaltma", value=True)
zaman_asimi = st.sidebar.slider("Dinleme Süresi (sn):", 5, 30, 10)

st.sidebar.markdown("---")
st.sidebar.info("💡 **İpucu:** Sessiz bir ortamda daha iyi sonuç alırsınız.")

# Translator
translator = Translator()

# Session State
if 'history' not in st.session_state:
    st.session_state.history = []
if 'total_translations' not in st.session_state:
    st.session_state.total_translations = 0
if 'favorite_lang' not in st.session_state:
    st.session_state.favorite_lang = {}

# İstatistikler ve Bilgi Kutuları
st.markdown("### 📊 Proje Bilgileri ve İstatistikler")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #667eea; margin: 0;">🎤</h2>
        <h3 style="margin: 10px 0;">{st.session_state.total_translations}</h3>
        <p style="margin: 0; color: #666;">Toplam Çeviri</p>
        <small style="color: #999;">Gerçekleştirilen</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #764ba2; margin: 0;">📝</h2>
        <h3 style="margin: 10px 0;">{len(st.session_state.history)}</h3>
        <p style="margin: 0; color: #666;">Geçmiş Kayıt</p>
        <small style="color: #999;">Saklanan çeviri</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    fav_lang = max(st.session_state.favorite_lang.items(), key=lambda x: x[1])[0] if st.session_state.favorite_lang else "Henüz Yok"
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #667eea; margin: 0;">🌍</h2>
        <h3 style="margin: 10px 0; font-size: 1.2em;">{fav_lang}</h3>
        <p style="margin: 0; color: #666;">Favori Dil</p>
        <small style="color: #999;">En çok kullanılan</small>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #764ba2; margin: 0;">🚀</h2>
        <h3 style="margin: 10px 0;">35</h3>
        <p style="margin: 0; color: #666;">Dil Desteği</p>
        <small style="color: #999;">Aktif diller</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

def translate_audio(kaynak_dil_kodu, zaman_asimi, gurultu_azaltma):
    """Sesli çeviri fonksiyonu"""
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            st.info("🎙️ Sizi dinliyorum... Konuşun.")
            
            if gurultu_azaltma:
                r.adjust_for_ambient_noise(source, duration=0.5)
            
            audio = r.listen(source, timeout=zaman_asimi, phrase_time_limit=15)
        
        with st.spinner("🔄 İşleniyor..."):
            # Sesi Metne Çevir
            if kaynak_dil_kodu:
                text = r.recognize_google(audio, language=kaynak_dil_kodu)
            else:
                text = r.recognize_google(audio)
            
            return process_translation(text)
            
    except sr.WaitTimeoutError:
        st.warning("⏱️ Zaman aşımı! Lütfen tekrar deneyin.")
        return False
    except sr.UnknownValueError:
        st.error("❌ Ses anlaşılamadı. Lütfen daha net konuşun.")
        return False
    except Exception as e:
        st.error(f"❌ Bir hata oluştu: {e}")
        return False

def process_translation(text, source_lang="auto"):
    """Çeviri işleme fonksiyonu"""
    try:
        # Tercüme Et
        translated = translator.translate(text, src=source_lang, dest=target_lang)
        
        # Dil isimlerini düzgün göster
        dil_isimleri = {
            "tr": "Türkçe 🇹🇷",
            "en": "İngilizce 🇬🇧",
            "fr": "Fransızca 🇫🇷",
            "de": "Almanca 🇩🇪",
            "es": "İspanyolca 🇪🇸",
            "it": "İtalyanca 🇮🇹",
            "ru": "Rusça 🇷🇺",
            "ja": "Japonca 🇯🇵",
            "zh-cn": "Çince 🇨🇳",
            "ko": "Korece 🇰🇷",
            "ar": "Arapça 🇸🇦",
            "pt": "Portekizce 🇵🇹",
            "nl": "Hollandaca 🇳🇱",
            "el": "Yunanca 🇬🇷",
            "sv": "İsveççe 🇸🇪",
            "pl": "Lehçe 🇵🇱",
            "hi": "Hintçe 🇮🇳",
            "fa": "Farsça 🇮🇷",
            "he": "İbranice 🇮🇱",
            "th": "Tayca 🇹🇭",
            "vi": "Vietnamca 🇻🇳",
            "id": "Endonezce 🇮🇩",
            "ms": "Malayca 🇲🇾",
            "uk": "Ukraynaca 🇺🇦",
            "ro": "Romence 🇷🇴",
            "cs": "Çekçe 🇨🇿",
            "hu": "Macarca 🇭🇺",
            "da": "Danca 🇩🇰",
            "no": "Norveççe 🇳🇴",
            "fi": "Fince 🇫🇮",
            "bg": "Bulgarca 🇧🇬",
            "hr": "Hırvatça 🇭🇷",
            "sr": "Sırpça 🇷🇸",
            "sk": "Slovakça 🇸🇰",
            "sl": "Slovence 🇸🇮"
        }
        
        kaynak_dil_adi = dil_isimleri.get(translated.src, translated.src.upper())
        hedef_dil_adi = secilen_dil
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="success-box">
                <h4>📝 Orijinal Metin</h4>
                <p style="font-size: 1.1em;"><i>{text}</i></p>
                <small>Algılanan Dil: {kaynak_dil_adi}</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="info-box">
                <h4>🌍 Çeviri</h4>
                <p style="font-size: 1.1em;"><i>{translated.text}</i></p>
                <small>Hedef Dil: {hedef_dil_adi}</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Metni Sese Çevir
        tts = gTTS(text=translated.text, lang=target_lang, slow=(ses_hizi < 1.0))
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        # Sesi Çal
        st.audio(audio_bytes, format="audio/mp3")
        
        # İstatistikleri Güncelle
        st.session_state.total_translations += 1
        if secilen_dil in st.session_state.favorite_lang:
            st.session_state.favorite_lang[secilen_dil] += 1
        else:
            st.session_state.favorite_lang[secilen_dil] = 1
        
        # Geçmişe Ekle
        st.session_state.history.append({
            "zaman": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "orijinal": text,
            "ceviri": translated.text,
            "kaynak_dil": translated.src,
            "hedef_dil": secilen_dil
        })
        
        return True
        
    except Exception as e:
        st.error(f"❌ Çeviri hatası: {e}")
        return False

# Ana Arayüz - Sekmeler
tab1, tab2, tab3, tab4 = st.tabs(["🎤 Sesli Çeviri", "⌨️ Metin Çevirisi", "📁 Ses Dosyası", "📊 İstatistikler"])

with tab1:
    st.markdown("### Mikrofona konuşarak anlık çeviri yapın")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎤 Çeviriye Başla", use_container_width=True, type="primary", key="voice_btn"):
            translate_audio(kaynak_dil_kodu, zaman_asimi, gurultu_azaltma)

with tab2:
    st.markdown("### Metin yazarak çeviri yapın")
    
    text_input = st.text_area(
        "Çevirmek istediğiniz metni yazın:", 
        height=200, 
        placeholder="Buraya yazın...",
        key="text_input"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝 Metni Çevir", use_container_width=True, type="primary", key="text_btn"):
            if text_input:
                process_translation(text_input)
            else:
                st.warning("⚠️ Lütfen bir metin girin.")
    
    with col2:
        if st.button("🗑️ Temizle", use_container_width=True, key="clear_btn"):
            st.rerun()

with tab3:
    st.markdown("### Ses dosyası yükleyerek çeviri yapın")
    
    uploaded_file = st.file_uploader("Ses dosyası seçin", type=['wav', 'mp3', 'ogg'], key="audio_upload")
    
    if uploaded_file:
        st.audio(uploaded_file)
        
        if st.button("🎵 Ses Dosyasını Çevir", type="primary", key="file_btn"):
            try:
                r = sr.Recognizer()
                
                # Dosyayı geçici olarak kaydet
                temp_file = f"temp_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
                with open(temp_file, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                with sr.AudioFile(temp_file) as source:
                    audio = r.record(source)
                    
                    if kaynak_dil_kodu:
                        text = r.recognize_google(audio, language=kaynak_dil_kodu)
                    else:
                        text = r.recognize_google(audio)
                    
                    process_translation(text)
                
                # Geçici dosyayı sil
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    
            except Exception as e:
                st.error(f"❌ Ses dosyası işlenemedi: {e}")

with tab4:
    st.markdown("### Çeviri İstatistikleri ve Geçmiş")
    
    if st.session_state.history:
        # Grafik için veri hazırla
        dil_dagilimi = {}
        for item in st.session_state.history:
            dil = item['hedef_dil']
            dil_dagilimi[dil] = dil_dagilimi.get(dil, 0) + 1
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Dil Dağılımı")
            for dil, sayi in sorted(dil_dagilimi.items(), key=lambda x: x[1], reverse=True):
                st.write(f"**{dil}:** {sayi} çeviri")
        
        with col2:
            st.subheader("⏰ Son Çeviriler")
            for item in reversed(st.session_state.history[-5:]):
                st.write(f"**{item['zaman']}** - {item['kaynak_dil']} → {item['hedef_dil']}")
        
        st.markdown("---")
        st.subheader("📜 Tüm Çeviri Geçmişi")
        
        for i, item in enumerate(reversed(st.session_state.history)):
            with st.expander(f"#{len(st.session_state.history)-i} - {item['zaman']} ({item['kaynak_dil']} → {item['hedef_dil']})"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Orijinal:**")
                    st.info(item['orijinal'])
                with col2:
                    st.write("**Çeviri:**")
                    st.success(item['ceviri'])
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("🗑️ Geçmişi Temizle", key="clear_history"):
                st.session_state.history = []
                st.session_state.total_translations = 0
                st.session_state.favorite_lang = {}
                st.rerun()
        
        with col2:
            # JSON olarak indir
            if st.button("💾 JSON İndir", key="download_json"):
                json_str = json.dumps(st.session_state.history, ensure_ascii=False, indent=2)
                st.download_button(
                    label="📥 İndir",
                    data=json_str,
                    file_name=f"ceviri_gecmisi_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
    else:
        st.info("📭 Henüz çeviri geçmişi yok. Yukarıdaki sekmelerden çeviri yapmaya başlayın!")

# Alt Bilgi
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white; margin-top: 2rem;'>
    <h3 style='margin: 0 0 1rem 0;'>Echo-Translate Pro v3.0</h3>
    <p style='margin: 0.5rem 0; font-size: 1.1em;'>🎤 Sesli Çeviri | ⌨️ Metin Çevirisi | 📁 Dosya Desteği | 📊 İstatistikler</p>
    <p style='margin: 0.5rem 0;'>35 Dil Desteği • Gerçek Zamanlı Çeviri • Yapay Zeka Destekli Ses Sentezi</p>
    <hr style='border: 1px solid rgba(255,255,255,0.3); margin: 1.5rem 0;'>
    <p style='margin: 0.5rem 0; font-size: 0.95em; font-style: italic;'>
        "Diller arasındaki engelleri yapay zeka ile aşmak..."
    </p>
    <p style='margin: 1rem 0 0 0; font-size: 0.9em;'>
        💻 Geliştirici: <b>Berat Koçak</b> | 2026
    </p>
    <small style='opacity: 0.8;'>Python • Streamlit • Google AI • Speech Recognition</small>
</div>
""", unsafe_allow_html=True)
