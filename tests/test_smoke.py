from magis.app import jalankan


def test_jalankan(capsys):
    jalankan()
    assert "MAGIS" in capsys.readouterr().out
