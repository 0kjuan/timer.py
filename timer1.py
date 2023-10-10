#importar el modulo time
import time
#input time en segundos
seconds=input("Escribe el tiempo en numeros de segundos ")

def count_timer (seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)

        timer=f'{mins}:{secs}'
        print(timer,end='\r')
        time.sleep(1)

        seconds-=1
    print('Se acabó el tiempo!')

#Llamar a la funcion
count_timer(int(seconds))