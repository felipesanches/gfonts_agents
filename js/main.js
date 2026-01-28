// Google Fonts Dashboard - Main Script

let questionsData = null;

document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    loadFontsAudit();
    loadPendingQuestions();
    loadMessageLog();
});

function initTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.dataset.tab;

            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            btn.classList.add('active');
            document.getElementById(`tab-${tabId}`).classList.add('active');
        });
    });
}

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
                            <span class="status-badge ${font.status}">${escapeHtml(font.status.replace('_', ' '))}</span>
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

async function loadPendingQuestions() {
    const container = document.getElementById('questions-list');
    const filterSelect = document.getElementById('person-filter');

    try {
        const response = await fetch('data/pending_questions.json');
        questionsData = await response.json();

        // Populate filter dropdown
        questionsData.questions_by_person.forEach(person => {
            const option = document.createElement('option');
            option.value = person.id;
            option.textContent = `${person.name} (${person.questions.length})`;
            filterSelect.appendChild(option);
        });

        // Add filter event listener
        filterSelect.addEventListener('change', () => {
            filterQuestions(filterSelect.value);
        });

        // Render questions
        renderQuestions(container, questionsData);
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load pending questions.</p>';
    }
}

function renderQuestions(container, data) {
    if (data.questions_by_person.length === 0) {
        container.innerHTML = '<p class="no-questions">No pending questions at this time.</p>';
        return;
    }

    let html = '';
    data.questions_by_person.forEach(person => {
        person.questions.forEach(q => {
            html += `
                <div class="question-card" data-person="${person.id}">
                    <div class="question-header">
                        <div>
                            <div class="question-person">${escapeHtml(person.name)}</div>
                            <div class="question-role">${escapeHtml(person.role.replace('_', ' '))}</div>
                        </div>
                        <span class="question-font">${escapeHtml(q.font)}</span>
                    </div>
                    <div class="question-text">${escapeHtml(q.question)}</div>
                    ${q.context ? `
                        <div class="question-context">
                            <div class="question-context-label">Context:</div>
                            ${escapeHtml(q.context)}
                        </div>
                    ` : ''}
                </div>
            `;
        });
    });

    container.innerHTML = html;
}

function filterQuestions(personId) {
    const cards = document.querySelectorAll('.question-card');
    cards.forEach(card => {
        if (personId === 'all' || card.dataset.person === personId) {
            card.classList.remove('hidden');
        } else {
            card.classList.add('hidden');
        }
    });
}

async function loadMessageLog() {
    const container = document.getElementById('messages');

    try {
        const response = await fetch('data/message_log.json');
        const messages = await response.json();

        // Group messages by day
        const messagesByDay = {};
        messages.forEach(entry => {
            const date = new Date(entry.timestamp);
            const dayKey = date.toISOString().split('T')[0];
            if (!messagesByDay[dayKey]) {
                messagesByDay[dayKey] = [];
            }
            messagesByDay[dayKey].push(entry);
        });

        // Generate HTML for each day
        const days = Object.keys(messagesByDay).sort().reverse();
        container.innerHTML = days.map(day => {
            const dayMessages = messagesByDay[day];
            const summary = generateDaySummary(dayMessages);
            const formattedDate = new Date(day + 'T00:00:00').toLocaleDateString('en-US', {
                weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
            });

            return `
                <div class="day-group">
                    <div class="day-header" onclick="toggleDay(this)">
                        <span class="day-date">${formattedDate}</span>
                        <span class="day-count">${dayMessages.length} messages</span>
                        <span class="day-toggle">▼</span>
                    </div>
                    <div class="day-summary">${escapeHtml(summary)}</div>
                    <div class="day-messages collapsed">
                        ${dayMessages.map(entry => `
                            <div class="message-entry">
                                <span class="timestamp">${formatTimestamp(entry.timestamp)}</span>
                                <p class="message-text">${escapeHtml(entry.message)}</p>
                                ${entry.translation ? `<p class="message-translation">${escapeHtml(entry.translation)}</p>` : ''}
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }).join('');
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load message log.</p>';
    }
}

function generateDaySummary(messages) {
    const topics = [];
    messages.forEach(msg => {
        const text = msg.message.toLowerCase();
        if (text.includes('repository') || text.includes('repo')) topics.push('repository setup');
        if (text.includes('investigate') || text.includes('audit')) topics.push('font investigation');
        if (text.includes('dashboard') || text.includes('panel')) topics.push('dashboard development');
        if (text.includes('commit') || text.includes('metadata')) topics.push('metadata validation');
        if (text.includes('config.yaml') || text.includes('gftools')) topics.push('build configuration');
    });
    const uniqueTopics = [...new Set(topics)];
    if (uniqueTopics.length === 0) return 'General discussion and setup';
    return 'Topics: ' + uniqueTopics.slice(0, 3).join(', ');
}

function toggleDay(header) {
    const dayGroup = header.parentElement;
    const messages = dayGroup.querySelector('.day-messages');
    const toggle = header.querySelector('.day-toggle');

    if (messages.classList.contains('collapsed')) {
        messages.classList.remove('collapsed');
        toggle.textContent = '▲';
    } else {
        messages.classList.add('collapsed');
        toggle.textContent = '▼';
    }
}

function formatTimestamp(isoString) {
    const date = new Date(isoString);
    return date.toLocaleString();
}

function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
