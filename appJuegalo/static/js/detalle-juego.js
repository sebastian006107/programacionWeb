$(document).ready(function() {
    const API_KEY = '646d5d8f63a44be69214f55e42654973';
    
    function cargarDetalleJuego() {
        const url = `https://api.rawg.io/api/games/${GAME_ID}?key=${API_KEY}`;
        
        $.ajax({
            url: url,
            method: 'GET',
            success: function(juego) {
                mostrarCarrusel(juego);
                mostrarInfo(juego);
                mostrarDescripcion(juego);
            },
            error: function(error) {
                console.error('Error al cargar el juego:', error);
                $('#info-juego').html('<p class="text-danger">Error al cargar la información del juego.</p>');
            }
        });
    }
    
    function mostrarCarrusel(juego) {
        let html = '';
        
        if (juego.background_image) {
            html += `
                <div class="carousel-item active">
                    <img src="${juego.background_image}" class="d-block w-100" alt="${juego.name}">
                </div>
            `;
        }
        
        if (juego.background_image_additional) {
            html += `
                <div class="carousel-item">
                    <img src="${juego.background_image_additional}" class="d-block w-100" alt="${juego.name}">
                </div>
            `;
        }
        
        $('#carousel-imagenes').html(html);
    }
    
    function mostrarInfo(juego) {
        let generos = juego.genres ? juego.genres.map(g => g.name).join(', ') : 'N/A';
        let plataformas = juego.platforms ? juego.platforms.slice(0, 5).map(p => p.platform.name).join(', ') : 'N/A';
        let fecha = juego.released || 'Fecha no disponible';
        let metacritic = juego.metacritic || 'N/A';
        
        let html = `
            <h1 class="mb-3">${juego.name}</h1>
            
            <div class="mb-3">
                <strong>Calificación:</strong>
                <span class="text-warning">
                    ${'⭐'.repeat(Math.round(juego.rating))} ${juego.rating.toFixed(1)}
                </span>
            </div>
            
            <div class="mb-3">
                <strong>Metacritic:</strong>
                <span class="badge bg-success">${metacritic}</span>
            </div>
            
            <div class="mb-3">
                <strong>Fecha de Lanzamiento:</strong> ${fecha}
            </div>
            
            <div class="mb-3">
                <strong>Géneros:</strong><br>
                ${juego.genres ? juego.genres.map(g => `<span class="info-badge">${g.name}</span>`).join('') : 'N/A'}
            </div>
            
            <div class="mb-3">
                <strong>Plataformas:</strong><br>
                ${juego.platforms ? juego.platforms.slice(0, 5).map(p => `<span class="info-badge">${p.platform.name}</span>`).join('') : 'N/A'}
            </div>
            
            <a href="${juego.website || '#'}" target="_blank" class="btn btn-primary w-100 mt-3" ${!juego.website ? 'disabled' : ''}>
                Sitio Web Oficial
            </a>
        `;
        
        $('#info-juego').html(html);
    }
    
    function mostrarDescripcion(juego) {
        let descripcion = juego.description_raw || juego.description || 'No hay descripción disponible.';
        $('#descripcion-juego').html(`<p>${descripcion}</p>`);
    }
    
    cargarDetalleJuego();
});