var submitData = JSON.stringify($('#the-form').serializeArray());
console.log('asdfasdfasdfasdf');

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
    $.get('/serv.py',
          submitData,
          (data) => {
              console.log('Response from serv.py received..');
              var dataObj = JSON.parse(data);
              $('.jumbotron').val();
          });
});
