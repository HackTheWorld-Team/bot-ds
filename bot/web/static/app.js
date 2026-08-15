const CALENDAR_ICON = `
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="2" stroke-linecap="round"
         stroke-linejoin="round" aria-hidden="true">
        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
        <line x1="16" y1="2" x2="16" y2="6"></line>
        <line x1="8" y1="2" x2="8" y2="6"></line>
        <line x1="3" y1="10" x2="21" y2="10"></line>
    </svg>`;

const STATUS_LABELS = {
    scheduled: "Programado",
    active: "En curso",
    completed: "Finalizado",
    held: "Realizado",
    ended: "Terminado",
    cancelled: "Cancelado",
};

const dateFormat = new Intl.DateTimeFormat("es", {
    dateStyle: "medium",
    timeStyle: "short",
});

function createMeta(label, value) {
    const row = document.createElement("span");
    const labelSpan = document.createElement("span");
    labelSpan.textContent = label;
    row.appendChild(labelSpan);
    row.appendChild(document.createTextNode(value));
    return row;
}

function buildCard(event) {
    const card = document.createElement("article");
    card.className = "card";
    card.setAttribute("role", "listitem");
    card.setAttribute("aria-label", `Evento ${event.name}`);

    const header = document.createElement("header");
    header.className = "card-header";

    const icon = document.createElement("span");
    icon.className = "card-icon";
    icon.innerHTML = CALENDAR_ICON;

    const title = document.createElement("h2");
    title.className = "card-title";
    title.textContent = "Eventos";

    header.append(icon, title);

    const body = document.createElement("div");
    body.className = "card-body";

    const name = document.createElement("h3");
    name.className = "event-name";
    name.textContent = event.name;

    const badge = document.createElement("span");
    const statusKey = event.status || "scheduled";
    const badgeClass = `badge badge--${statusKey}`;
    badge.className = badgeClass;
    badge.textContent = STATUS_LABELS[statusKey] || statusKey;

    const meta = document.createElement("div");
    meta.className = "event-meta";

    const start = new Date(event.start_time);
    const end = new Date(event.end_time);
    const when = createMeta("Cuándo", dateFormat.format(start));
    const duration = createMeta(
        "Duración",
        end > start ? `${Math.round((end - start) / 60000)} min` : "—"
    );
    const organizer = createMeta(
        "Organizador",
        event.organizer_id ? `ID ${event.organizer_id}` : "Desconocido"
    );

    meta.append(when, duration, organizer);

    if (event.description) {
        const description = document.createElement("p");
        description.className = "event-description";
        description.textContent = event.description;
        body.appendChild(description);
    }

    body.append(name, badge, meta);
    card.append(header, body);

    return card;
}

async function loadEvents() {
    const grid = document.getElementById("cards");

    try {
        const response = await fetch("/api/eventos");
        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const events = await response.json();
        grid.innerHTML = "";

        if (!events.length) {
            const empty = document.createElement("p");
            empty.className = "empty";
            empty.textContent = "No hay eventos registrados todavía.";
            grid.appendChild(empty);
            return;
        }

        const fragment = document.createDocumentFragment();
        for (const event of events) {
            fragment.appendChild(buildCard(event));
        }
        grid.appendChild(fragment);
    } catch (error) {
        grid.innerHTML = "";

        const empty = document.createElement("p");
        empty.className = "empty";
        empty.textContent = "No se pudieron cargar los eventos.";
        grid.appendChild(empty);
    }
}

document.addEventListener("DOMContentLoaded", loadEvents);