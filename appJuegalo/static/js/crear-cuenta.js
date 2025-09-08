$(document).ready(function () {
    $("#registroForm").submit(function (event) {
        event.preventDefault();
        let isValid = true;


        $(".error-message").hide().text("");
        $(".form-control, .form-select").removeClass("is-invalid");


        if ($("#nombre").val().trim() === "") {
            $("#nombre").addClass("is-invalid");
            $("#nombre").next(".error-message").text("El nombre es obligatorio.").show();
            isValid = false;
        }


        if ($("#apellidos").val().trim() === "") {
            $("#apellidos").addClass("is-invalid");
            $("#apellidos").next(".error-message").text("Los apellidos son obligatorios.").show();
            isValid = false;
        }

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


        if ($("#direccion").val().trim() === "") {
            $("#direccion").addClass("is-invalid");
            $("#direccion").next(".error-message").text("La dirección es obligatoria.").show();
            isValid = false;
        }


        const telefono = $("#telefono").val().trim();
        if (telefono === "") {
            $("#telefono").addClass("is-invalid");
            $("#telefono").next(".error-message").text("El teléfono es obligatorio.").show();
            isValid = false;
        } else {

            const telefonoPattern = /^\d{8,}$/;
            if (!telefonoPattern.test(telefono)) {
                $("#telefono").addClass("is-invalid");
                $("#telefono").next(".error-message").text("Ingresa un teléfono válido (mínimo 8 dígitos).").show();
                isValid = false;
            }
        }

        if ($("#rol").val() === "") {
            $("#rol").addClass("is-invalid");
            $("#rol").next(".error-message").text("Selecciona un tipo de usuario.").show();
            isValid = false;
        }


        if (isValid) {
            alert("¡Usuario registrado correctamente!");
            $("#registroForm")[0].reset();

            $(".error-message").hide();
            $(".form-control, .form-select").removeClass("is-invalid");
        }
    });
});