
def get_decision(text):
    # Exemple basique de décision automatisée
    if "achat" in text.lower():
        return "📈 Signal détecté : Achat"
    elif "vente" in text.lower():
        return "📉 Signal détecté : Vente"
    else:
        return "ℹ️ Aucun signal clair détecté."
