var submitData = $('#the-form').serializeArray();

/*     Using $.get is easier
  $.ajax({
    type: 'POST',
    url: 'web_server/serv.py',
    data: 'submitData',
    dataType: 'json',
    contentType: 'application/json'
});
*/

$('#sponsor-yes').on('click', function(e) {
    e.preventDefault();
    $.ajax(
        'queryResults.json',
        {
         data: submitData,
         processData: false
        }
    )
        .done((data) => {
            console.log('Response from serv.py received..');
            console.log(data);
            var dataObj = JSON.parse(data);
            $('.jumbotron').val(JSON.stringify(dataObj));
            console.log(JSON.stringify(dataObj))
        });
});

