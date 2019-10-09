//"Cart"
$(document).ready(function() {
    $("#transactionAdderForm").click(function(){
        //$("#mainForm").clone().appendTo("#secondForm");
        //alert('shit!!!')

        var form_idx = $('#id_form-TOTAL_FORMS').val();
        $("#AdderTransactionForm").append("<tr>"+$('#EmptyForm').html().replace(/__prefix__/g, form_idx)+"</tr>");
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
      });
    $("#AdderTransactionForm").on('click', '#btnDelete', function(){
        var form_idx = $('#id_form-TOTAL_FORMS').val();
        $(this).closest('tr').remove();
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) - 1);
    });
});

//"Input Stock"
$(document).ready(function() {
    $("#inputStockAdder").click(function(){
        //$("#mainForm").clone().val("").appendTo("#copiedForm");
        var form_idx = $('#id_form-TOTAL_FORMS').val();
        $("#copiedForm").append("<tr>"+$('#EmptyForm').html().replace(/__prefix__/g, form_idx)+"</tr>");
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
        //alert(form_idx)
      });

    $("#copiedForm").on('click', '#btnDelete', function(){
        var form_idx = $('#id_form-TOTAL_FORMS').val();
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) - 1);
        $(this).closest('tr').remove();
        //alert(form_idx)
    });
});

//function select_barang() {
//    alert(document.getElementById('tes').value);
//};

//Filter Report By Date
$(function() {
  $('input[name="daterange"]').daterangepicker({
    opens: 'left'
  }, function(start, end, label) {
    console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
  });
});
