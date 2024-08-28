from navigate import *
from download import *
import concurrent.futures

urls = user_driven_navigation()
urls_and_filenames = []
for name, videos in urls:
    for n, video in enumerate(videos):
        urls_and_filenames.append((video, f"out/{name}_{n}.mp4"))

print(f"Iniziato il download di {len(urls_and_filenames)} file.\nAspettare i messaggi di conferma prima di provare ad aprire i file\nI file potrebbero essere scaricati in ordine sparso")

#print(urls_and_filenames)

# Utilizzo di ThreadPoolExecutor per eseguire download in parallelo
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Lista per tenere traccia dei future
    futures = []
    
    # Sottometti i compiti al ThreadPoolExecutor
    for url, filename in urls_and_filenames:
        future = executor.submit(download_and_combine_video, url, filename)
        futures.append(future)
    
    for future in futures:
        result = future.result()  # Questo blocca finché il future non è completato
