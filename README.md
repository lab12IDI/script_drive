# Drive Script

Script en python que permite la descaga de muestras desde Drive, para ello utiliza la API de Google. Se puede consultar más información sobre el Script en :

https://citogenetica12.cicancer.org/wiki/index.php?title=Script_Drive

## Requisitos 

* Google API v2
* Python v3

## Instalación

La instalación es muy simple y se encuentra explicada en :
https://citogenetica12.cicancer.org/wiki/index.php?title=Script_Drive

## Functionamiento

Se esta trabajando para automatizar tareas rutinarias, y descargar ficheros desde el Drive es una de las tareas que más se repite. Para ello se está tratanto de automatizar el acceso al drive y el funcionamiento de este script es relativamente sencillo para que cualquiera pueda ejecutarlo. 

### Descarga múltiple de muestras

Para descargar de manera masiva una cantidad de muestras, se debe especificar en un archivo llamado "samples.txt" las muestras que deseamos descargar. En formato lista.

```
MUESTRA_1
MUESTRA_2
MUESTRA_3
MUESTRA_4
MUESTRA_5
```

Esta parte del script realizará una búsqueda recursiva por todo el Drive con la intención de descargar el Excel que contiene los resultados de los análisis. Aunque se puede modificar para realizar búsquedas con otras extensiones, eso lo veremos más adelante. Para ejecutar :

```
python3 main.py --dSamples
```
El proceso que sigue es leer recursivamente todas las carpetas y subcarpetas hasta que llega a la carpeta de análisis (esto se debe optimizar por que tarda bastante) , y una vez llega a esa carpeta descargar el fichero y su configuración. Éste código lo podéis encontrar en el fichero "functions.py" , y dentro de éste en la función downloadSample:

```
	#Si encontramos el fichero de analisis lo descargamos
	if it['name']==i['name']+".xlsx":
		download(it['id'],service,it['name'])
		break

```
Como véis esta parte se puede modificar para descargar otros archivos. ya que sería tan fácil cómo modificar los condicionales. 

PD : El directorio de salida, es el mismo del script.

## Descarga de carpetas

Para descargar ficheros en carpetas completas, deberemos conocer el Identificador de las carpetas,( éste se encuentra en el enlace de google Drive o podemos ejecutar un comando --viewIDs ) después deberemos introducirlos en la variable que se encuentra en el archivo main, y que se llama folders, es un array por lo tanto simplemente agregamos a éste los identificadores, por último ejecutamos el siguiente comando : 
```
python3 main.py --dSelectFolders
```
