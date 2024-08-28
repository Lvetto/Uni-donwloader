from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def user_driven_navigation():
    # Opzioni del browser
    options = Options()
    options.headless = False  # Assicurati che headless sia disattivato

    # Imposta il percorso del driver
    driver_path = input("Inserire percorso del WebDriver: ")

    if driver_path == "":
        driver_path = '/home/luca/Downloads/chrome_driver/chromedriver'

    # Avvia il browser
    driver = webdriver.Chrome(options=options, executable_path=driver_path)

    # Vai alla pagina iniziale
    driver.get('https://ariel.unimi.it/')

    # Informa l'utente di navigare manualmente fino a un certo punto
    input("Fai il login su ariel e naviga fino alla pagina che contiene i video da scaricare.\nUna volta fatto, premi invio e il programma inizierà a cliccare i vari pulsanti per far comparire i video e a scaricarli")

    # Ottieni una lista di tutte le finestre/schede aperte
    windows = driver.window_handles

    # Cambia il controllo alla nuova scheda (si assume che sia l'ultima aperta)
    driver.switch_to.window(windows[-1])

    # Trova tutti gli elementi con la classe specificata
    buttons = driver.find_elements(By.CLASS_NAME, 'cmdboxlecturecs')

    # Clicca su ogni bottone trovato
    for button in buttons:
        try:
            button.click()
            time.sleep(0.3)
        except:
            pass
    
    # Trova tutti i bottoni che contengono il testo 'Visualizza video'
    buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Visualizza video')]")

    # Clicca su ogni bottone trovato
    for button in buttons:
        try:
            button.click()
            time.sleep(0.3)
        except:
            pass
    
    time.sleep(0.5)

    # Supponiamo che 'html_content' sia la variabile che contiene il codice HTML della pagina
    html_content = driver.page_source  # Se stai usando Selenium per ottenere il contenuto della pagina

    soup = BeautifulSoup(html_content, 'html.parser')

    # Trova il tbody con id 'threadlist'
    tbody = soup.find('tbody', id='threadList')

    # Inizializza una lista per mantenere le tuple di titoli e src dei video
    threads = []

    # Itera su tutti i tag tr all'interno del tbody
    for tr in tbody.find_all('tr'):
        # Trova l'ultimo span contenuto in un h2
        h2 = tr.find('h2')
        if h2:
            span = h2.find_all('span')[-1]  # Prendi l'ultimo span
            title = span.text if span else ''

            # Trova tutti i video all'interno del tr
            videos = tr.find_all('video')
            video_sources = []
            for video in videos:
                # Trova tutti i tag source all'interno del video e ottieni l'attributo src
                sources = video.find_all('source')
                for source in sources:
                    src = source.get('src')
                    if src:
                        video_sources.append(src)

            # Associa il titolo con la lista degli src dei video
            threads.append((title, video_sources))
    
    time.sleep(1)

    # Puoi decidere se chiudere il browser automaticamente o meno
    keep_open = input("Premi Invio per chiudere il browser o digita 'no' per lasciarlo aperto: ")
    if keep_open.lower() != 'no':
        driver.quit()
    
    return threads

if __name__ == "__main__":
    user_driven_navigation()
