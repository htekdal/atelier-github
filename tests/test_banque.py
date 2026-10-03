import pytest

from tresorerie.banque import charger_cle, entetes_requete


def test_cle_absente(monkeypatch):
    monkeypatch.delenv("BANQUE_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        charger_cle()


def test_entetes(monkeypatch):
    monkeypatch.setenv("BANQUE_API_KEY", "cle-de-test")
    assert entetes_requete()["Authorization"] == "Bearer cle-de-test"
