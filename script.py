import sys
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element, SubElement

def obtener_nombres(archivo):
    lista=[]
    tree = ET.ElementTree(file = archivo)


    contador = 0

    nombre_archivo = archivo.split('.')

    for elem in tree.iterfind('way'):
        bandera_Altname=0
        bandera_name=0
        nombre_completo=""
        altname_completo=""
        for subelem in elem.iterfind('tag'):

            if(subelem.attrib['k'] == "name"):
                nombre_completo = subelem.attrib['v']
                etiqueta_nombre=subelem.attrib['v'].split(' ')

                if verificar_etiqueta(etiqueta_nombre[0])== 1 :  #primera palabra

                    if(len(etiqueta_nombre)!=1):

                        if(etiqueta_nombre[1]==''):
                            segunda_palabra=2
                        else:
                            segunda_palabra=1

                        if verificar_numero(etiqueta_nombre[segunda_palabra][0])==1 or etiqueta_nombre[segunda_palabra] =="Central": #primer letra de la segunda palabra
                                bandera_name=1

            if(subelem.attrib['k'] == "alt_name"):

                altname_completo=subelem.attrib['v']
                etiqueta_altname=subelem.attrib['v'].split(' ')
                bandera_Altname=1

        if(bandera_Altname==1 and bandera_name==1):
            elem.set('action', 'modify')

            contador+=1
            for subelem in elem.iterfind('tag'):

                if(subelem.attrib['k'] == "name"):
                    if verificar_etiqueta(etiqueta_altname[0])== 1 :
                        subelem.attrib['v']=altname_completo
                    else:
                        subelem.attrib['v']=etiqueta_nombre[0]+ " " +altname_completo
                        #print(subelem.attrib['v'])
                if(subelem.attrib['k']== "alt_name"):
                    subelem.attrib['v']=nombre_completo


    tree.write(nombre_archivo[0] + '_new.osm')




def verificar_etiqueta(etiqueta):
    lista = ['Paseo','Río', 'Avenida', 'Hacienda', 'Puerto', 'Callejón', 'Calle', 'Calzada', 'Camino', 'Av.','Paso', 'Cañada', 'Minas', 'Cerrada',
    'Puebla', 'Principal', 'Central','Primera', 'Segunda', 'Portón', 'Lateral', 'Calz.', 'Corrido', 'Casa', 'Villa', 'Mejía',
    'Vía', 'Via', 'Real', 'Isla', 'Avendida', 'Marisma', 'Rada', 'Raudal', 'Ribera', 'Embocadura', 'Cataratas', 'Médanos',
    'Mirador', 'Av', 'Jardín',  'A.', 'Circuito','Gral.', 'Rincón', 'Calz', 'Rinconada', 'Periférico', 'Cda', 'Jardin',
    'C.', 'Callejon', 'Colegio', 'Valle', 'avenida', 'camino', 'calle', 'Calle', 'Rotonda', 'Parqueo', 'Parque', 'entrada',
    'Entrada', 'sendero', 'Sendero', 'Pasaje', 'pasaje', 'Puerto', 'Ciudad', 'Puente', 'Boulevard', 'Agrosuperior', 'Bodegas',
    'Autobanco', 'SkyTrace', 'Plaza', 'Motel', 'C/', 'Rotonda', 'Drive', 'Residencial', 'Automac',
    'Auto', 'Transcersal', 'Inter', 'Pasillo', 'Centro', 'Caminito', 'Arandas', 'Proveedores', 'Cajero', 'Zona', 'Primer', 'Res.']
    for i in lista:
        if i == etiqueta:
            return 1

    return 0


#revisa que tenga un numero
def verificar_numero(numero):
    lista= ["0","1","2","3","4","5","6","7","8","9"]
    for i in lista:
        if i == numero:
            return 1

    return 0

def verificarargumentos():
    nombre_archivo = sys.argv[1].split('.')

    if len(sys.argv)!= 2:
        print("Cantidad de argumentos invalida. Debe ejecutarse con un archivo como parametro")
        exit(0)

    if nombre_archivo[1] != "osm":
        print("Formato de archivo invalido. Debe ser un .osm")
        exit(0)

    else:
        obtener_nombres(sys.argv[1])

def main():
	verificarargumentos()
main()
