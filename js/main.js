// Google Fonts Dashboard - Main Script

let questionsData = null;

document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    loadFontsAudit();
    loadDesigners();
    loadPendingPRs();
    loadPendingQuestions();
    loadMessageLog();
    loadFridayStatus();
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
                            ${font.commit ? `
                                <a href="${escapeHtml(font.repository_url)}/commit/${escapeHtml(font.commit)}" target="_blank">
                                    ${escapeHtml(font.commit.substring(0, 7))}
                                </a>
                            ` : '<span class="missing">missing</span>'}
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

let designersData = null;

async function loadDesigners() {
    const container = document.getElementById('designers-grid');
    const searchInput = document.getElementById('designer-search');
    const countSpan = document.getElementById('designer-count');

    try {
        const response = await fetch('data/designers.json');
        designersData = await response.json();

        countSpan.textContent = `${designersData.length} designers`;

        // Add search event listener
        searchInput.addEventListener('input', () => {
            filterDesigners(searchInput.value);
        });

        renderDesigners(container, designersData);
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load designers data.</p>';
    }
}

function renderDesigners(container, designers) {
    container.innerHTML = designers.map(designer => `
        <div class="designer-card" data-name="${escapeHtml(designer.name.toLowerCase())}">
            <div class="designer-avatar">
                ${designer.avatar_url
                    ? `<img src="${escapeHtml(designer.avatar_url)}" alt="${escapeHtml(designer.name)}" loading="lazy" />`
                    : `<div class="avatar-placeholder">${escapeHtml(designer.name.charAt(0))}</div>`
                }
            </div>
            <div class="designer-info">
                <h3 class="designer-name">${escapeHtml(designer.name)}</h3>
                ${designer.bio
                    ? `<div class="designer-bio">${designer.bio}</div>`
                    : '<div class="designer-bio no-bio">No bio available</div>'
                }
                ${designer.link
                    ? `<a class="designer-link" href="${escapeHtml(designer.link)}" target="_blank">Website</a>`
                    : ''
                }
            </div>
        </div>
    `).join('');
}

function filterDesigners(searchTerm) {
    const cards = document.querySelectorAll('.designer-card');
    const term = searchTerm.toLowerCase();
    let visibleCount = 0;

    cards.forEach(card => {
        if (card.dataset.name.includes(term)) {
            card.classList.remove('hidden');
            visibleCount++;
        } else {
            card.classList.add('hidden');
        }
    });

    document.getElementById('designer-count').textContent =
        `${visibleCount} of ${designersData.length} designers`;
}

