

/*     Using $.get is easier
  $.ajax({
    type: 'POST',
    url: 'web_server/serv.py',
    data: 'submitData',
    dataType: 'json',
    contentType: 'application/json'
});
*/

$('#submit-form').on('click', function(e) {
    e.preventDefault();

    let submitData = $('#film-title').select()[0].value.split(' ');
    let omdb_url = 'http://www.omdbapi.com/?apikey=c346dee9&t=';

    submitData.forEach((data) => {
        omdb_url += data + '+';
    });

    omdb_url = omdb_url.slice(0, omdb_url.length-1);
    $.ajax(
        'placeholder',
        {
         data: omdb_url
        }
    )
        .done((data) => {
            console.log('Response from serv.py received..');
            console.log(data);
            var dataObj = JSON.parse(data);
            $('.jumbotron').val(JSON.stringify(dataObj));
        });
});

