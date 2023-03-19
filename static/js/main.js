$(document).ready(function () {
    $('#logout_btn').click(function () {
        $.ajax({
            url: logout_url,
            data: {},
            success: function (result) {
                if (result == 'ok') {
                    location.reload()
                }
            }
        })
    })
})