"""Local'de test etmek için küçük başlangıç dosyası.

GitHub Actions, direkt olarak:
  from mhrs_client import check_and_book_appointment; check_and_book_appointment()
satırını çalıştıracak. Yani main.py zorunlu değil,
ama bilgisayarında test etmek istersen işine yarar.
"""
from mhrs_client import check_and_book_appointment


if __name__ == "__main__":
    check_and_book_appointment()
