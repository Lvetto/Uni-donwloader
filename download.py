import subprocess
import os

def download_and_combine_video(m3u8_url, output_filename):
    # Comando ffmpeg per scaricare e unire i video
    command = [
        'ffmpeg',
        '-i', m3u8_url,      # URL del file m3u8
        '-c', 'copy',        # Copia i flussi senza ricodificarli
        '-bsf:a', 'aac_adtstoasc',  # Bitstream filter per l'audio
        output_filename      # Nome del file di output
    ]

    # Esecuzione del comando
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Controllo degli errori
    if process.returncode != 0:
        print("Errore durante il download o la combinazione dei video:")
        print(process.stderr)
    else:
        print("Video scaricato e combinato con successo in:", output_filename)

if __name__ == "__main__":
    # Esempio di utilizzo
    m3u8_url = 'https://videolectures.unimi.it/vod/mp4:Andreazza_IFNSN_20201110.mp4/manifest.m3u8'
    output_filename = 'output_video.mp4'
    download_and_combine_video(m3u8_url, output_filename)
