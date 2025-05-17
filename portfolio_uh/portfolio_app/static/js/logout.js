$('#logout').click(function() {
    const csrf = $('[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: '/logout/',
        type: 'POST',
        data: {
            'logout': true,
            'csrfmiddlewaretoken': csrf
        },
        dataType: 'json',
        
        success: function(data) {
            console.log('Success: ', data);
            window.location.href = '/';
        },

        error: function(error) {
            console.error('Error: ', error);
        }
    })
});
