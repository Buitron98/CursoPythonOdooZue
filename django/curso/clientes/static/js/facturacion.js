$(document).ready(function(){
    alert('Javascript ejecución');
})

// Funcionamiento grilla detalle
$(function(){
        $(document).on("click",".agregarItemDetalle", function(){
            var item_line = '<tr>' +
                              '<td><input type="text" class="form-control"></td>' +
                              '<td><input type="number" class="form-control"></td>' +
                              '<td><input type="number" class="form-control"></td>' +
                              '<td><input type="number" class="form-control"></td>' +
                              '<td><button type="button" id="btnEliminarItemDetalle" class="eliminarItemDetalle btn btn-sm btn-outline-danger">Eliminar</button></td>' +
                          '</tr>';
            $('#TablaDetalleFactura').append(item_line);
        });

        $(document).on("click",".eliminarItemDetalle", function(){
            $(this).closest("tr").remove();
        });

    })