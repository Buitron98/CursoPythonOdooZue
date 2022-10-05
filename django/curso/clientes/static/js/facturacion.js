$(document).ready(function(){
    var rowCount = 0;
    var table_detalle = document.getElementById("TablaDetalleFactura");
    for (var i = 0; i < table_detalle.children[1].children.length; i++) {
        rowCount = i+1;
        table_detalle.children[1].children[i].children[0].children[0].name = 'rel_producto_'+rowCount.toString();
        table_detalle.children[1].children[i].children[1].children[0].name = 'cantidad_'+rowCount.toString();
        table_detalle.children[1].children[i].children[2].children[0].name = 'precio_unitario_'+rowCount.toString();
        table_detalle.children[1].children[i].children[3].children[0].name = 'precio_total_'+rowCount.toString();
    }
})

//Funcionamiento detalle de factura
$(function(){
    $(document).on("click",".agregarItemDetalle", function(){
        var rowCount = $('.date-item').length + 1;
        var select_productos = document.getElementById("field_rel_producto");
        var item_line = '<tr class="date-item">' +
                          '<td>'+select_productos.outerHTML.replace('hidden="hidden" ',' ').replace('name="rel_producto_item"','name="rel_producto_'+rowCount.toString()+'"')+'</td>' +
                          '<td><input type="number" class="form-control" name="cantidad_'+rowCount.toString()+'"></td>' +
                          '<td><input type="number" step="0.01" class="form-control" name="precio_unitario_'+rowCount.toString()+'"></td>' +
                          '<td><input type="number" step="0.01" class="form-control" name="precio_total_'+rowCount.toString()+'"></td>' +
                          '<td><button type="button" id="btnEliminarItemDetalle" class="eliminarItemDetalle btn btn-sm btn-outline-danger">Eliminar</button></td>' +
                      '</tr>';
        $('#TablaDetalleFactura').append(item_line);
    });

    $(document).on("click",".eliminarItemDetalle", function(){
        $(this).closest("tr").remove();
        // Asignar item nuevamente
        var rowCount = 0;
        var table_detalle = document.getElementById("TablaDetalleFactura");
        for (var i = 0; i < table_detalle.children[1].children.length; i++) {
            rowCount = i+1;
            table_detalle.children[1].children[i].children[0].children[0].name = 'rel_producto_'+rowCount.toString();
            table_detalle.children[1].children[i].children[1].children[0].name = 'cantidad_'+rowCount.toString();
            table_detalle.children[1].children[i].children[2].children[0].name = 'precio_unitario_'+rowCount.toString();
            table_detalle.children[1].children[i].children[3].children[0].name = 'precio_total_'+rowCount.toString();
        }
    });
})