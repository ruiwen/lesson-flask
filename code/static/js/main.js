
console.log("hello world!");

// $(window).on('beforeunload', function() {
//     return "Stooop!"
// });

$(document).ready(function() {

    // Bind the event handler in $(document).ready()
    // callback because the form may not be ready to be bound
    // at the point this script is loaded
    $('form').submit(function (evt) {
        evt.preventDefault();

//         alert("submitted!");

//         return false;

        // http://api.jquery.com/jQuery.ajax/
        $('#results pre').text('');
        $.ajax({
            method: 'POST',
            data: getFormData($('form')),
            success: function(data, xhr, status) {
                $('#results pre').text(data);
            },
            error: function(xhr, status, error) {
                console.log("Error!: ", status, error);
                $('#results pre').text("OH NO")
            }
        })
    });

    // We can also use jQuery to change CSS attributes
    // but perhaps this isn't the best idea
    $('input[type=checkbox]').change(function(evt) {
        if (this.checked) {
            $('label[for=human_field]').css('color', 'blue');
        }
        else {
            $('label[for=human_field]').css('color', 'red');
        }
    });
});

function nameChange (evt) {
    var val = $('input[name=name]').val();
    if (val && val.length > 0) {
        $('#greeting').text("Hello " + val);
    }
    else {
        $('#greeting').text('');
    }
}

function getFormData($form){
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function(n, i){
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}