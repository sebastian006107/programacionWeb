$(document).ready(function() {
    const API_KEY = '646d5d8f63a44be69214f55e42654973';
    
    function cargarJuegosPlayStation() {
        $('#juegos-playstation').html('<div class="col-12 text-center"><div class="spinner-border" role="status"><span class="visually-hidden">Cargando...</span></div></div>');
        
        const url = `https://api.rawg.io/api/games?key=${API_KEY}&platforms=18,187,16&page_size=30&ordering=-added&metacritic=80,100`;
        
        $.ajax({
            url: url,
            method: 'GET',
            success: function(data) {
                mostrarJuegos(data.results);
            },
            error: function(error) {
                console.error('Error al cargar juegos:', error);
                $('#juegos-playstation').html('<div class="col-12 text-center text-danger">Error al cargar los juegos. Por favor, intenta más tarde.</div>');
            }
        });
    }
    
    function mostrarJuegos(juegos) {
        let html = '';
        
        juegos.forEach(function(juego) {
            let generos = '';
            if (juego.genres && juego.genres.length > 0) {
                generos = juego.genres.slice(0, 2).map(g => g.name).join(', ');
            }
            
            let fecha = juego.released ? new Date(juego.released).getFullYear() : 'TBA';
            
            let metacritic = juego.metacritic ? 
                `<span class="badge bg-success">${juego.metacritic}</span>` : '';
            
            html += `
                <div class="col-12 col-md-6 col-lg-4 mb-4">
                    <div class="card h-100 game-card" data-game-id="${juego.id}">
                        <div class="position-relative">
                            <img src="${juego.background_image}" class="card-img-top" alt="${juego.name}">
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
        
        $('#juegos-playstation').html(html);
        
        $('.game-card').on('click', function() {
            const gameId = $(this).data('game-id');
            window.location.href = `/juegos/${gameId}/`;
        });
    }
    
    cargarJuegosPlayStation();
});