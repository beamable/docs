# HTML Sign-In

## Overview

The purpose of this guide is to demonstrate everything needed for game makers to set up a web page which handles Beamable login and account administration.
In this guide we will have a step-by-step approach to creating a simple HTML page that can log in users and retrieve their account information. After following through this guide, the new HTML login will be functional and ready for any additional branding and customization.
This web page may be setup in a game specific or studio specific setting. It is recommended to have some basic knowledge of web development, including basic HTML and JavaScript before continuing.

## Creating HTML Login Page

### Setup Website HTML

The first step is to create the login page itself. Ultimately, this will be hosted in a durable and highly available fashion, with [SSL/TLS](https://cybernews.com/resources/web-hosting-glossary/#ssl-tls) security and a hostname. However for starting out we can go with a simple file on your machine, something like `file:///Users/exampleuser/Projects/Beamable/index.html`.

The login page needs a form that gathers email and password.

```html
<form onsubmit="return login(event)">
    <label>Email: <input type="text" name="username" id="login-username"></label>
    <label>Password: <input type="password" name="password" id="login-password"></label>
    <input type="submit" value="Login">
</form>
```

### Setup Login JavaScript

In the HTML above, the Login button refers to a JavaScript function that does not yet exist, namely `login()`. Let’s use a bit of jQuery to retrieve the username and password values from the form and then pass them along to the `/basic/auth/token` endpoint.

The CID value is a decimal number that can be found in the Unity project at `\Assets\Beamable\Resources\config-defaults.txt` or the Beamable Portal. Substitute your own CID as shown when logging into the Beamable Portal from within Unity.

```javascript
function login(evt) {
    evt.preventDefault();
    const cid = 'YOUR_CID';
    const pid = 'YOUR_PID';
    const scope = cid + '.' + pid;
    let request = $.ajax('https://api.beamable.com/basic/auth/token', {
        method: 'POST',
        headers: {'X-DE-SCOPE': scope},
        data: {
            grant_type: 'password',
            username: $('#login-username').val(),
            password: $('#login-password').val(),
        }
    });
    return false;
}
```

!!! info "Logging into a realm"
    Using only your CID in the X-DE-SCOPE header is accepted, but for almost all purposes, logging into a specific realm (CID.PID) is better.

### Setup Account Information Retrieval

The response for a successful login is a Json object containing an OAuth access token, the corresponding refresh token, and information about the token type (always ‘Bearer’ in our case) and expiration time. With the access token in hand, we can now retrieve account data from the `/basic/accounts/me` endpoint.

```javascript
request.done(function(data) {
        let accessToken = data.access_token;
        let refreshToken = data.refresh_token;
        $.ajax('https://api.beamable.com/basic/accounts/me', {
            method: 'GET',
            headers: {
                'X-DE-SCOPE': scope,
                Authorization: 'Bearer ' + accessToken,
            }
        }).done(function(accountData) {
            $('#account-output').text(JSON.stringify(accountData));
        });
    });
```

!!! info "Best Practice"
    In a production implementation, save the refresh token to persistent storage such as browser cookies or other client storage.

### Complete HTML and JavaScript Sample

The document below ties together all the pieces from the step by step instructions above.

```html
<!DOCTYPE html>
<html lang="en">
<head><title>Example Studio Login</title></head>
<body>

<script src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
<script>
function login(evt) {
    evt.preventDefault();
    const cid = 'YOUR ORGANIZATION ID FROM PORTAL';
    const pid = 'YOUR_PID';
    const scope = cid + '.' + pid;
    let request = $.ajax('https://api.beamable.com/basic/auth/token', {
        method: 'POST',
        headers: {'X-DE-SCOPE': scope},
        data: {
            grant_type: 'password',
            username: $('#login-username').val(),
            password: $('#login-password').val(),
        }
    });
    request.done(function(data) {
        let accessToken = data.access_token;
        let refreshToken = data.refresh_token;
        $.ajax('https://api.beamable.com/basic/accounts/me', {
            method: 'GET',
            headers: {
                'X-DE-SCOPE': scope,
                Authorization: 'Bearer ' + accessToken,
            }
        }).done(function(accountData) {
            $('#account-output').text(JSON.stringify(accountData));
        });
    });
    return false;
}
</script>

<form onsubmit="return login(event)">
    <label>Email: <input type="text" name="username" id="login-username"></label>
    <label>Password: <input type="password" name="password" id="login-password"></label>
    <input type="submit" value="Login">
</form>

<div>
    <samp><span id="account-output"></span></samp>
</div>

</body>
</html>
```

!!! warning "CID-scoped logins"
    When the scope field is in `{{cid}}.{{pid}}` form, that is a realm-scoped login, the standard login for players. For some purposes, such as administrative tools, you may want a CID-scoped login, which will yield a token that is pertinent to your organization as a whole, rather than a specific realm.
    
    In the case of CID-scoped logins, you must include 'customerScoped=true' in the body.
