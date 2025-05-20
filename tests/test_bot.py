from updater import get_decision

def test_get_decision():
    assert "achat" in get_decision("We should BUY now")
    assert "vente" in get_decision("SELL it all")
    assert "Aucun" in get_decision("Hold position")
