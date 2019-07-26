import overpy

def cambio_de_calles(result):

    print("_________________________________________________________________")
    print(result.ways)
    for way in result.ways:
        #print("soy un nombre")
        #print(way.tags.get("name"," "))
        #print("soy un alt name")
        #print(way.tags.get("alt_name"," "))
        #result.ways[way].tags.get("name"," ")="asd"
        nombre_completo= way.tags.get("name"," ")
        etiqueta_nombre=nombre_completo.split(' ')
        nombre_alterno= way.tags.get("alt_name"," ")
        etiqueta_alt_name=nombre_alterno.split(' ')




        if(nombre_completo != " " and nombre_alterno!= " "):
            if verificar_etiqueta(etiqueta_nombre[0])== 1 :  #primera palabra
                if verificar_numero(etiqueta_nombre[1][0])==1: #primer letra de la segunda palabra

                    print(nombre_completo)
                    print(nombre_alterno) #aqui hay que hacer un set



    return result


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
    api = overpy.Overpass()
    result = api.query("""[out:json][timeout:25];(way["highway"](10.005388733188,-84.224066734314,10.024279593607,-84.201428890228););out;""")
    #print(result)
    print(type(result))
    resultado=cambio_de_calles(result)

if __name__== "__main__":
  main()
