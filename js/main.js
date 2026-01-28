// Google Fonts Dashboard - Main Script

document.addEventListener('DOMContentLoaded', () => {
    loadFontsAudit();
    loadMessageLog();
});

async function loadFontsAudit() {
    const container = document.getElementById('fonts-table');

    try {
        const response = await fetch('data/fonts.json');
        const fonts = await response.json();

        const table = document.createElement('table');
        table.innerHTML = `
            <thead>
                <tr>
                    <th>Font Family</th>
                    <th>Repository</th>
                    <th>Commit</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                ${fonts.map(font => `
                    <tr class="status-${font.status}">
                        <td class="font-name">
                            <a href="font-report.html?font=${encodeURIComponent(font.slug || font.name.toLowerCase().replace(/\s+/g, '-'))}">${escapeHtml(font.name)}</a>
                        </td>
                        <td class="repo-url">
                            <a href="${escapeHtml(font.repository_url)}" target="_blank">
                                ${escapeHtml(font.repository_url.replace('https://github.com/', ''))}
                            </a>
                        </td>
                        <td class="commit-hash">
                            <a href="${escapeHtml(font.repository_url)}/commit/${escapeHtml(font.commit)}" target="_blank">
                                ${escapeHtml(font.commit.substring(0, 7))}
                            </a>
                        </td>
                        <td class="status">
                            <span class="status-badge ${font.status}">${escapeHtml(font.status)}</span>
                        </td>
                    </tr>
                `).join('')}
            </tbody>
        `;
        container.appendChild(table);
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load fonts data.</p>';
    }
}

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
