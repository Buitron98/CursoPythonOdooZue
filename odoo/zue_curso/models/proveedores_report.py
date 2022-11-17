from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError

import base64
import io
import xlsxwriter

class zue_curso_proveedores_print_report(models.TransientModel):
    _name = 'zue_curso.proveedores_print_report'
    _description = 'Imprimir reporte de proveedores'

    report_id = fields.Many2one('zue_curso.report_proveedores', string='Reporte')
    excel_file = fields.Binary(string='Excel')
    excel_filename = fields.Char(string='Excel filename')


    def print_report(self):
        datas = {
            'id': self.id,
            'model': 'zue_curso.proveedores_print_report'
        }

        return {
            'type':'ir.actions.report',
            'report_name':'zue_curso.report_list_proveedores',
            'report_type':'qweb-html',
            'datas':datas
        }

    def print_report_excel(self):
        #Crear excel
        filename = 'Reporte_proveedores.xlsx'
        stream = io.BytesIO()
        book = xlsxwriter.Workbook(stream,{'in_memory':True})
        #Crear hoja del excel
        sheet = book.add_worksheet('Proveedores')

        #Crear contenido hoja 1

        #Titulo reporte
        cell_format_title = book.add_format({'bold':True,'align':'center'})
        cell_format_title.set_font_name('Calibri')
        cell_format_title.set_font_size(20)
        cell_format_title.set_font_color('#1F497D')
        text_title = self.report_id.name
        sheet.merge_range('A1:D1',text_title,cell_format_title)

        #Contenido del reporte / Columnas tabla
        columns = ['Nombre','Identificación','Tipo','Valor']
        aument_columns = 0
        for column in columns:
            sheet.write(1,aument_columns,column)
            aument_columns += 1

        # Contenido del reporte / Detalle tabla
        # <tr t-foreach="o.report_id.proveedor_ids" t-as="p">
        aument_rows = 2
        for p in self.report_id.proveedor_ids:
            sheet.write(aument_rows, 0, p.complate_name)
            sheet.write(aument_rows, 1, f"{p.type_document}-{p.num_document}")
            if p.type_proveedor == 'a':
                type_proveedor = 'Adquiriente'
            elif p.type_proveedor == 'b':
                type_proveedor = 'Prestamista'
            else:
                type_proveedor = 'Publico'
            sheet.write(aument_rows, 2, type_proveedor)
            sheet.write(aument_rows, 3, p.value)
            aument_rows += 1

        #Tamaños columnas
        sheet.set_column(0,0,40)
        sheet.set_column(1, 1, 40)
        sheet.set_column(2, 2, 40)
        sheet.set_column(3, 3, 40)

        #Convertir en tabla
        array_header_table = []
        for i in columns:
            dict = {'header':i}
            array_header_table.append(dict)

        sheet.add_table(1,0,aument_rows-1,len(columns)-1,{'style': 'Table Style Medium 2','columns':array_header_table})

        #Pagina 2
        sheet_two = book.add_worksheet('Info Detallada')
        text_title_two = 'Información Detallada'
        sheet_two.merge_range('A1:H1', text_title_two, cell_format_title)

        #Cerrar excel
        book.close()

        #Guardamos el excel
        self.write({
            'excel_file': base64.encodestring(stream.getvalue()),
            'excel_filename': filename
        })

        #Descargar el excel
        action = {
            'name': 'Reporte proveedores excel',
            'type': 'ir.actions.act_url',
            'url': 'web/content/?model=zue_curso.proveedores_print_report&id='+str(self.id)
                   +'&filename_field=excel_filename&field=excel_file&download=true&filename='+self.excel_filename,
            'target':'self',
        }

        return action

    def print_report_excel_sql(self):
        #Crear excel
        filename = 'Reporte_proveedores.xlsx'
        stream = io.BytesIO()
        book = xlsxwriter.Workbook(stream,{'in_memory':True})
        #Crear hoja del excel
        sheet = book.add_worksheet('Proveedores')

        #Crear contenido hoja 1

        #Titulo reporte
        cell_format_title = book.add_format({'bold':True,'align':'center'})
        cell_format_title.set_font_name('Calibri')
        cell_format_title.set_font_size(20)
        cell_format_title.set_font_color('#1F497D')
        text_title = self.report_id.name
        sheet.merge_range('A1:D1',text_title,cell_format_title)

        #Contenido del reporte / Columnas tabla
        columns = ['Nombre','Identificación','Tipo','Valor']
        aument_columns = 0
        for column in columns:
            sheet.write(1,aument_columns,column)
            aument_columns += 1

        # Contenido del reporte / Detalle tabla
        query = '''
            select complate_name,
                    type_document || '-' || num_document as identificacion,
                    case when type_proveedor = 'a' then 'Adquiriente' 
                         when type_proveedor = 'b' then 'Prestamista'
                    else 'Publico' end as type_proveedor,
                    value  
            from zue_curso_proveedores zcp  
        '''
        try:
            self._cr.execute(query)
        except Exception as e:
            raise ValidationError('La consulta fallo, motivo: '+str(e))

        result_query = self._cr.dictfetchall()

        # Imprimir Diccionario en Excel
        aument_columns = 0
        aument_rows = 2
        for query in result_query:
            for row in query.values():
                sheet.write(aument_rows, aument_columns, row)
                aument_columns += 1
            aument_columns = 0
            aument_rows += 1

        #Tamaños columnas
        sheet.set_column(0,0,40)
        sheet.set_column(1, 1, 40)
        sheet.set_column(2, 2, 40)
        sheet.set_column(3, 3, 40)

        #Convertir en tabla
        array_header_table = []
        for i in columns:
            dict = {'header':i}
            array_header_table.append(dict)

        sheet.add_table(1,0,aument_rows-1,len(columns)-1,{'style': 'Table Style Medium 2','columns':array_header_table})

        #Pagina 2
        sheet_two = book.add_worksheet('Info Detallada')
        text_title_two = 'Información Detallada'
        sheet_two.merge_range('A1:H1', text_title_two, cell_format_title)

        #Cerrar excel
        book.close()

        #Guardamos el excel
        self.write({
            'excel_file': base64.encodestring(stream.getvalue()),
            'excel_filename': filename
        })

        #Descargar el excel
        action = {
            'name': 'Reporte proveedores excel',
            'type': 'ir.actions.act_url',
            'url': 'web/content/?model=zue_curso.proveedores_print_report&id='+str(self.id)
                   +'&filename_field=excel_filename&field=excel_file&download=true&filename='+self.excel_filename,
            'target':'self',
        }

        return action
