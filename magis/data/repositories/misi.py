from __future__ import annotations

import sqlite3

from magis.contracts.errors import DataTidakDitemukan
from magis.contracts.models import Misi

_KOLOM = "id_misi, name, description, type, id_tema, id_loot, id_prasyarat"

class MisiRepository:
    """Penyimpanan misi di SQLite."""

    def __init__(self, db:sqlite3.Connection):
        self._db = db
        self._db.execute("PRAGMA foreign_keys = ON")

    def daftar(self) -> list[Misi]:
        baris = self._db.execute(
            f"SELECT {_KOLOM} FROM misi ORDER BY id_misi"
        ).fetchall()
        return [Misi(*b) for b in baris]

    def ambil(self, id_misi: str) -> Misi:
        baris = self._db.execute(
            f"SELECT {_KOLOM} FROM misi WHERE id_misi = ?", (id_misi,)
        ).fetchone()
        if baris is None:
            raise DataTidakDitemukan(f"misi {id_misi} tidak ada")
        return Misi(*baris)