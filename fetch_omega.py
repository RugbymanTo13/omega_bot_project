import requests

def get_omega_signal():
    try:
        response = requests.get("https://goldenbrain-api-test.onrender.com/alert")
        if response.status_code == 200:
            return response.text
        else:
            return "⚠️ Impossible de récupérer les signaux Omega∞"
    except Exception as e:
        return f"❌ Erreur : {e}"