async function loadPendingPRs() {
    const container = document.getElementById('prs-list');

    try {
        const response = await fetch('data/pending_prs.json');
        const prs = await response.json();

        if (prs.length === 0) {
            container.innerHTML = '<p class="no-prs">No pending PRs at this time.</p>';
            return;
        }

        container.innerHTML = prs.map(pr => `
            <div class="pr-card priority-${pr.priority}">
                <div class="pr-header">
                    <div class="pr-title">${escapeHtml(pr.title)}</div>
                    <div class="pr-badges">
                        <span class="pr-type">${escapeHtml(pr.type.replace('_', ' '))}</span>
                        <span class="pr-priority priority-${pr.priority}">${escapeHtml(pr.priority)}</span>
                        <span class="pr-status status-${pr.status}">${escapeHtml(pr.status.replace('_', ' '))}</span>
                    </div>
                </div>
                ${pr.font ? `<div class="pr-font">Font: ${escapeHtml(pr.font)}</div>` : ''}
                ${pr.designers_count ? `<div class="pr-font">Designers: ${pr.designers_count}</div>` : ''}
                <div class="pr-description">${escapeHtml(pr.description)}</div>
                <div class="pr-files">
                    <strong>Files to modify:</strong> ${pr.files_to_modify.length} files
                    <details>
                        <summary>Show files</summary>
                        <ul>
                            ${pr.files_to_modify.slice(0, 20).map(f => `<li><code>${escapeHtml(f)}</code></li>`).join('')}
                            ${pr.files_to_modify.length > 20 ? `<li><em>... and ${pr.files_to_modify.length - 20} more</em></li>` : ''}
                        </ul>
                    </details>
                </div>
                ${pr.changes.add_commit ? `
                    <div class="pr-changes">
                        <strong>Add commit:</strong> <code>${escapeHtml(pr.changes.add_commit)}</code>
                    </div>
                ` : ''}
                ${pr.changes.options ? `
                    <div class="pr-changes">
                        <strong>Options:</strong>
                        <ul>
                            ${pr.changes.options.map(o => `<li>${escapeHtml(o)}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}
                ${pr.type === 'designer_metadata' ? renderDesignerChanges(pr.changes) : ''}
                ${pr.notes ? `<div class="pr-notes"><em>Note: ${escapeHtml(pr.notes)}</em></div>` : ''}
            </div>
        `).join('');
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load pending PRs.</p>';
    }
}

function renderDesignerChanges(changes) {
    // changes is an object with designer IDs as keys
    const designers = Object.entries(changes);
    if (designers.length === 0) return '';

    const designerList = designers.slice(0, 10).map(([id, data]) => {
        const fonts = data.notable_fonts && data.notable_fonts.length > 0
            ? ` - ${data.notable_fonts.slice(0, 3).join(', ')}`
            : '';
        return `<li><strong>${escapeHtml(data.name)}</strong>${fonts}</li>`;
    }).join('');

    const moreCount = designers.length > 10 ? designers.length - 10 : 0;

    return `
        <div class="pr-changes">
            <strong>Designer bios to add:</strong>
            <details>
                <summary>Show ${designers.length} designers</summary>
                <ul>
                    ${designerList}
                    ${moreCount > 0 ? `<li><em>... and ${moreCount} more</em></li>` : ''}
                </ul>
            </details>
        </div>
    `;
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
                            <div class="message-entry ${entry.role || 'user'}">
                                <span class="message-role">${entry.role === 'assistant' ? 'Claude' : 'User'}</span>
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

// Friday Status functionality
async function loadFridayStatus() {
    const weekSpan = document.getElementById('status-week');
    const downloadBtn = document.getElementById('download-odp');
    const doneList = document.getElementById('status-done');
    const plannedList = document.getElementById('status-planned');
    const questionsList = document.getElementById('status-questions');

    // Get the status week window (Friday 2pm GMT-3 to following Friday 1pm GMT-3)
    const { windowStart, windowEnd, friday } = getStatusWeekWindow();
    weekSpan.textContent = `Week of ${friday.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}`;

    try {
        const response = await fetch('data/message_log.json');
        const messages = await response.json();

        // Get messages within the status week window
        const weekMessages = messages.filter(m => {
            const msgDate = new Date(m.timestamp);
            return msgDate >= windowStart && msgDate <= windowEnd;
        });

        // Extract status items from messages
        const statusData = extractStatusFromMessages(weekMessages);

        // Populate the lists
        renderStatusList(doneList, statusData.done, 'No items recorded yet');
        renderStatusList(plannedList, statusData.planned, 'No items planned yet');
        renderStatusList(questionsList, statusData.questions, 'No questions pending');

        // Set up download button
        downloadBtn.addEventListener('click', () => {
            downloadODP(statusData, friday);
        });
    } catch (error) {
        doneList.innerHTML = '<li class="empty-list">Failed to load status data</li>';
        plannedList.innerHTML = '<li class="empty-list">Failed to load status data</li>';
        questionsList.innerHTML = '<li class="empty-list">Failed to load status data</li>';
    }
}

function getStatusWeekWindow() {
    // Status week: Friday 2pm GMT-3 to following Friday 1pm GMT-3
    // GMT-3 offset in minutes: -180 (or +180 to convert to UTC)
    const GMT_MINUS_3_OFFSET = 180; // minutes to add to get UTC

    const now = new Date();

    // Find the upcoming Friday (or today if it's Friday before 1pm GMT-3)
    const friday = new Date(now);
    const day = friday.getDay();

    // Calculate days until Friday (0 = Sunday, 5 = Friday)
    let daysUntilFriday = (5 - day + 7) % 7;
    if (daysUntilFriday === 0) {
        // It's Friday - check if we're past 1pm GMT-3
        const nowInGMT3 = new Date(now.getTime() + (now.getTimezoneOffset() - GMT_MINUS_3_OFFSET) * 60000);
        if (nowInGMT3.getHours() >= 13) {
            // Past 1pm GMT-3 on Friday, move to next Friday
            daysUntilFriday = 7;
        }
    }
    friday.setDate(friday.getDate() + daysUntilFriday);
    friday.setHours(0, 0, 0, 0);

    // Window end: This Friday at 1pm GMT-3 (16:00 UTC)
    const windowEnd = new Date(friday);
    windowEnd.setUTCHours(16, 0, 0, 0); // 1pm GMT-3 = 16:00 UTC

    // Window start: Previous Friday at 2pm GMT-3 (17:00 UTC)
    const windowStart = new Date(friday);
    windowStart.setDate(windowStart.getDate() - 7);
    windowStart.setUTCHours(17, 0, 0, 0); // 2pm GMT-3 = 17:00 UTC

    return { windowStart, windowEnd, friday };
}

function extractStatusFromMessages(messages) {
    const done = [];
    const planned = [];
    const questions = [];

    // Analyze assistant messages for accomplishments
    messages.forEach(msg => {
        if (msg.role === 'assistant') {
            const text = msg.message.toLowerCase();

            // Detect completed work
            if (text.includes('created pr') || text.includes('submitted pr')) {
                const prMatch = msg.message.match(/PR #(\d+)/i);
                if (prMatch) {
                    done.push(`Created PR #${prMatch[1]} for google/fonts`);
                }
            }
            if (text.includes('added') && text.includes('designer')) {
                const countMatch = msg.message.match(/(\d+)\s+designer/i);
                if (countMatch) {
                    done.push(`Researched and added ${countMatch[1]} designer biographies`);
                }
            }
            if (text.includes('enrichment') || text.includes('bio.html')) {
                if (!done.some(d => d.includes('designer bio'))) {
                    done.push('Enriched designer metadata catalog');
                }
            }
            if (text.includes('implemented') || text.includes('added') && text.includes('tab')) {
                const feature = msg.message.match(/added\s+(?:the\s+)?["']?([^"'\n]+)["']?\s+tab/i);
                if (feature) {
                    done.push(`Implemented ${feature[1]} feature`);
                }
            }
        }
    });

    // Remove duplicates
    const uniqueDone = [...new Set(done)];

    // Default planned items if nothing specific found
    if (planned.length === 0) {
        planned.push('Continue designer catalog enrichment');
        planned.push('Repository audit and validation');
    }

    return {
        done: uniqueDone.slice(0, 5),
        planned: planned.slice(0, 3),
        questions: questions.slice(0, 3)
    };
}

function renderStatusList(ul, items, emptyMessage) {
    if (items.length === 0) {
        ul.innerHTML = `<li class="empty-list">${emptyMessage}</li>`;
    } else {
        ul.innerHTML = items.map(item => `<li>${escapeHtml(item)}</li>`).join('');
    }
}

function downloadODP(statusData, friday) {
    const dateStr = friday.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });

    // ODP is a ZIP file containing XML files
    // We'll create a minimal ODP structure
    const content = generateODPContent(statusData, dateStr);

    // Create and download the file
    const blob = new Blob([content], { type: 'application/vnd.oasis.opendocument.presentation' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `status-${friday.toISOString().split('T')[0]}.fodp`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function generateODPContent(statusData, dateStr) {
    // Generate Flat ODP (FODP) which is a single XML file
    const doneItems = statusData.done.length > 0
        ? statusData.done.map(item => `<text:list-item><text:p text:style-name="P2">${escapeXml(item)}</text:p></text:list-item>`).join('\n')
        : '<text:list-item><text:p text:style-name="P2">(No items recorded)</text:p></text:list-item>';

    const plannedItems = statusData.planned.length > 0
        ? statusData.planned.map(item => `<text:list-item><text:p text:style-name="P2">${escapeXml(item)}</text:p></text:list-item>`).join('\n')
        : '<text:list-item><text:p text:style-name="P2">(No items planned)</text:p></text:list-item>';

    const questionItems = statusData.questions.length > 0
        ? statusData.questions.map(item => `<text:list-item><text:p text:style-name="P2">${escapeXml(item)}</text:p></text:list-item>`).join('\n')
        : '<text:list-item><text:p text:style-name="P2">(No questions pending)</text:p></text:list-item>';

    return `<?xml version="1.0" encoding="UTF-8"?>
<office:document xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
    xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
    xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"
    xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0"
    xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0"
    xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"
    xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"
    office:version="1.3" office:mimetype="application/vnd.oasis.opendocument.presentation">
  <office:styles>
    <style:style style:name="dp1" style:family="drawing-page">
      <style:drawing-page-properties draw:fill="solid" draw:fill-color="#1a73e8"/>
    </style:style>
  </office:styles>
  <office:automatic-styles>
    <style:style style:name="P1" style:family="paragraph">
      <style:paragraph-properties fo:text-align="center"/>
      <style:text-properties fo:font-size="32pt" fo:font-weight="bold" fo:color="#ffffff"/>
    </style:style>
    <style:style style:name="P2" style:family="paragraph">
      <style:text-properties fo:font-size="18pt" fo:color="#ffffff"/>
    </style:style>
    <style:style style:name="P3" style:family="paragraph">
      <style:text-properties fo:font-size="20pt" fo:font-weight="bold" fo:color="#ffffff"/>
    </style:style>
    <style:style style:name="gr1" style:family="graphic">
      <style:graphic-properties draw:stroke="none" draw:fill="none"/>
    </style:style>
  </office:automatic-styles>
  <office:body>
    <office:presentation>
      <draw:page draw:name="Status" draw:style-name="dp1" presentation:presentation-page-layout-name="AL1T0">
        <draw:frame draw:style-name="gr1" draw:layer="layout" svg:width="25cm" svg:height="3cm" svg:x="0.5cm" svg:y="0.5cm">
          <draw:text-box>
            <text:p text:style-name="P1">Felipe Sanches - Weekly Status</text:p>
            <text:p text:style-name="P2">${escapeXml(dateStr)}</text:p>
          </draw:text-box>
        </draw:frame>
        <draw:frame draw:style-name="gr1" draw:layer="layout" svg:width="24cm" svg:height="4cm" svg:x="0.5cm" svg:y="4cm">
          <draw:text-box>
            <text:p text:style-name="P3">What was done this week</text:p>
            <text:list>
              ${doneItems}
            </text:list>
          </draw:text-box>
        </draw:frame>
        <draw:frame draw:style-name="gr1" draw:layer="layout" svg:width="24cm" svg:height="3cm" svg:x="0.5cm" svg:y="9cm">
          <draw:text-box>
            <text:p text:style-name="P3">Planned for next week</text:p>
            <text:list>
              ${plannedItems}
            </text:list>
          </draw:text-box>
        </draw:frame>
        <draw:frame draw:style-name="gr1" draw:layer="layout" svg:width="24cm" svg:height="3cm" svg:x="0.5cm" svg:y="13cm">
          <draw:text-box>
            <text:p text:style-name="P3">Questions for the team</text:p>
            <text:list>
              ${questionItems}
            </text:list>
          </draw:text-box>
        </draw:frame>
      </draw:page>
    </office:presentation>
  </office:body>
</office:document>`;
}

function escapeXml(text) {
    if (!text) return '';
    return text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&apos;');
}
