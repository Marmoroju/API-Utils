import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def consumir_api(url, headers=None, params=None):
    
    retry_strategy = Retry(
        total = 3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    try:
        r = session.get(url, headers=headers, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as e:
        print("Erro HTTP: ", e)
    except requests.exceptions.Timeout:
        print("Erro: requisição demorou demais (timeout).")
    except requests.exceptions.RequestException as e:
        print("Erro de rede: ", e)
    return None