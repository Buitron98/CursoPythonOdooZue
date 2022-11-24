import pandas
#Libreria comunicación
import xmlrpc.client

# Parametros conexión
url = 'http://localhost:8069'
db = 'DevCurso'
username = 'admin'
password = 'admin'

#Conexión
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db,username,password,{})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

#---------------------------- CRUD ---------------------------------------

# Consultar campos de un modelo
'''
fields_proveedores = models.execute_kw(db,uid,password,'zue_curso.proveedores','fields_get',[],{'attributes':['string','help','type']})
print(fields_proveedores)
'''
# Consultar información
info_proveedores = models.execute_kw(db,uid,password,'zue_curso.proveedores','search_read',[],{'fields':['complate_name','type_document','num_document','type_proveedor','value']})

df_info_proveedores = pandas.DataFrame(info_proveedores)

print(df_info_proveedores)

# Crear un registro
'''
complate_name = input('Digite su nombre: ')
type_document = input('Digite su tipo documento: ')
num_document = input('Digite su número documento: ')
date_vinculation = input('Digite la fecha de vinculación: ')
value = input('Digite su valor: ')

dict_proveedor = {
    'complate_name':complate_name,
    'type_document':type_document,
    'num_document':num_document,
    'date_vinculation':date_vinculation,
    'active': True,
    'type_proveedor':'a',
    'value': float(value),
}
new_proveedor = models.execute_kw(db,uid,password,'zue_curso.proveedores','create',[dict_proveedor])
print('Id con el cual se creo el registro: '+str(new_proveedor))
'''

#Actualizar un registro
'''
ids_proveedor = models.execute_kw(db,uid,password,'zue_curso.proveedores','search',[[['complate_name','=','Juanito']]])
print('------ Ids a actualizar -------')
print(ids_proveedor)
dict_proveedor = {
    'complate_name':'Update name API',
}
update_proveedor = models.execute_kw(db,uid,password,'zue_curso.proveedores','write',[ids_proveedor,dict_proveedor])
print('------ Info actualizada -------')
print(update_proveedor)
'''

#Eliminar un registro
'''
ids_proveedor = models.execute_kw(db,uid,password,'zue_curso.proveedores','search',[[['complate_name','ilike','API']]])
print('------ Ids a eliminar -------')
print(ids_proveedor)
delete_proveedor = models.execute_kw(db,uid,password,'zue_curso.proveedores','unlink',[ids_proveedor])
print('------ Info eliminada -------')
print(delete_proveedor)
'''