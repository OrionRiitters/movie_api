$('#submit-form').on('click', function(e) {
    e.preventDefault();

    $('.info-bit').remove();

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
            let dataObj = JSON.parse(data);
            jsonToHTML(dataObj);

        });
});

