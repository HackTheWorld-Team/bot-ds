document.addEventListener('DOMContentLoaded', () => {
    const eventsGrid = document.getElementById('eventsGrid');
    const noEvents = eventsGrid.querySelector('.no-events');

    fetch('/api/eventos')
        .then(response => response.json())
        .then(events => {
            if (events.length === 0) {
                noEvents.style.display = 'block';
                return;
            }

            noEvents.style.display = 'none';
            eventsGrid.innerHTML = '';

            events.forEach(event => {
                const card = document.createElement('div');
                card.className = 'event-card';
                
                const statusClass = `status-${event.status.replace('-', '').toLowerCase() || 'scheduled'}`;
                
                card.innerHTML = `
                    <div class="event-header">
                        <span class="event-name">${event.name || 'Sin nombre'}</span>
                        <span class="event-status ${statusClass}">${event.status || 'Programado'}</span>
                    </div>
                    <div class="event-meta">
                        <span class="meta-item">
                            <span class="time-badge">${new Date(event.start_time).toLocaleDateString('es-ES')}</span>
                        </span>
                        <span class="meta-item">
                            <span class="organizer">Organizador: #${event.organizer_id || 'N/A'}</span>
                        </span>
                    </div>
                `;
                
                eventsGrid.appendChild(card);
            });
        })
        .catch(err => {
            console.error('Error cargando eventos:', err);
            noEvents.textContent = 'Error al cargar eventos';
            noEvents.style.color = 'var(--error)';
        });
});