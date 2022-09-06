print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n")
print("\033[;36;1;4m" + "DESCARGADOR DE  VIDEOS EN HD. \n" + "\033[0;m")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n")

from pytube import YouTube

nom = input("\033[;33;1m" "¿CUAL ES SU NOMBRE?: " "\033[0;m")
print("\n")
print("\033[;31m" + "Hola " + nom + " Suscribete a mi Canal de YOUTUBE, Don LuchoTV. \n" + "\033[0;m")

url_video = input("\033[;35m" + "Ingrese la url del video AQUÍ: \n" + "\033[0;m")

print("\n")

destino = input("\033[;33m" + "Escriba /sdcard/Luego coloque un nombre, donde se le creará una carpeta para almacenar el video descargado: \n \n" + "\033[0;m")


yt = YouTube(url_video)

video = yt.streams.get_highest_resolution()

video.download(destino)
print("\n")

print("\033[;32;1m" + nom + " Su Video fu descargado con exito." + "\033[0;m" + destino)
print("\033[;35m" + "Busquelo con el 'Nombre de su carpeta que agrego'." + "\033[0;m")
