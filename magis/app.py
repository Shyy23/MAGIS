from magis.data.fake.repositories import MisiRepositoryPalsu


def jalankan():
    print("===== MAGIS =====")
    repo = MisiRepositoryPalsu()
    for misi in repo.daftar():
        print(f"[{misi.id_misi}] {misi.name} ({misi.type})")

    ambilMisi = repo.ambil("M01")
    print(f"[{ambilMisi.id_misi}] {ambilMisi.name} ({ambilMisi.type})")