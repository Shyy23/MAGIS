from magis.contracts.errors import DataTidakDitemukan
from magis.contracts.models import Misi


class MisiRepositoryPalsu:
    """Penyimpanan misi tiruan: isinya list biasa di memori."""

    def __init__(self):
        self._data = [
            Misi(id_misi="M01", name="Hutan Persamaan", 
                 description="Hutan yang menyimpan misteri", 
                 type="eksplorasi", id_tema="T01"),
            Misi(id_misi="M02", name="Inti Hutan Persamaan", 
                 description="Ada suara apa ya??", 
                 type="boss", id_tema="T01", id_prasyarat="M01")
        ]

    def daftar(self):
        return list(self._data)

    def ambil(self, id_misi):
        for misi in self._data:
            if misi.id_misi == id_misi:
                return misi
        raise DataTidakDitemukan(f"misi {id_misi} tidak ada")