$(document).ready(function(){
    $('#quantity, #unit_price').on('input', function() {
        $.post("{% url 'quantity_analysis' %}", {  // Sends data to Django
            quantity: $('#quantity').val(),
            unit_price: $('#unit_price').val(),
            csrfmiddlewaretoken: '{{ csrf_token }}'  // Security token
        }, function(response) {
            $('#total_price').val(response.total_price || '');  // Updates the Total Price field
        });
    });
});
