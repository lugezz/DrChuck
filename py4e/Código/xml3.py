import xml.etree.ElementTree as ET


tree = ET.parse('siradig_prueba.xml')
stuff = tree.getroot()

lst = stuff.findall('deducciones/deduccion')
print('Deducciones count:', len(lst))

for item in lst:
    print('Denominación', item.find('denominacion').text)
    print('Descripción', item.find('descBasica').text)
    print('Tipo Deducción', item.get('tipo'))

    lst2 = item.findall('periodos/periodo')
    for item2 in lst2:
        print("*" * 50)
        print(f'Desde: {item2.get("mesDesde")}, Hasta: {item2.get("mesHasta")}, Monto Mensual: {item2.get("montoMensual")}')
        print("*" * 50)
