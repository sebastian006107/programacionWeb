$(document).ready(function () {
    $("#loginForm").submit(function (event) {
        event.preventDefault();
        let isValid = true;

        $(".error-message").hide().text("");
        $(".form-control").removeClass("is-invalid");


        const email = $("#correo").val().trim();
        if (email === "") {
            $("#correo").addClass("is-invalid");
            $("#correo").next(".error-message").text("El correo es obligatorio.").show();
            isValid = false;
        } else {

            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                $("#correo").addClass("is-invalid");
                $("#correo").next(".error-message").text("Ingresa un email válido.").show();
                isValid = false;
            }
        }


        const password = $("#clave").val().trim();
        if (password === "") {
            $("#clave").addClass("is-invalid");
            $("#clave").next(".error-message").text("La contraseña es obligatoria.").show();
            isValid = false;
        } else if (password.length < 6) {
            $("#clave").addClass("is-invalid");
            $("#clave").next(".error-message").text("La contraseña debe tener al menos 6 caracteres.").show();
            isValid = false;
        }


        if (isValid) {
            alert("¡Inicio de sesión exitoso!");
            $("#loginForm")[0].reset();
            

            $(".error-message").hide();
            $(".form-control").removeClass("is-invalid");
        }
    });
});