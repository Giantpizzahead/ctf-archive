function login() {
    $("#err_message").slideUp("fast"), $.ajax({
        type: "POST",
        url: "api.php",
        data: {
            username: $("#username").val(),
            password: $("#password").val(),
            action: "login"
        },
        dataType: "json",
        success: function(e) {
            1 == e.code ? ($("#mfa_recepient").html(e.mfa), $("#mfa_user_token").val(e.login_session_token), $("#login").slideUp(), $("#mfa").slideDown()) : ($("#err_message").html(e.message), $("#err_message").slideDown())
        }
    })
}

function proceed_login() {
    $("#err_message").slideUp("fast");
    var e = $("#captcha_code").val(),
        a = $("#mfa_user_token").val(),
        s = $("#username").val(),
        t = $("#mfa_code").val();
    fetch("mfa_service.php?captchacode=" + e, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Accept: "application/json"
        },
        body: JSON.stringify({
            query: "query submit_mfa_token($code: String!, $usertoken: String!, $username: String!) { submit_mfa_token(code: $code, usertoken: $usertoken, username: $username) }",
            variables: {
                code: t,
                usertoken: a,
                username: s
            }
        })
    }).then(e => e.json()).then(e => {
        4 == e.code ? ($("#err_message").html(e.message), $("#err_message").slideDown(), $("#captcha")[0].src = "./securimage/securimage_show.php?time=" + (new Date).getTime(), $("#captcha_code").val("")) : 1 == JSON.parse(e.data.submit_mfa_token).code ? document.location = JSON.parse(e.data.submit_mfa_token).redirect : ($("#err_message").html(JSON.parse(e.data.submit_mfa_token).message), $("#err_message").slideDown(), setTimeout(function() {
            location.reload()
        }, 3e3))
    })
}