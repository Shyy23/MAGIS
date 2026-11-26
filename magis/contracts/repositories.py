from __future__ import annotations

from typing import Protocol

from magis.contracts.models import Misi


class MisiRepository(Protocol):
    def daftar(self) -> list[Misi]:
        "Semua misi, urut menurut id_misi."
        ...

    def ambil(self, id_misi:str) -> Misi:
        "Melempar DataTidkDitemukan jika id_misi tidak ada."
        ...
        