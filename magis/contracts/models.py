from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

TipeMisi = Literal['eksplorasi', 'boss']
TipeEvent = Literal['eksplorasi', 'boss']
StatusMisi = Literal['ongoing', 'selesai', 'gagal']
StatusRuangan = Literal['gagal', 'berhasil']
JenisSoal = Literal['event', 'skill']
StatusBattle = Literal['ongoing', 'victory', 'lose', 'fled']


# ------------- Soal ----------------
@dataclass(frozen=True)
class Tema:
    id_tema: str
    name: str
# ------------- Misi & Ruangan ----------------
@dataclass(frozen=True)
class Misi:
    id_misi: str
    name: str
    description: str
    type: TipeMisi
    id_tema: str
    id_loot: str | None = None
    id_prasyarat: str | None = None # None = misi pertama

# ------------- Item dan Loot ----------------
@dataclass(frozen=True)
class Item:
    id_item : str
    name : str
    effect_value : int
    description : str

@dataclass(frozen=True)
class Loot:
    id_loot : str
    gold_min : int
    gold_max : int
    exp : int
# ------------- Karakter ----------------
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

@dataclass(frozen=True)
class Monster:
    id_monster : str
    name : str
    hp : int = 100
    mp : int | None = None
    atk : int = 10
    level : int = 1

@dataclass(frozen=True)
class Boss:
    id_boss: str
    name : str
    hp : int = 100
    mp : int | None = None
    atk : int = 10
    level : int = 1

# ------------- Skill ----------------


# ------------- Event & Aturan ----------------
@dataclass(frozen=True)
class Aturan:
    id_aturan : str
    name : str
    value : int
    


