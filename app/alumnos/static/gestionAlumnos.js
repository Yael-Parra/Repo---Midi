document.addEventListener('DOMContentLoaded', function() {

    const btnsEliminacion = document.querySelectorAll('.btnEliminacion');
    
    btnsEliminacion.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.getAttribute('href');

            if (confirm('¿Estás seguro de que deseas eliminar este alumno? Esta acción no se puede deshacer.')) {
                window.location.href = url;
            }
        });
    });
});