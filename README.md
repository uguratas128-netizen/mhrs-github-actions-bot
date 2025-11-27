# MHRS Otomatik Randevu Botu (GitHub Actions ile)

Bu repo, bilgisayarın kapalı olsa bile GitHub Actions üzerinden
belirli aralıklarla MHRS randevu kontrolü yapmayı amaçlayan bir iskelet projedir.

## Nasıl Çalışır?

- `mhrs_client.py` içinde:
  - MHRS'e giriş
  - Randevu arama
  - Randevu alma
  iş mantığını kendin doldurursun.
- `.github/workflows/mhrs.yml` dosyası sayesinde:
  - GitHub Actions her 5 dakikada bir çalışır
  - Ortam değişkenlerini (secrets) okur
  - `check_and_book_appointment()` fonksiyonunu çalıştırır.

## Gerekli Secrets (Settings → Secrets and variables → Actions)

Şu değişkenleri eklemelisin:

- `MHRS_TC_KIMLIK`
- `MHRS_PASSWORD`
- `MHRS_PHONE` (opsiyonel)
- `MHRS_HASTANE_ID`
- `MHRS_KLINIK_ID`
- `MHRS_DOKTOR_ID` (opsiyonel)
- `MHRS_DATE_FROM` (örn: 2025-02-01)
- `MHRS_DATE_TO`   (örn: 2025-02-28)

## Local Çalıştırma

```bash
pip install -r requirements.txt
python main.py
```

## Önemli Not

Bu proje sadece iskelet yapıdır. MHRS'e istek atma, login olma ve randevu alma
kodlarını kendin yazmalısın. Bu işlemler sırasında MHRS'in kullanım koşullarına
ve yasal mevzuata uyman gerekir.
