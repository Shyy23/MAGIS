from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

TipeMisi = Literal['eksplorasi', 'boss']

@dataclass(frozen=True)
class Tema:
    id_tema: int
    name: str

@dataclass(frozen=True)
class Misi:
    id_misi: int
    name: str
    description: str
    type: TipeMisi
    id_tema: int
    id_loot: int | None = None
    id_prasyarat: int | None = None # None = misi pertama

@dataclass
class Player:
    id_player: int
    name: str
    gold: int = 0
    level: int = 1
    exp: int = 0
    hp: int = 100
    mp: int = 100
    atk: int = 10
