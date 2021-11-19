(function() {
    "use strict";

    var treeviewMenu = $('.app-menu');

    // Toggle Sidebar
    $('[data-toggle="sidebar"]').click(function(event) {
        event.preventDefault();
        $('.app').toggleClass('sidenav-toggled');
    });

    // Activate sidebar treeview toggle
    $("[data-toggle='treeview']").click(function(event) {
        event.preventDefault();
        if (!$(this).parent().hasClass('is-expanded')) {
            treeviewMenu.find("[data-toggle='treeview']").parent().removeClass('is-expanded');
        }
        $(this).parent().toggleClass('is-expanded');
    });

    // Set initial active toggle
    $("[data-toggle='treeview.'].is-expanded").parent().toggleClass('is-expanded');

    //Activate bootstrip tooltips
    $("[data-toggle='tooltip']").tooltip();

})();

// Funcion para aadir los productos a la tabla
function agregar_producto() {
    let idProducto = $("#Producto").val()
    let textproducto = $("#Producto option:selected").text()
    let textcantidad = $("#cantidadProducto").val()

    $("#tbl_productos").append(
        "<tr id='tr" + textcantidad + "'> <input type='hidden' name='producto_id[]' value='" + idProducto + "'> <input type='hidden' name='cantidad[]' value='" + textcantidad + "'>  <td>" + textproducto + "</td><td>" + textcantidad + "</td><td><button type='button' onclick='$(" + '"' + "#tr" + textcantidad + '"' + ").remove()' class='btn btn-danger'><i class='fa fa-times-circle' aria-hidden='true'></i></button></td></tr>"
    )
}

// funcion para abrir modals Registrar cliente
var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

$('#myModal').on('shown.bs.modal', function() {
    $('#myInput').trigger('focus')
})