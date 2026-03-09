@echo off
echo ========================================
echo Echo-Translate Kurulum Scripti
echo ========================================
echo.

echo [1/3] Python versiyonu kontrol ediliyor...
python --version
if errorlevel 1 (
    echo HATA: Python yuklu degil!
    echo Lutfen Python 3.7+ yukleyin: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo.

echo [2/3] Gerekli kutuphaneler yukleniyor...
pip install -r requirements.txt
if errorlevel 1 (
    echo HATA: Kutuphaneler yuklenemedi!
    pause
    exit /b 1
)
echo.

echo [3/3] Kurulum tamamlandi!
echo.
echo ========================================
echo Uygulamayi baslatmak icin:
echo   streamlit run app.py
echo ========================================
echo.
pause
