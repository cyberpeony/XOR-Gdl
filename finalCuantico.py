import math
class Lugar :
    def __init__(self, nombre, x, y, z):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"Nombre: {self.nombre}, Posicion: ({self.x}, {self.y},{self.z})"
    
base = Lugar("Main", 1800, 1800, 1800)
    
estacionUno = Lugar("Estacion 1", 75,12,45)
estacionDos =  Lugar("Estacion 2", 100,150,200)
estacionTres =  Lugar("Estacion 3", 200,250,300)

lugarUno = Lugar("Colinas del Rey", 10, 30, 10)
lugarDos = Lugar("Jardienes del Valle", 40, 50,5)
lugarTres = Lugar("COlinas de San Javier", 15, 15, 15)
lugarCuatro = Lugar("Lomas del valle", 15, 25, 20)
lugarCinco = Lugar("Villa Magna", 25, 10, 10)
lugarSeis = Lugar("Jardin Real", 80, 80, 3)
lugarSiete = Lugar("Chapalita", 24, 27, 60)
lugarOcho = Lugar("Zoologico", 12, 13, 18)
lugarNueve = Lugar("Tlaquepaque", 15, 90, 20)
lugarDiez = Lugar("Rancho Contento", 25, 6, 18)

lugares = [lugarUno, lugarDos, lugarTres, lugarCuatro, lugarCinco, lugarSeis, lugarSiete, lugarOcho, lugarNueve, lugarDiez]

mainAuno = 0
mainAdos = 0
mainAtres = 0

def dist(uno: Lugar,dos: Lugar):
    dist = math.sqrt(pow(abs(dos.x - uno.x),2) + pow(abs(dos.y - uno.y), 2) + pow(abs(dos.z - uno.z), 2))

    return dist 



def main():
    
    
    mainA1 = dist(base, estacionUno)
    mainA2 = dist(base, estacionDos)
    mainA3 = dist(base, estacionTres)
    
    
    
    print("Ingresa la cantidad de destinos: " )
    x = input()
    x = int(x)
    while (int(x) > 2):

        print("El maximo destino es 2, intenta de nuevo. Cantidad de destino:" )
        x = input()
    r = 0
    print("Lista de destinos: ")
    for i in lugares:
        r += 1
        print(r, i.nombre )
    
    lugUno = 0
    lugDos = 0
 
    distA11 = 0
    distA21 = 0
    distA31 = 0
    
    distA12 = 0
    distA22 = 0
    distA32 = 0
    
    distMasCorta = 0
    distanciaLugares = 0
    
    totalKm = 0
    
    if x == 1:
        print("Primer lugar:")
        lugUno   = int(input())
       
        distA11 =  dist(estacionUno, lugares[lugUno - 1])
        
        distA21 =  dist(estacionDos, lugares[lugUno - 1])
     
        distA31 = dist(estacionTres, lugares[lugUno - 1])
        
    
        if distA11 > distA21 and distA11 > distA31:
          
            distMasCorta = distA11
            totalKm = mainA1 + distMasCorta
            print("Te conviene mas ir de base a Estacion 1 y de ahi a el destino final, dado que la distancia es la mas corta y es: ", totalKm, " Km")
        
        elif distA21 > distA11 and distA21 > distA31:
            
            distMasCorta = distA21
            totalKm = mainA2 + distMasCorta
            print("Te conviene mas ir de base a Estacion 2 y de ahi a el destino final, dado que la distancia es la mas corta y es: ", totalKm, " Km")
            
        elif  distA31 > distA11 and distA31 > distA21:
            
            distMasCorta = distA31
            totalKm = mainA3 + distMasCorta
            print("Te conviene mas ir de base a Estacion 3 y de ahi a el destino final, dado que la distancia es la mas corta y es: ", totalKm, " Km")
              
    elif x == 2:
        print("Primer lugar:")
        lugUno = int(input())
        
        distA11 =  dist(estacionUno, lugares[lugUno - 1])
       
        distA21 =  dist(estacionDos, lugares[lugUno - 1])
     
        distA31 = dist(estacionTres, lugares[lugUno - 1])
        
        print("Segundo Lugar:")
        lugDos  = int(input())
        
        distanciaLugares = dist(lugares[lugUno - 1], lugares[lugDos - 1])
        
        if distA11 > distA21 and distA11 > distA31:
          
            distMasCorta = distA11
            totalKm = mainA1 + distMasCorta + distanciaLugares
            print("Te conviene mas ir de base a Estacion 1 y de ahi a ambas direcciones, dado que la distancia es la mas corta y es: ", totalKm, " Km")
        
        elif distA21 > distA11 and distA21 > distA31:
            
            distMasCorta = distA21
            totalKm = mainA2 + distMasCorta + distanciaLugares
            print("Te conviene mas ir de base a Estacion 2 y de ahi a ambas direcciones, dado que la distancia es la mas corta y es: ", totalKm, " Km")
            
        elif  distA31 > distA11 and distA31 > distA21:
            
            disMasCorta = distA31
            totalKm = mainA3 + distMasCorta + distanciaLugares
            print("Te conviene mas ir de base a Estacion 3 y de ahi a ambas direcciones, dado que la distancia es la mas corta y es: ", totalKm, " Km")
        
        
    
    return 0
    
main()