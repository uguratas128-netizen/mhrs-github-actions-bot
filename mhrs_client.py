import os
import logging
import requests


def login_to_mhrs(tc_kimlik: str, password: str, phone: str | None = None):
    """MHRS'e giriş yapan fonksiyonun iskeleti.

    Buraya kendi gerçek MHRS login kodunu koymalısın.
    Şu an sadece örnek bir session döndürüyor.
    """
    session = requests.Session()
    logging.info("MHRS'e giriş yapılıyormuş gibi yapıyoruz (buraya gerçek login kodu gelecek).")
    # Buraya:
    #  - MHRS login endpoint'ine POST isteği
    #  - Gerekirse SMS doğrulama
    #  - Hata kontrolleri
    # eklemen gerekiyor.
    return session


def find_and_book_appointment(session, hospital_id: str, clinic_id: str, doctor_id: str | None,
                              date_from: str, date_to: str):
    """Randevu arayıp bulursa almaya çalışan fonksiyonun iskeleti.

    Buraya MHRS randevu arama ve randevu alma isteklerini eklemelisin.
    """
    logging.info(
        "Randevu aranıyor: hastane=%s, klinik=%s, doktor=%s, tarih aralığı=%s - %s",
        hospital_id, clinic_id, doctor_id, date_from, date_to
    )

    # Örnek pseudo kod:
    # search_url = "https://mhrs.gov.tr/....."
    # params = {...}
    # resp = session.get(search_url, params=params)
    # resp.raise_for_status()
    # uygun_slot = ...
    # book_url = "https://mhrs.gov.tr/....."
    # book_payload = {...}
    # book_resp = session.post(book_url, data=book_payload)
    # book_resp.raise_for_status()
    # logging.info("Randevu başarıyla alındı!")

    logging.info("Şu an demo moddasın, gerçek randevu isteği gönderilmiyor.")


def check_and_book_appointment():
    """GitHub Actions tarafından her çalıştırıldığında çağrılan ana fonksiyon."""
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
    )

    tc_kimlik = os.environ.get("MHRS_TC_KIMLIK")
    password = os.environ.get("MHRS_PASSWORD")
    phone = os.environ.get("MHRS_PHONE")

    hospital_id = os.environ.get("MHRS_HASTANE_ID")
    clinic_id = os.environ.get("MHRS_KLINIK_ID")
    doctor_id = os.environ.get("MHRS_DOKTOR_ID")
    date_from = os.environ.get("MHRS_DATE_FROM")
    date_to = os.environ.get("MHRS_DATE_TO")

    missing = [name for name, value in [
        ("MHRS_TC_KIMLIK", tc_kimlik),
        ("MHRS_PASSWORD", password),
        ("MHRS_HASTANE_ID", hospital_id),
        ("MHRS_KLINIK_ID", clinic_id),
        ("MHRS_DATE_FROM", date_from),
        ("MHRS_DATE_TO", date_to),
    ] if not value]

    if missing:
        logging.error("Eksik ortam değişkenleri: %s", ", ".join(missing))
        return

    logging.info("MHRS işlemine başlıyoruz...")
    session = login_to_mhrs(tc_kimlik, password, phone)

    find_and_book_appointment(
        session=session,
        hospital_id=hospital_id,
        clinic_id=clinic_id,
        doctor_id=doctor_id,
        date_from=date_from,
        date_to=date_to,
    )

    logging.info("İşlem tamamlandı.")
