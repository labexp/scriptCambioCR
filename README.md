# SCRIPT de cambio masivo para las calles de Costa Rica 


Visita la página de la propuesta del proyecto(https://wiki.openstreetmap.org/wiki/ES_talk:Propuesta_para_el_nombramiento_de_calles_en_Costa_Rica) 

## Getting Started


El cambio masivo del nombramiento de calles en Costa Rica se realizó con un script y varias herramientas para tomar los datos de open street maps(OSM)



### Instalación y preparación de entorno

Para hacer esto se necesita tener descargado el repositorio, JOSM , Python3 y pip3:

* GITHUB (Descargar [AQUí](https://github.com/labexp/scriptCambioCR.git))
* JOSM (Descargar [AQUí](https://josm.openstreetmap.de/wiki/Download))
* Python3 (Descargar [AQUí](https://www.python.org/downloads/))
* Pip3 (Descargar [AQUí](https://www.tecmint.com/install-pip-in-linux/)) 


Descargar el proyecto:

```
git clone https://github.com/labexp/scriptCambioCR.git
```



Instrucciones
======

### _Paso 1_

Ingresar en JOSM, darle click en archivo->descargar datos, luego pulsar la pestaña "descargar de la API de overpass" y en el cuadro de texto copie el contenido del documento overpass.txt. Finalmente dar click en descargar. 
Esto va a generar un archivo .osm el cuál deberá guardarlo en la carpeta en donde se encuentre script.py


### _Paso 2_

Ejecución del código:

Abra la terminal en la carpeta mencionada en el punto anterior y ejecute lo siguiente:
        
```
python3 script.py <nombre del archivo>
```
    

### _Paso 3_

Abrir nuevamente JOSM y darle click en la pestaña archivo->abrir y busca el archivo .osm que se genera a partir del script. Una vez abierto el archivo darle click al ícono con una flecha verde apuntando hacia arriba que aparece en la parte superior, con esto se actualizarán los datos que hayan sido modificados por el script. 
