# MCP Server News

Un server MCP (Model Context Protocol) per recuperare le ultime notizie da siti web di tecnologia. Questo progetto è stato creato per illustrare come implementare un server MCP che può essere utilizzato con assistenti AI basati su Claude.

## Descrizione

Questo repository contiene un'implementazione di un server MCP che consente ai modelli linguistici di accedere alle ultime notizie tecnologiche da vari siti web. Il server espone uno strumento (`get_tech_news`) che può essere utilizzato per recuperare contenuti da fonti di notizie specificate.

## Caratteristiche

- Recupero delle ultime notizie da siti web tecnologici supportati
- Integrazione semplice con Claude Desktop tramite MCP
- Architettura estendibile per aggiungere nuove fonti di notizie

## Requisiti

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) package manager (consigliato)
- Claude Desktop (per testare l'integrazione)

## Installazione

### 1. Installare uv (opzionale ma consigliato)

Per MacOS e Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Per Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clonare il repository

```bash
git clone https://github.com/username/mcp-server-news.git
cd mcp-server-news
```

### 3. Creare un ambiente virtuale e installare le dipendenze

Con uv:
```bash
# Creazione ambiente virtuale
uv venv

# Attivazione per macOS/Linux
source .venv/bin/activate

# Attivazione per Windows
.venv\Scripts\activate

# Installazione librerie
uv add "mcp[cli]" httpx bs4 python-dotenv
```

Con pip:
```bash
# Creazione ambiente virtuale
python -m venv venv

# Attivazione per macOS/Linux
source venv/bin/activate

# Attivazione per Windows
venv\Scripts\activate

# Installazione librerie
pip install "mcp[cli]" httpx bs4 python-dotenv
```

## Utilizzo

### Esecuzione del server MCP

```bash
python main.py
```

### Integrazione con Claude Desktop

1. Apri Claude Desktop
2. Vai su Impostazioni > Impostazioni Sviluppatore
3. Clicca su "Edit Config"
4. Modifica il file `claude_desktop_config.json` aggiungendo:

```json
{
    "mcpServers": {
        "mcp-server-news": {
            "command": "/percorso/al/tuo/uv",
            "args": [
                "--directory",
                "/percorso/completo/al/tuo/progetto/mcp-server-news",
                "run",
                "main.py"
            ]
        }
    }
}
```

Sostituisci `/percorso/al/tuo/uv` con il percorso al tuo eseguibile uv (puoi trovarlo con `which uv` su macOS/Linux o `where uv` su Windows) e `/percorso/completo/al/tuo/progetto/mcp-server-news` con il percorso completo della directory del progetto.

## Struttura del Progetto

```
mcp-server-news/
├── main.py         # Implementazione del server MCP
├── .env            # File per le variabili d'ambiente (opzionale)
├── README.md       # Questo file
└── requirements.txt # Dipendenze del progetto
```

## Configurazione

Per aggiungere nuove fonti di notizie, modifica il dizionario `NEWS_SITES` nel file `main.py`:

```python
NEWS_SITES = {
    "arstechnica": "https://arstechnica.com",
    "techcrunch": "https://techcrunch.com",
    # Aggiungi altre fonti qui
}
```

## Come Funziona

Il server MCP espone uno strumento (`get_tech_news`) che, quando invocato, esegue le seguenti operazioni:

1. Verifica che la fonte richiesta sia supportata
2. Recupera il contenuto HTML dalla fonte specificata
3. Estrae il testo dai primi paragrafi utilizzando Beautiful Soup
4. Restituisce il testo estratto al modello AI

## Contribuire

Contributi sono benvenuti! Senti libero di aprire issues o pull requests per migliorare questo progetto.

Alcune idee per contribuire:
- Aggiungere supporto per altre fonti di notizie
- Migliorare la qualità del contenuto estratto
- Implementare funzionalità di caching per ridurre le richieste ripetute
- Aggiungere filtri per categorie di notizie

## Licenza

[MIT](LICENSE)

## Ringraziamenti

- [Anthropic](https://www.anthropic.com/) per lo sviluppo del Model Context Protocol
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) per il parsing HTML
- [httpx](https://www.python-httpx.org/) per le richieste HTTP asincrone