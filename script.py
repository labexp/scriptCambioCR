import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element, SubElement



def obtener_nombres():
    tree = ET.ElementTree(file='chepe.osm')

    root = tree.getroot()


    # price - raise the main price and insert new tier

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
                    print(etiqueta_nombre)
                    if(len(etiqueta_nombre)!=1):
                        if(etiqueta_nombre[1]==''):
                            segunda_palabra=2
                        else:
                            segunda_palabra=1
                        if verificar_numero(etiqueta_nombre[segunda_palabra][0])==1 or etiqueta_nombre[segunda_palabra] =="Central": #primer letra de la segunda palabra
                                bandera_name=1


            if(subelem.attrib['k'] == "alt_name"):
                altname_completo=subelem.attrib['v']
                bandera_Altname=1

        if(bandera_Altname==1 and bandera_name==1):
            for subelem in elem.iterfind('tag'):
                if(subelem.attrib['k'] == "name"):
                    subelem.attrib['v']=altname_completo
                if(subelem.attrib['k']== "alt_name"):
                    subelem.attrib['v']=nombre_completo

        elif(bandera_Altname==1 and bandera_name!=1):
            print(altname_completo)
            print(nombre_completo)
            print("_______________________________________")
    tree.write('file_new.osm')




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



def main():
    obtener_nombres()

if __name__== "__main__":
  main()
