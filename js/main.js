// Google Fonts Dashboard - Main Script

document.addEventListener('DOMContentLoaded', () => {
    loadMessageLog();
});

async function loadMessageLog() {
    const container = document.getElementById('messages');

    try {
        const response = await fetch('data/message_log.json');
        const messages = await response.json();

        container.innerHTML = messages.map(entry => `
            <div class="message-entry">
                <span class="timestamp">${formatTimestamp(entry.timestamp)}</span>
                <p class="message-text">${escapeHtml(entry.message)}</p>
            </div>
        `).join('');
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load message log.</p>';
    }
}

function formatTimestamp(isoString) {
    const date = new Date(isoString);
    return date.toLocaleString();
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
