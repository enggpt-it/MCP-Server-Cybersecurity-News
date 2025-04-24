from mcp.server.fastmcp import FastMCP
import httpx
from bs4 import BeautifulSoup

# Inizializza il server
mcp = FastMCP("cybersecurity_news")

USER_AGENT = "news-app/1.0"

# Dizionario dei siti di notizie supportati
NEWS_SITES = {
    "redhotcyber": "https://www.redhotcyber.com/"
}

async def fetch_news(url: str):
    """Recupera e riassume le ultime notizie dal sito specificato."""
    async with httpx.AsyncClient(headers={"User-Agent": USER_AGENT}) as client:
        try:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()  # Gestisce errori HTTP
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Trova tutti i tag <h5> e <p> dentro <div class="carousel-caption">
            captions = soup.find_all("div", class_="carousel-caption")
            news_items = []
            for caption in captions:
                title_tag = caption.find("h5")
                paragraph_tag = caption.find("p")
                
                # Estrai il testo e il link dal tag <h5>
                title = title_tag.get_text().strip() if title_tag else ""
                link = title_tag.find("a")["href"] if title_tag and title_tag.find("a") else ""
                
                # Estrai il testo dal tag <p>
                paragraph = paragraph_tag.get_text().strip() if paragraph_tag else ""
                
                # Aggiungi il risultato alla lista
                news_items.append({"title": title, "link": link, "summary": paragraph})
            
            return news_items
        except httpx.TimeoutException:
            return "Errore di timeout durante il recupero delle notizie"
        except httpx.HTTPStatusError as e:
            return f"Errore HTTP: {e.response.status_code}"
        except Exception as e:
            return f"Errore durante il recupero delle notizie: {str(e)}"

@mcp.tool()  
async def get_news(source: str):
    """
    Recupera le ultime notizie da una specifica fonte di news.

    Args:
        source: Nome della fonte di news (ad esempio, "redhotcyber").

    Returns:
        Una lista delle ultime notizie con titolo, link e descrizione.
    """
    if source not in NEWS_SITES:
        raise ValueError(f"La fonte {source} non è supportata. Fonti disponibili: {', '.join(NEWS_SITES.keys())}")

    news_text = await fetch_news(NEWS_SITES[source])
    return news_text

if __name__ == "__main__":
    mcp.run(transport="stdio")