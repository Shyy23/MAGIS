class MagisError(Exception):
    """Induk semua galat di MAGIS."""

class DataTidakDitemukan(MagisError):
    """Dipakai saat id yang dicari tidak ada."""