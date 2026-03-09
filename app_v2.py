import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os
from datetime import datetime
from io import BytesIO

# Sayfa Yapılandırması
st.set_page_config(page_title="Echo-Translate AI", page_icon="🎤", layout="wide")
st.title("🎤 Echo-Translate: Anlık Sesli Tercüman")
st.markdown("---")

# Yan Menü (Ayarlar)
st.sidebar.header("⚙️ Ayarlar")
dil_secenekleri = {
    "İngilizce 🇬🇧": "en",
    "Fransızca 🇫🇷": "fr",
    "Almanca 🇩🇪": "de",
    "İspanyolca 🇪🇸": "es",
    "İtalyanca 🇮🇹": "it",
    "Rusça 🇷🇺": "ru",
    "Japonca 🇯🇵": "ja",
    "Arapça 🇸🇦": "ar"
}
secilen_dil = st.sidebar.selectbox("Hedef Dil Seçin:", list(dil_secenekleri.keys()))
target_lang = dil_secenekleri[secilen_dil]

st.sidebar.markdown("---")
st.sidebar.info("💡 **İpucu:** Metin girişi kullanarak çeviri yapabilirsiniz.")

translator = Translator()

# Çeviri geçmişi için session state
if 'history' not in st.session_state:
    st.session_state.history = []

def translate_text(text, source_lang="auto"):
    """Metni çevir ve seslendir"""
    try:
        # Tercüme Et
        translated = translator.translate(text, src=source_lang, dest=target_lang)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("📝 **Orijinal Metin:**")
            st.write(f"*{text}*")
            if translated.src != source_lang:
                st.caption(f"Algılanan dil: {translated.src}")
        
        with col2:
            st.success(f"🌍 **Çeviri ({secilen_dil}):**")
            st.write(f"*{translated.text}*")
        
        # Metni Sese Çevir (Text to Speech)
        tts = gTTS(text=translated.text, lang=target_lang)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        # Sesi Çal
        st.audio(audio_bytes, format="audio/mp3")
        
        # Geçmişe ekle
        st.session_state.history.append({
            "zaman": datetime.now().strftime("%H:%M:%S"),
            "orijinal": text,
            "ceviri": translated.text,
            "dil": secilen_dil
        })
        
        return True
        
    except Exception as e:
        st.error(f"❌ Bir hata oluştu: {e}")
        return False

# Ana Arayüz
tab1, tab2 = st.tabs(["⌨️ Metin Çevirisi", "🎙️ Ses Dosyası Yükle"])

with tab1:
    st.markdown("### Metin yazarak çeviri yapın")
    text_input = st.text_area("Çevirmek istediğiniz metni yazın:", height=150, placeholder="Buraya yazın...")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📝 Metni Çevir", use_container_width=True, type="primary"):
            if text_input:
                translate_text(text_input)
            else:
                st.warning("⚠️ Lütfen çevirmek için bir metin girin.")

with tab2:
    st.markdown("### Ses dosyası yükleyerek çeviri yapın")
    st.info("🎤 **Not:** Mikrofon desteği için PyAudio gereklidir. Şimdilik metin girişi kullanabilirsiniz.")
    
    uploaded_file = st.file_uploader("Ses dosyası seçin (WAV, MP3)", type=['wav', 'mp3'])
    
    if uploaded_file:
        st.audio(uploaded_file)
        st.warning("⚠️ Ses dosyası tanıma özelliği için ek kütüphaneler gereklidir.")

st.markdown("---")

# Çeviri Geçmişi
if st.session_state.history:
    st.subheader("📜 Çeviri Geçmişi")
    for i, item in enumerate(reversed(st.session_state.history[-5:])):
        with st.expander(f"⏰ {item['zaman']} - {item['dil']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Orijinal:**")
                st.info(item['orijinal'])
            with col2:
                st.write("**Çeviri:**")
                st.success(item['ceviri'])
    
    if st.button("🗑️ Geçmişi Temizle"):
        st.session_state.history = []
        st.rerun()

# Alt bilgi
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>Echo-Translate v2.0 | Metin tabanlı çeviri sistemi</small>
</div>
""", unsafe_allow_html=True)
