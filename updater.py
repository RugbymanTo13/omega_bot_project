from utils import process_message

def get_decision(text: str) -> str:
    processed = process_message(text)
    if "buy" in processed:
        return "Signal d'achat détecté 📈"
    elif "sell" in processed:
        return "Signal de vente détecté 📉"
    return "Aucun signal détecté."
