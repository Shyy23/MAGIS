from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

TipeMisi = Literal['eksplorasi', 'boss']
TipeEvent = Literal['eksplorasi', 'boss']
StatusMisi = Literal['ongoing', 'selesai', 'gagal']
StatusRuangan = Literal['gagal', 'berhasil']
JenisSoal = Literal['event', 'skill']
StatusBattle = Literal['ongoing', 'victory', 'lose', 'fled']

@dataclass(frozen=True)
class Tema:
    id_tema: str
    name: str

@dataclass(frozen=True)
class Misi:
    id_misi: str
    name: str
    description: str
    type: TipeMisi
    id_tema: str
    id_loot: str | None = None
    id_prasyarat: str | None = None # None = misi pertama

@dataclass
class Player:
    id_player: str
    name: str
    gold: int = 0
    level: int = 1
    exp: int = 0
    hp: int = 100
    mp: int = 100
    atk: int = 10


