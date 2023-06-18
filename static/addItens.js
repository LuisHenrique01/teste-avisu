$(document).ready(function () {
    var init = parseInt($('#id_elementos-INITIAL_FORMS').val())
    var total = parseInt($('#id_elementos-TOTAL_FORMS').val())
    var formsetCount = init !== total ? total : init;


    function generateFormsetHtml() {
        var formsetHtml = $("#div_id_elementos-0-nome").html();
        formsetHtml = formsetHtml.replace(/id_elementos-0-nome/g, `id_elementos-${formsetCount}-nome`);
        formsetHtml = formsetHtml.replace(/elementos-0-nome/g, `elementos-${formsetCount}-nome`);
        return formsetHtml;
    }

    function addFormset() {
        var formsetHtml = generateFormsetHtml();
        $("#formset-container").append(formsetHtml);
        formsetCount++;
    }

    function addTotalElements() {
        $('#id_elementos-TOTAL_FORMS').val(formsetCount.toString())
    }

    $("#add-more-btn").on("click", function () {
        addFormset();
        addTotalElements();
    });
});