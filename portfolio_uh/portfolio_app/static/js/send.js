$('#button-submit').click(function() {
    const userInfo = $('#user-info').val();
    const platformSelect = $('#platform-select').val();
    const csrf = $('[name=csrfmiddlewaretoken]').val();
    const submitButton = $(this);

    if(!userInfo) {
        alert('Please enter the required data');
        return;
    }

    $.ajax({
        url: '/feedback/',
        type: 'POST',
        data: {
            'user-info': userInfo,
            'platform-select': platformSelect,
            'csrfmiddlewaretoken': csrf
        },
        dataType: 'json',
        
        success: function(data) {
            console.log('Success: ', data);
            submitButton.text('success :)');
            submitButton.prop('disabled', true);
            submitButton.css({
                'background-color': '#4682B4',
                'color': '#E0FFFF',
            });
        },

        error: function(error) {
            console.error('Error: ', error);
            submitButton.text('failed to send');
            submitButton.prop('disabled', false);
            submitButton.css({
                'background-color': '#7B68EE',
                'color': '#E6E6FA',
            });
        }
    })
});

$('#login-button').click(function() {
    const login = $('#login').val();
    const password = $('#password').val();
    const csrf = $('[name=csrfmiddlewaretoken]').val();
    const loginButton = $(this);

    if(!login) {
        alert('Пожалуйста, введите логин');
        return;
    }

    if(!password) {
        alert('Пожалуйста, введите пароль');
        return;
    }

    $.ajax({
        url: '/auth/',
        type: 'POST',
        data: {
            'login': login,
            'password': password,
            'csrfmiddlewaretoken': csrf
        },
        dataType: 'json',
        
        success: function(data) {
            console.log('Success: ', data);
            window.location.href='/';
        },

        error: function(error) {
            alert('wrong username or password');
            console.error('Error: ', error);
        }
    })   
});

$('#reg-button').click(function() {
    const username = $('#username').val();
    const password = $('#password').val();
    const firstName = $('#first-name').val();
    const lastName = $('#last-name').val();
    const email = $('#email').val();
    const csrf = $('[name=csrfmiddlewaretoken]').val();

    if(!username) {
        alert('Пожалуйста, введите логин');
        return;
    }

    if(!password) {
        alert('Пожалуйста, введите пароль');
        return;
    }

    $.ajax({
        url: '/reg/',
        type: 'POST',
        data: {
            'username': username,
            'first-name': firstName,
            'last-name': lastName,
            'password': password,
            'email': email,
            'csrfmiddlewaretoken': csrf
        },
        dataType: 'json',
        
        success: function(data) {
            console.log('Success: ', data);
            window.location.href='/';
        },

        error: function(error) {
            console.error('Error: ', error);
        }
    })   
});