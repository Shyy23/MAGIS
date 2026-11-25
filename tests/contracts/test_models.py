from magis.contracts.models import Misi, Player, Tema


def test_membuat_tema():
    t = Tema(id_tema="T01", name="Linear Satu Variabel")
    assert t.name == "Linear Satu Variabel"
    assert t.id_tema == "T01"

def test_membuat_player_default():
    p = Player(id_player = "P1", name="Daffa")
    assert (p.gold, p.level, p.hp) == (0, 1, 100)

def test_membuat_misi():
    m = Misi(id_misi="M01", name="Hutan Persamaan", description="Jelajahi hutan", type="eksplorasi"
            , id_tema="T01")
    assert m.name == "Hutan Persamaan"
    assert m.id_prasyarat is None

# Negative Test
# def test_mengubah_misi():
#      m = Misi(id_misi="M01", name="Gua", description="Jelajahi hutan", type="eksplorasi"
#                 , id_tema="T01")
#      m.name = "Gua Kuadrat"