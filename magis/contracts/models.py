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

@dataclass
class Item:
    id_item : str
    name : str
    effect_value : int
    description : str

@dataclass
class Monster:
    id_monster : str
    name : str
    hp : int = 100
    mp : int | None = None
    atk : int = 10
    level : int = 1

@dataclass
class Boss:
    id_boss: str
    name : str
    hp : int = 100
    mp : int | None = None
    atk : int = 10
    level : int = 1

@dataclass
class Loot:
    id_loot : str
    gold_min : int
    gold_max : int
    exp_dasar : int
@dataclass
class Aturan:
    id_aturan : str
    name : str
    value : int
    


