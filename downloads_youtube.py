print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n")
print("\033[;36;1;4m" + "DESCARGADOR DE  VIDEOS EN HD. \n" + "\033[0;m")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n")

from pytube import YouTube

nom = input("\033[;33;1m" "¿CUAL ES SU NOMBRE?: " "\033[0;m")
print("\n")
print("\033[;31m" + "Hola " + nom + " Suscribete a mi Canal de YOUTUBE, Don LuchoTV. \n" + "\033[0;m")

url_video = input("\033[;35m" + "Ingrese la url del video AQUÍ: \n" + "\033[0;m")

print("\n")

destino = input("\033[;33m" + "Escriba /sdcard/coloque un nombre donde se almacenara el video: \n \n" + "\033[0;m")


yt = YouTube(url_video)

video = yt.streams.get_highest_resolution()

video.download(destino)
print("\n")

print("\033[;32;1m" + nom + " Su Video se a descargado con exito, gracias: " + "\033[0;m" + destino)