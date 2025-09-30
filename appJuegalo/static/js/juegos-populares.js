$(document).ready(function() {
    // Configuración de la API
    const API_KEY = '646d5d8f63a44be69214f55e42654973';
    
    // Función para cargar juegos AAA más populares
    function cargarJuegosPopulares() {
        // URL para obtener los juegos más populares de todos los tiempos
        // page_size=12 para tener más variedad
        // ordering=-added para obtener los juegos más populares (más agregados a bibliotecas)
        const url = `https://api.rawg.io/api/games?key=${API_KEY}&page_size=12&ordering=-added&metacritic=85,100`;
        
        // Mostrar mensaje de carga
        $('#juegos-populares').html('<div class="col-12 text-center"><div class="spinner-border" role="status"><span class="visually-hidden">Cargando...</span></div></div>');
        
        // Llamada AJAX
        $.ajax({
            url: url,
            method: 'GET',
            success: function(data) {
                mostrarJuegos(data.results);
            },
            error: function(error) {
                console.error('Error al cargar juegos:', error);
                $('#juegos-populares').html('<div class="col-12 text-center text-danger">Error al cargar los juegos. Por favor, intenta más tarde.</div>');
            }
        });
    }
    
    // Función para mostrar los juegos en cards mejoradas
    function mostrarJuegos(juegos) {
        let html = '';
        
        // Recorrer cada juego y crear una card
        juegos.forEach(function(juego) {
            // Obtener géneros
            let generos = '';
            if (juego.genres && juego.genres.length > 0) {
                generos = juego.genres.slice(0, 2).map(g => g.name).join(', ');
            }
            
            // Obtener fecha de lanzamiento
            let fecha = juego.released ? new Date(juego.released).getFullYear() : 'TBA';
            
            // Obtener metacritic score si existe
            let metacritic = juego.metacritic ? 
                `<span class="badge bg-success">${juego.metacritic}</span>` : '';
            
            // Crear la card HTML con mejor diseño
            html += `
                <div class="col-12 col-md-6 col-lg-4 col-xl-3 mb-4">
                    <div class="card h-100 game-card" data-game-id="${juego.id}" style="cursor: pointer;">
                        <div class="position-relative">
                            <img src="${juego.background_image}" class="card-img-top" alt="${juego.name}" 
                                 style="height: 180px; object-fit: cover;">
                            <div class="position-absolute top-0 end-0 p-2">
                                ${metacritic}
                            </div>
                        </div>
                        <div class="card-body d-flex flex-column">
                            <h6 class="card-title fw-bold">${juego.name}</h6>
                            <p class="text-muted small mb-2">${generos} • ${fecha}</p>
                            <div class="mb-2">
                                <small class="text-warning">
                                    ${'⭐'.repeat(Math.round(juego.rating))} ${juego.rating.toFixed(1)}
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        });
        
        // Insertar las cards en el contenedor
        $('#juegos-populares').html(html);
        
        // Agregar evento de click para redirección
        $('.game-card').on('click', function() {
            const gameId = $(this).data('game-id');
            // Redireccionar a página de detalles del juego
            window.location.href = `/games/${gameId}/`;
        });
    }
    
    // Cargar los juegos cuando la página esté lista
    cargarJuegosPopulares();
});