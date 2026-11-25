import pytest

from magis.contracts.errors import DataTidakDitemukan
from magis.contracts.models import Misi
from magis.data.fake.repositories import MisiRepositoryPalsu


@pytest.fixture
def repo():
    return MisiRepositoryPalsu()

def test_daftar_mengembalikan_semua_misi(repo):
    hasil = repo.daftar()
    assert len(hasil) == 2
    assert all(isinstance(m, Misi) for m in hasil)

def test_daftar_mengembalikan_salinan(repo):
    repo.daftar().clear()
    assert len(repo.daftar()) == 2

def test_ambil_id_yang_ada(repo):
    misi = repo.ambil("M01")
    assert misi.name == "Hutan Persamaan"

def test_ambil_id_tidak_ada_melempar_galat(repo):
    with pytest.raises(DataTidakDitemukan):
        repo.ambil("M999")
