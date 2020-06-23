from buku.models import daftar_buku


def run_view():
    print("=== Daftar Buku ===")
    for db in daftar_buku:
        print(db)
