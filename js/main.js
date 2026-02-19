// Google Fonts Dashboard - Main Script

let questionsData = null;

document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    loadLibrarySources();
    loadCacheStats();
    loadFontsAudit();
    loadDesigners();
    loadPendingPRs();
    loadPendingQuestions();
    loadMessageLog();
    loadFridayStatus();
    loadBuildApproaches();
    loadPlans();
    loadDiskUsage();
    loadBioAudit();
    loadPrebuildResearch();
});

function initTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    function activateTab(tabId) {
        const btn = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
        const content = document.getElementById(`tab-${tabId}`);
        if (!btn || !content) return;

        tabBtns.forEach(b => b.classList.remove('active'));
        tabContents.forEach(c => c.classList.remove('active'));

        btn.classList.add('active');
        content.classList.add('active');
    }

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.dataset.tab;
            history.replaceState(null, '', `#${tabId}`);
            activateTab(tabId);
        });
    });

    // Activate tab from URL fragment on load
    const hash = location.hash.slice(1);
    if (hash) {
        activateTab(hash);
    }

    // Handle back/forward navigation
    window.addEventListener('hashchange', () => {
        const tabId = location.hash.slice(1);
        if (tabId) {
            activateTab(tabId);
        }
    });
}

// Library Sources tracking
let sourcesData = null;

async function loadLibrarySources() {
    const container = document.getElementById('sources-table-container');
    const searchInput = document.getElementById('sources-search');
    const statusFilter = document.getElementById('sources-status-filter');
    const licenseFilter = document.getElementById('sources-license-filter');
    const countSpan = document.getElementById('sources-count');

    try {
        const response = await fetch('data/gfonts_library_sources.json');
        sourcesData = await response.json();

        // Update summary
        updateSourcesSummary(sourcesData.summary);

        // Update timestamp
        document.getElementById('sources-timestamp').textContent =
            new Date(sourcesData.generated_at).toLocaleString();

        // Set up filters
        searchInput.addEventListener('input', () => filterSources());
        statusFilter.addEventListener('change', () => filterSources());
        licenseFilter.addEventListener('change', () => filterSources());

        // Initial render
        renderSourcesTable(container, sourcesData.families);
        countSpan.textContent = `${sourcesData.families.length} families`;
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load library sources data. Make sure the file exists at /mnt/shared/gfonts_library_sources.json</p>';
        console.error('Error loading sources:', error);
    }
}

function updateSourcesSummary(summary) {
    document.getElementById('summary-total').textContent = summary.total;
    document.getElementById('summary-complete').textContent = summary.complete;
    document.getElementById('summary-missing-config').textContent = summary.missing_config;
    document.getElementById('summary-missing-commit').textContent = summary.missing_commit;
    document.getElementById('summary-no-source').textContent = summary.no_source;

    // Update progress bar
    const completePercent = (summary.complete / summary.total * 100).toFixed(1);
    const partialPercent = ((summary.missing_config + summary.missing_commit) / summary.total * 100).toFixed(1);

    document.getElementById('progress-complete').style.width = completePercent + '%';
    document.getElementById('progress-partial').style.width = partialPercent + '%';

    // Render status breakdown chart
    renderStatusChart(summary);

    // Load and render progress history
    loadProgressHistory();
}

function renderStatusChart(summary) {
    const canvas = document.getElementById('status-chart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Clear canvas
    ctx.clearRect(0, 0, width, height);

    const data = [
        { label: 'Complete', value: summary.complete, color: '#4caf50' },
        { label: 'Missing Config', value: summary.missing_config, color: '#ff9800' },
        { label: 'Missing Commit', value: summary.missing_commit, color: '#2196f3' },
        { label: 'No Source', value: summary.no_source, color: '#f44336' }
    ];

    const total = data.reduce((sum, d) => sum + d.value, 0);
    const barHeight = 40;
    const barGap = 20;
    const labelWidth = 120;
    const valueWidth = 60;
    const startX = labelWidth;
    const maxBarWidth = width - labelWidth - valueWidth - 20;

    data.forEach((d, i) => {
        const y = 30 + i * (barHeight + barGap);
        const barWidth = (d.value / total) * maxBarWidth;

        // Label
        ctx.fillStyle = '#e0e0e0';
        ctx.font = '14px system-ui, sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText(d.label, labelWidth - 10, y + barHeight / 2 + 5);

        // Bar
        ctx.fillStyle = d.color;
        ctx.fillRect(startX, y, barWidth, barHeight);

        // Value
        ctx.fillStyle = '#e0e0e0';
        ctx.textAlign = 'left';
        ctx.fillText(`${d.value} (${((d.value / total) * 100).toFixed(1)}%)`, startX + barWidth + 10, y + barHeight / 2 + 5);
    });
}

async function loadProgressHistory() {
    try {
        const response = await fetch('data/progress_history.json');
        const history = await response.json();
        renderProgressChart(history.entries, history.claude_code_start_date);
    } catch (error) {
        console.error('Failed to load progress history:', error);
    }
}

function renderProgressChart(entries, claudeCodeStartDate) {
    const canvas = document.getElementById('progress-chart');
    if (!canvas || entries.length === 0) return;

    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Clear canvas
    ctx.clearRect(0, 0, width, height);

    const padding = { top: 20, right: 20, bottom: 40, left: 60 };
    const chartWidth = width - padding.left - padding.right;
    const chartHeight = height - padding.top - padding.bottom;

    // Find max value for scaling
    const maxValue = Math.max(...entries.map(e => e.summary.total));

    // Draw axes
    ctx.strokeStyle = '#555';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(padding.left, padding.top);
    ctx.lineTo(padding.left, height - padding.bottom);
    ctx.lineTo(width - padding.right, height - padding.bottom);
    ctx.stroke();

    // Y-axis labels
    ctx.fillStyle = '#888';
    ctx.font = '12px system-ui, sans-serif';
    ctx.textAlign = 'right';
    for (let i = 0; i <= 4; i++) {
        const y = padding.top + (chartHeight * i / 4);
        const value = Math.round(maxValue * (1 - i / 4));
        ctx.fillText(value.toString(), padding.left - 10, y + 4);
    }

    if (entries.length === 1) {
        // Single point - show stacked bar
        const e = entries[0];
        const barWidth = 100;
        const x = padding.left + chartWidth / 2 - barWidth / 2;

        const segments = [
            { value: e.summary.complete, color: '#4caf50' },
            { value: e.summary.missing_config, color: '#ff9800' },
            { value: e.summary.missing_commit, color: '#2196f3' },
            { value: e.summary.no_source, color: '#f44336' }
        ];

        let currentY = height - padding.bottom;
        segments.forEach(seg => {
            const segHeight = (seg.value / maxValue) * chartHeight;
            ctx.fillStyle = seg.color;
            ctx.fillRect(x, currentY - segHeight, barWidth, segHeight);
            currentY -= segHeight;
        });

        // Date label
        ctx.fillStyle = '#888';
        ctx.textAlign = 'center';
        const date = new Date(e.timestamp);
        ctx.fillText(date.toLocaleDateString(), x + barWidth / 2, height - 10);
    } else {
        // Multiple points - draw lines
        const xStep = chartWidth / (entries.length - 1);

        const series = [
            { key: 'complete', color: '#4caf50' },
            { key: 'missing_config', color: '#ff9800' },
            { key: 'missing_commit', color: '#2196f3' },
            { key: 'no_source', color: '#f44336' }
        ];

        series.forEach(s => {
            ctx.strokeStyle = s.color;
            ctx.lineWidth = 2;
            ctx.beginPath();
            entries.forEach((e, i) => {
                const x = padding.left + i * xStep;
                const y = height - padding.bottom - (e.summary[s.key] / maxValue) * chartHeight;
                if (i === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            });
            ctx.stroke();
        });

        // X-axis date labels (first and last)
        ctx.fillStyle = '#888';
        ctx.textAlign = 'center';
        const firstDate = new Date(entries[0].timestamp);
        const lastDate = new Date(entries[entries.length - 1].timestamp);
        ctx.fillText(firstDate.toLocaleDateString(), padding.left, height - 10);
        ctx.fillText(lastDate.toLocaleDateString(), width - padding.right, height - 10);

        // Draw Claude Code start marker
        if (claudeCodeStartDate) {
            const startDate = new Date(claudeCodeStartDate);
            // Find the index where Claude Code started
            let markerIndex = -1;
            for (let i = 0; i < entries.length; i++) {
                const entryDate = new Date(entries[i].timestamp).toDateString();
                if (entryDate === startDate.toDateString() ||
                    (entries[i].source && entries[i].source.includes('claude'))) {
                    markerIndex = i;
                    break;
                }
            }

            if (markerIndex >= 0) {
                const markerX = padding.left + markerIndex * xStep;

                // Draw vertical dashed line
                ctx.strokeStyle = '#9c27b0';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(markerX, padding.top);
                ctx.lineTo(markerX, height - padding.bottom);
                ctx.stroke();
                ctx.setLineDash([]);

                // Draw label
                ctx.fillStyle = '#9c27b0';
                ctx.font = '11px system-ui, sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('Claude Code', markerX, padding.top - 5);
            }
        }
    }
}

function filterSources() {
    const searchTerm = document.getElementById('sources-search').value.toLowerCase();
    const statusValue = document.getElementById('sources-status-filter').value;
    const licenseValue = document.getElementById('sources-license-filter').value;

    const filtered = sourcesData.families.filter(family => {
        const matchesSearch = !searchTerm ||
            (family.family_name && family.family_name.toLowerCase().includes(searchTerm)) ||
            (family.designer && family.designer.toLowerCase().includes(searchTerm));
        const matchesStatus = statusValue === 'all' || family.status === statusValue;
        const matchesLicense = licenseValue === 'all' || family.license === licenseValue;
        return matchesSearch && matchesStatus && matchesLicense;
    });

    const container = document.getElementById('sources-table-container');
    renderSourcesTable(container, filtered);
    document.getElementById('sources-count').textContent =
        `${filtered.length} of ${sourcesData.families.length} families`;
}

function renderSourcesTable(container, families) {
    if (families.length === 0) {
        container.innerHTML = '<p class="no-results">No families match the current filters.</p>';
        return;
    }

    // Limit to first 200 for performance, with a message
    const displayFamilies = families.slice(0, 200);
    const hasMore = families.length > 200;

    const table = document.createElement('table');
    table.className = 'sources-table';
    table.innerHTML = `
        <thead>
            <tr>
                <th>Family</th>
                <th>Designer</th>
                <th>Repository</th>
                <th>Commit</th>
                <th>Config</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            ${displayFamilies.map(family => `
                <tr class="status-row-${family.status}">
                    <td class="family-name">${escapeHtml(family.family_name || 'Unknown')}</td>
                    <td class="designer-name">${escapeHtml(family.designer || '-')}</td>
                    <td class="repo-cell">
                        ${family.repository_url
                            ? `<a href="${escapeHtml(family.repository_url)}" target="_blank" title="${escapeHtml(family.repository_url)}">
                                ${escapeHtml(family.repository_url.replace('https://github.com/', '').substring(0, 30))}${family.repository_url.length > 50 ? '...' : ''}
                               </a>`
                            : '<span class="missing">—</span>'
                        }
                    </td>
                    <td class="commit-cell">
                        ${family.commit
                            ? `<code title="${escapeHtml(family.commit)}">${escapeHtml(family.commit.substring(0, 7))}</code>`
                            : '<span class="missing">—</span>'
                        }
                    </td>
                    <td class="config-cell">
                        ${family.config_yaml
                            ? `<code title="${escapeHtml(family.config_yaml)}">${escapeHtml(family.config_yaml.split('/').pop())}</code>`
                            : '<span class="missing">—</span>'
                        }
                    </td>
                    <td class="status-cell">
                        <span class="status-badge status-${family.status}">${formatStatus(family.status)}</span>
                    </td>
                </tr>
            `).join('')}
        </tbody>
    `;

    container.innerHTML = '';
    container.appendChild(table);

    if (hasMore) {
        const moreMsg = document.createElement('p');
        moreMsg.className = 'more-results';
        moreMsg.textContent = `Showing first 200 of ${families.length} results. Use filters to narrow down.`;
        container.appendChild(moreMsg);
    }
}

function formatStatus(status) {
    const statusLabels = {
        'complete': 'Complete',
        'missing_config': 'Missing Config',
        'missing_commit': 'Missing Commit',
        'incomplete_source': 'Incomplete',
        'no_source': 'No Source'
    };
    return statusLabels[status] || status;
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
                ${pr.files_to_modify ? `
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
                ` : ''}
                ${pr.changes && pr.changes.add_commit ? `
                    <div class="pr-changes">
                        <strong>Add commit:</strong> <code>${escapeHtml(pr.changes.add_commit)}</code>
                    </div>
                ` : ''}
                ${pr.changes && pr.changes.options ? `
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
    if (!changes) return '';
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
    const seenPRs = new Set();

    // Analyze assistant messages for accomplishments
    messages.forEach(msg => {
        if (msg.role === 'assistant') {
            const text = msg.message.toLowerCase();

            // Detect completed work - PRs
            if (text.includes('created pr') || text.includes('submitted pr')) {
                const prMatch = msg.message.match(/PR #(\d+)/i);
                if (prMatch && !seenPRs.has(prMatch[1])) {
                    seenPRs.add(prMatch[1]);
                    done.push({
                        text: `Created PR #${prMatch[1]} for google/fonts`,
                        links: [{
                            text: `PR #${prMatch[1]}`,
                            url: `https://github.com/google/fonts/pull/${prMatch[1]}`
                        }]
                    });
                }
            }
            if (text.includes('added') && text.includes('designer')) {
                const countMatch = msg.message.match(/(\d+)\s+designer/i);
                if (countMatch && !done.some(d => d.text && d.text.includes('designer biographies'))) {
                    done.push({ text: `Researched and added ${countMatch[1]} designer biographies` });
                }
            }
            if (text.includes('enrichment') || text.includes('bio.html')) {
                if (!done.some(d => (d.text || d).includes('designer'))) {
                    done.push({ text: 'Enriched designer metadata catalog' });
                }
            }
            if (text.includes('implemented') || text.includes('added') && text.includes('tab')) {
                const feature = msg.message.match(/added\s+(?:the\s+)?["']?([^"'\n]+)["']?\s+tab/i);
                if (feature) {
                    done.push({ text: `Implemented ${feature[1]} feature` });
                }
            }
        }
    });

    // Remove duplicates based on text
    const seenTexts = new Set();
    const uniqueDone = done.filter(item => {
        const text = item.text || item;
        if (seenTexts.has(text)) return false;
        seenTexts.add(text);
        return true;
    });

    // Default planned items if nothing specific found
    if (planned.length === 0) {
        planned.push({ text: 'Continue designer catalog enrichment' });
        planned.push({ text: 'Repository audit and validation' });
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
        ul.innerHTML = items.map(item => {
            const text = item.text || item;
            let html = escapeHtml(text);
            // Replace link placeholders with actual hyperlinks
            if (item.links) {
                item.links.forEach(link => {
                    html = html.replace(
                        escapeHtml(link.text),
                        `<a href="${escapeHtml(link.url)}" target="_blank" class="status-link">${escapeHtml(link.text)}</a>`
                    );
                });
            }
            return `<li>${html}</li>`;
        }).join('');
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
        ? statusData.done.map(item => `<text:list-item><text:p text:style-name="P2">${formatODPItemWithLinks(item)}</text:p></text:list-item>`).join('\n')
        : '<text:list-item><text:p text:style-name="P2">(No items recorded)</text:p></text:list-item>';

    const plannedItems = statusData.planned.length > 0
        ? statusData.planned.map(item => `<text:list-item><text:p text:style-name="P2">${formatODPItemWithLinks(item)}</text:p></text:list-item>`).join('\n')
        : '<text:list-item><text:p text:style-name="P2">(No items planned)</text:p></text:list-item>';

    const questionItems = statusData.questions.length > 0
        ? statusData.questions.map(item => `<text:list-item><text:p text:style-name="P2">${formatODPItemWithLinks(item)}</text:p></text:list-item>`).join('\n')
        : '<text:list-item><text:p text:style-name="P2">(No questions pending)</text:p></text:list-item>';

    return `<?xml version="1.0" encoding="UTF-8"?>
<office:document xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
    xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
    xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"
    xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0"
    xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0"
    xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"
    xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"
    xmlns:xlink="http://www.w3.org/1999/xlink"
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
    <style:style style:name="Link" style:family="text">
      <style:text-properties fo:color="#90caf9" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color"/>
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

function formatODPItemWithLinks(item) {
    const text = item.text || item;
    if (!item.links || item.links.length === 0) {
        return escapeXml(text);
    }

    // Replace link text with ODP hyperlink elements
    let result = text;
    item.links.forEach(link => {
        result = result.replace(
            link.text,
            `{{LINK:${link.url}:${link.text}}}`
        );
    });

    // Now escape and convert placeholders to actual ODP links
    result = escapeXml(result);
    result = result.replace(
        /\{\{LINK:([^:]+):([^}]+)\}\}/g,
        '<text:a xlink:type="simple" xlink:href="$1"><text:span text:style-name="Link">$2</text:span></text:a>'
    );

    return result;
}

// Cache Stats functionality
async function loadCacheStats() {
    try {
        const response = await fetch('data/cache_stats.json');
        const data = await response.json();

        // Update stats
        document.getElementById('cache-total').textContent = data.total_unique_repos;
        document.getElementById('cache-cloned').textContent = data.cloned;
        document.getElementById('cache-not-cloned').textContent = data.not_cloned;

        // Calculate and display percentage
        const percent = ((data.cloned / data.total_unique_repos) * 100).toFixed(1);
        document.getElementById('cache-percent').textContent = percent + '% cloned';
        document.getElementById('cache-bar').style.width = percent + '%';

        // Update not-cloned count
        document.getElementById('not-cloned-count').textContent = data.not_cloned;

        // Populate not-cloned list
        const ul = document.getElementById('not-cloned-repos');
        if (data.not_cloned_list && data.not_cloned_list.length > 0) {
            ul.innerHTML = data.not_cloned_list.map(url => {
                const shortUrl = url.replace('https://github.com/', '').replace('https://gitlab.com/', 'gitlab:');
                return `<li><a href="${escapeHtml(url)}" target="_blank">${escapeHtml(shortUrl)}</a></li>`;
            }).join('');
            if (data.not_cloned > data.not_cloned_list.length) {
                ul.innerHTML += `<li><em>... and ${data.not_cloned - data.not_cloned_list.length} more</em></li>`;
            }
        } else {
            ul.innerHTML = '<li>All repositories are cloned!</li>';
        }
    } catch (error) {
        console.error('Failed to load cache stats:', error);
        document.getElementById('cache-stats').innerHTML = '<p class="error">Failed to load cache stats.</p>';
    }
}

// Build Approaches functionality
let buildsData = null;

const CATEGORY_COLORS = {
    gftools_builder: '#34a853',
    gftools_builder_makefile: '#4caf50',
    fontmake_direct: '#2196f3',
    custom_build_py: '#9c27b0',
    custom_build_sh: '#7b1fa2',
    makefile_other: '#ff9800',
    travis_ci_only: '#795548',
    github_actions_only: '#607d8b',
    source_no_build: '#f44336',
    prebuilt_only: '#e91e63',
    unknown: '#9e9e9e'
};

async function loadBuildApproaches() {
    const container = document.getElementById('builds-table-container');
    const searchInput = document.getElementById('builds-search');
    const categoryFilter = document.getElementById('builds-category-filter');
    const sourceFilter = document.getElementById('builds-source-filter');
    const countSpan = document.getElementById('builds-count');

    try {
        const response = await fetch('data/build_approaches.json');
        buildsData = await response.json();

        // Check if scan is pending
        if (buildsData.status === 'pending_scan' || buildsData.total_repos === 0) {
            container.innerHTML = '<p class="builds-pending-notice">Build classification scan has not been run yet. Run <code>python3 scripts/classify_build_approaches.py</code> to populate this data.</p>';
            document.getElementById('builds-total').textContent = '0';
            document.getElementById('builds-gftools').textContent = '0';
            document.getElementById('builds-fontmake').textContent = '0';
            document.getElementById('builds-custom').textContent = '0';
            document.getElementById('builds-nobuild').textContent = '0';
            renderBuildsDescriptions(buildsData.summary.by_category);
            return;
        }

        // Show degraded mode notice
        if (buildsData.degraded_mode) {
            const intro = document.getElementById('builds-intro');
            intro.innerHTML += '<p style="margin-top:0.5rem;color:#b06d00;"><strong>Note:</strong> ' +
                escapeHtml(buildsData.notes || 'Running in degraded mode.') + '</p>';
        }

        // Update summary
        updateBuildsSummary(buildsData);

        // Populate category filter
        buildsData.summary.by_category.forEach(cat => {
            if (cat.count > 0) {
                const opt = document.createElement('option');
                opt.value = cat.key;
                opt.textContent = `${cat.label} (${cat.count})`;
                categoryFilter.appendChild(opt);
            }
        });

        // Update timestamp
        if (buildsData.generated_at) {
            document.getElementById('builds-timestamp').textContent =
                new Date(buildsData.generated_at).toLocaleString();
        }

        // Render descriptions
        renderBuildsDescriptions(buildsData.summary.by_category);

        // Set up filters
        searchInput.addEventListener('input', () => filterBuilds());
        categoryFilter.addEventListener('change', () => filterBuilds());
        sourceFilter.addEventListener('change', () => filterBuilds());

        // Initial render
        renderBuildsTable(container, buildsData.repos);
        countSpan.textContent = `${buildsData.repos.length} repos`;
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load build approaches data.</p>';
        console.error('Error loading build approaches:', error);
    }
}

function updateBuildsSummary(data) {
    const cats = {};
    data.summary.by_category.forEach(c => { cats[c.key] = c.count; });

    document.getElementById('builds-total').textContent = data.total_repos;
    document.getElementById('builds-gftools').textContent =
        (cats.gftools_builder || 0) + (cats.gftools_builder_makefile || 0);
    document.getElementById('builds-fontmake').textContent =
        cats.fontmake_direct || 0;
    document.getElementById('builds-custom').textContent =
        (cats.custom_build_py || 0) + (cats.custom_build_sh || 0) +
        (cats.makefile_other || 0);
    document.getElementById('builds-nobuild').textContent =
        (cats.source_no_build || 0) + (cats.prebuilt_only || 0) +
        (cats.unknown || 0);

    // Render charts
    renderBuildsCategoryChart(data.summary.by_category);
    renderBuildsSourceChart(data.summary.by_source_format);
}

function renderBuildsCategoryChart(categories) {
    const canvas = document.getElementById('builds-category-chart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    ctx.clearRect(0, 0, width, height);

    const data = categories.filter(c => c.count > 0);
    if (data.length === 0) return;

    const total = data.reduce((sum, d) => sum + d.count, 0);
    const barHeight = 32;
    const barGap = 12;
    const labelWidth = 200;
    const valueWidth = 100;
    const startX = labelWidth;
    const maxBarWidth = width - labelWidth - valueWidth - 20;

    data.forEach((d, i) => {
        const y = 20 + i * (barHeight + barGap);
        const barWidth = Math.max(2, (d.count / total) * maxBarWidth);

        // Label
        ctx.fillStyle = '#e0e0e0';
        ctx.font = '13px system-ui, sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText(d.label, labelWidth - 10, y + barHeight / 2 + 4);

        // Bar
        ctx.fillStyle = CATEGORY_COLORS[d.key] || '#9e9e9e';
        ctx.fillStyle = CATEGORY_COLORS[d.key] || '#9e9e9e';
        ctx.fillRect(startX, y, barWidth, barHeight);

        // Value
        ctx.fillStyle = '#e0e0e0';
        ctx.textAlign = 'left';
        ctx.fillText(
            `${d.count} (${((d.count / total) * 100).toFixed(1)}%)`,
            startX + barWidth + 8,
            y + barHeight / 2 + 4
        );
    });
}

function renderBuildsSourceChart(formats) {
    const canvas = document.getElementById('builds-source-chart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    ctx.clearRect(0, 0, width, height);

    const data = (formats || []).filter(f => f.count > 0);
    if (data.length === 0) return;

    const maxCount = Math.max(...data.map(d => d.count));
    const barHeight = 32;
    const barGap = 12;
    const labelWidth = 200;
    const valueWidth = 80;
    const startX = labelWidth;
    const maxBarWidth = width - labelWidth - valueWidth - 20;

    const formatColors = {
        glyphs: '#ff9800',
        glyphspackage: '#ff5722',
        ufo: '#2196f3',
        designspace: '#4caf50',
        sfd: '#9c27b0',
        none: '#9e9e9e'
    };

    data.forEach((d, i) => {
        const y = 20 + i * (barHeight + barGap);
        const barWidth = Math.max(2, (d.count / maxCount) * maxBarWidth);

        // Label
        ctx.fillStyle = '#e0e0e0';
        ctx.font = '13px system-ui, sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText(d.label, labelWidth - 10, y + barHeight / 2 + 4);

        // Bar
        ctx.fillStyle = formatColors[d.key] || '#9e9e9e';
        ctx.fillRect(startX, y, barWidth, barHeight);

        // Value
        ctx.fillStyle = '#e0e0e0';
        ctx.textAlign = 'left';
        ctx.fillText(d.count.toString(), startX + barWidth + 8, y + barHeight / 2 + 4);
    });
}

function renderBuildsDescriptions(categories) {
    const container = document.getElementById('builds-descriptions');
    if (!container || !categories) return;

    let html = '<h3>Build Approach Descriptions</h3>';
    categories.forEach(cat => {
        html += `
            <div class="build-desc-card cat-${cat.key}">
                <span class="desc-label">${escapeHtml(cat.label)}</span>
                <span class="desc-count">${cat.count}</span>
                <span class="desc-text">${escapeHtml(cat.description)}</span>
            </div>
        `;
    });
    container.innerHTML = html;
}

function filterBuilds() {
    const searchTerm = document.getElementById('builds-search').value.toLowerCase();
    const categoryValue = document.getElementById('builds-category-filter').value;
    const sourceValue = document.getElementById('builds-source-filter').value;

    const filtered = buildsData.repos.filter(repo => {
        const matchesSearch = !searchTerm ||
            repo.repo.toLowerCase().includes(searchTerm) ||
            (repo.families && repo.families.some(f => f.toLowerCase().includes(searchTerm)));
        const matchesCategory = categoryValue === 'all' || repo.category === categoryValue;
        const matchesSource = sourceValue === 'all' ||
            (sourceValue === 'none' && repo.source_formats.length === 0) ||
            repo.source_formats.includes(sourceValue);
        return matchesSearch && matchesCategory && matchesSource;
    });

    const container = document.getElementById('builds-table-container');
    renderBuildsTable(container, filtered);
    document.getElementById('builds-count').textContent =
        `${filtered.length} of ${buildsData.repos.length} repos`;
}

function formatBuildCategory(key) {
    const labels = {
        gftools_builder: 'gftools-builder',
        gftools_builder_makefile: 'gftools via Make',
        fontmake_direct: 'fontmake',
        custom_build_py: 'Custom Python',
        custom_build_sh: 'Custom Shell',
        makefile_other: 'Makefile (other)',
        travis_ci_only: 'Travis CI',
        github_actions_only: 'GitHub Actions',
        source_no_build: 'No build',
        prebuilt_only: 'Pre-built only',
        unknown: 'Unknown'
    };
    return labels[key] || key;
}

function renderBuildsTable(container, repos) {
    if (!repos || repos.length === 0) {
        container.innerHTML = '<p class="no-results">No repos match the current filters.</p>';
        return;
    }

    const displayRepos = repos.slice(0, 200);
    const hasMore = repos.length > 200;

    const table = document.createElement('table');
    table.className = 'builds-table';
    table.innerHTML = `
        <thead>
            <tr>
                <th>Repository</th>
                <th>Category</th>
                <th>Source Formats</th>
                <th>Config</th>
                <th>Families</th>
            </tr>
        </thead>
        <tbody>
            ${displayRepos.map(repo => `
                <tr>
                    <td class="repo-name">
                        ${repo.url
                            ? `<a href="${escapeHtml(repo.url)}" target="_blank">${escapeHtml(repo.repo)}</a>`
                            : escapeHtml(repo.repo)
                        }
                    </td>
                    <td>
                        <span class="category-badge cat-${repo.category}">${formatBuildCategory(repo.category)}</span>
                    </td>
                    <td>
                        ${repo.source_formats.length > 0
                            ? repo.source_formats.map(f => `<span class="source-tag fmt-${f}">${escapeHtml(f)}</span>`).join('')
                            : '<span class="missing">\u2014</span>'
                        }
                    </td>
                    <td class="config-cell">
                        ${repo.config_path
                            ? `<code title="${escapeHtml(repo.config_path)}">${escapeHtml(repo.config_path.split('/').pop())}</code>`
                            : '<span class="missing">\u2014</span>'
                        }
                    </td>
                    <td class="families-cell" title="${escapeHtml((repo.families || []).join(', '))}">
                        ${repo.families && repo.families.length > 0
                            ? escapeHtml(repo.families.slice(0, 2).join(', ')) + (repo.families.length > 2 ? ` +${repo.families.length - 2}` : '')
                            : '<span class="missing">\u2014</span>'
                        }
                    </td>
                </tr>
            `).join('')}
        </tbody>
    `;

    container.innerHTML = '';
    container.appendChild(table);

    if (hasMore) {
        const moreMsg = document.createElement('p');
        moreMsg.className = 'more-results';
        moreMsg.textContent = `Showing first 200 of ${repos.length} results. Use filters to narrow down.`;
        container.appendChild(moreMsg);
    }
}

// Plans functionality
async function loadPlans() {
    const container = document.getElementById('plans-list');

    try {
        const response = await fetch('data/plans.json');
        const plans = await response.json();

        if (plans.length === 0) {
            container.innerHTML = '<p class="no-results">No plans documented yet.</p>';
            return;
        }

        container.innerHTML = plans.map(plan => {
            const date = plan.timestamp ? new Date(plan.timestamp).toLocaleString() : 'Unknown';
            const statusClass = plan.status === 'completed' ? 'complete' :
                                plan.status === 'in_progress' ? 'warning' : 'error';

            return `
                <div class="plan-card">
                    <div class="plan-header">
                        <div class="plan-title">${escapeHtml(plan.title)}</div>
                        <div class="plan-badges">
                            <span class="plan-date">${escapeHtml(date)}</span>
                            <span class="status-badge status-${plan.status === 'in_progress' ? 'missing_config' : plan.status === 'completed' ? 'complete' : 'no_source'}">${escapeHtml(plan.status.replace('_', ' '))}</span>
                        </div>
                    </div>
                    <div class="plan-prompt">
                        <strong>Original prompt:</strong> ${escapeHtml(plan.prompt)}
                    </div>
                    <div class="plan-summary">${escapeHtml(plan.summary)}</div>
                    <div class="plan-steps">
                        <strong>Steps:</strong>
                        <ol>
                            ${plan.steps.map(step => `
                                <li class="plan-step step-${step.status}">
                                    <span class="step-status">${step.status === 'completed' ? '\u2705' : step.status === 'in_progress' ? '\u23f3' : step.status === 'blocked' ? '\u26d4' : '\u2b1c'}</span>
                                    ${escapeHtml(step.description)}
                                </li>
                            `).join('')}
                        </ol>
                    </div>
                    ${plan.files_modified ? `
                        <details class="plan-files">
                            <summary>Files modified (${plan.files_modified.length})</summary>
                            <ul>
                                ${plan.files_modified.map(f => `<li><code>${escapeHtml(f.file)}</code> <em>(${escapeHtml(f.action)})</em></li>`).join('')}
                            </ul>
                        </details>
                    ` : ''}
                </div>
            `;
        }).join('');
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load plans data.</p>';
        console.error('Error loading plans:', error);
    }
}

// Disk Usage functionality
async function loadDiskUsage() {
    try {
        const response = await fetch('data/disk_usage.json');
        const data = await response.json();

        // Update stats
        document.getElementById('disk-total').textContent = data.filesystem.total;
        document.getElementById('disk-used').textContent = data.filesystem.used;
        document.getElementById('disk-available').textContent = data.filesystem.available;

        const percent = data.filesystem.percent;
        const percentElement = document.getElementById('disk-percent');
        percentElement.textContent = percent + '%';

        // Color-code based on usage
        if (percent >= 98) {
            percentElement.classList.add('critical');
        } else if (percent >= 95) {
            percentElement.classList.add('warning');
        }

        // Update bar
        const bar = document.getElementById('disk-bar');
        bar.style.width = percent + '%';
        if (percent >= 98) {
            bar.classList.add('critical');
        } else if (percent >= 95) {
            bar.classList.add('warning');
        }

        // Update breakdown table
        const tbody = document.querySelector('#disk-breakdown-table tbody');
        tbody.innerHTML = data.breakdown.map(item => `
            <tr>
                <td><code>${escapeHtml(item.description || item.path)}</code></td>
                <td>${escapeHtml(item.size)}</td>
            </tr>
        `).join('');

        // Update timestamp
        document.getElementById('disk-timestamp').textContent = new Date(data.timestamp).toLocaleString();
    } catch (error) {
        document.getElementById('disk-usage').innerHTML = '<p class="error">Failed to load disk usage data.</p>';
    }
}

// Bio Audit functionality
let bioAuditData = null;

async function loadBioAudit() {
    const container = document.getElementById('bio-audit-content');
    if (!container) return;

    try {
        const response = await fetch('data/bio_audit.json');
        bioAuditData = await response.json();
        renderBioAudit(container, bioAuditData);
    } catch (error) {
        container.innerHTML = '<p class="error">Failed to load bio audit data. Run <code>python3 scripts/audit_bios.py</code> to generate it.</p>';
        console.error('Error loading bio audit:', error);
    }
}

function renderBioAudit(container, data) {
    const s = data.summary;
    const total = s.total_bios;
    const pct = (n) => total > 0 ? ((n / total) * 100).toFixed(1) : '0';

    // Issue type labels
    const issueLabels = {
        missing_target_blank: 'Missing target="_blank"',
        http_not_https: 'HTTP instead of HTTPS',
        promotional_language: 'Promotional language',
        first_person: 'First-person voice',
        vague_filler: 'Vague filler phrases',
        forbidden_html_tags: 'Forbidden HTML tags',
        html_errors: 'HTML errors (broken markup)',
        arctic_code_vault: 'Arctic Code Vault mention',
        email_address: 'Email address in bio',
        over_word_limit: 'Over ~150 word limit',
        link_text_format: 'Link text format issues',
        links_in_body: 'Links in body paragraph',
        missing_pipe_separator: 'Missing pipe separator',
        other: 'Other issues',
    };

    // Sort issue types by count
    const issueTypes = Object.entries(s.bios_with_issue_type)
        .sort((a, b) => b[1] - a[1]);

    // Build the summary section
    let html = `
        <div class="guide-section">
            <h3>Summary Statistics</h3>
            <table class="guide-table">
                <thead>
                    <tr><th>Metric</th><th>Count</th><th>Percentage</th></tr>
                </thead>
                <tbody>
                    <tr><td>Total bios inspected</td><td><strong>${total}</strong></td><td>100%</td></tr>
                    <tr><td>Fully compliant</td><td><strong>${s.passing}</strong></td><td>${pct(s.passing)}%</td></tr>
                    <tr><td>Minor issues only (1&ndash;2 items)</td><td><strong>${s.minor_issues}</strong></td><td>${pct(s.minor_issues)}%</td></tr>
                    <tr><td>Major issues (3+ items)</td><td><strong>${s.major_issues}</strong></td><td>${pct(s.major_issues)}%</td></tr>
                </tbody>
            </table>

            <h4>Issues by Type (bios affected)</h4>
            <table class="guide-table">
                <thead>
                    <tr><th>Issue Type</th><th>Bios Affected</th><th>% of Catalog</th></tr>
                </thead>
                <tbody>
                    ${issueTypes.map(([key, count]) => `
                        <tr>
                            <td>${escapeHtml(issueLabels[key] || key)}</td>
                            <td>${count}</td>
                            <td>${pct(count)}%</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        </div>

        <div class="guide-section">
            <h3>Quality Assessment</h3>
            <p>Out of ${total} bios in the catalog, only <strong>${s.passing}</strong> (${pct(s.passing)}%) fully pass the Editorial Guide checklist. ${s.minor_issues} bios (${pct(s.minor_issues)}%) have minor issues (1&ndash;2 items, often just a missing <code>target="_blank"</code>), while <strong>${s.major_issues}</strong> (${pct(s.major_issues)}%) have substantive problems requiring editorial attention.</p>
            <p>The most pervasive issue &mdash; missing <code>target="_blank"</code> on links &mdash; affects ${s.bios_with_issue_type.missing_target_blank || 0} bios (${pct(s.bios_with_issue_type.missing_target_blank || 0)}%). This is a mechanical fix that could be automated. Promotional language (${s.bios_with_issue_type.promotional_language || 0} bios) requires more careful editorial work.</p>
        </div>
    `;

    // Severity filter controls
    html += `
        <div class="guide-section">
            <h3>All Bios</h3>
            <div style="margin-bottom: 1em; display: flex; gap: 1em; align-items: center; flex-wrap: wrap;">
                <label>Filter:
                    <select id="bio-audit-severity-filter" style="padding: 0.3em; background: #1e1e1e; color: #e0e0e0; border: 1px solid #555; border-radius: 4px;">
                        <option value="all">All (${total})</option>
                        <option value="major">Major issues (${s.major_issues})</option>
                        <option value="minor">Minor issues (${s.minor_issues})</option>
                        <option value="pass">Passing (${s.passing})</option>
                    </select>
                </label>
                <label>Search:
                    <input type="text" id="bio-audit-search" placeholder="Designer name..." style="padding: 0.3em; background: #1e1e1e; color: #e0e0e0; border: 1px solid #555; border-radius: 4px; width: 200px;">
                </label>
                <span id="bio-audit-count" style="color: #888;">${total} bios</span>
            </div>
            <div id="bio-audit-table-container"></div>
        </div>
    `;

    container.innerHTML = html;

    // Render the table
    renderBioAuditTable(data.results, 'all', '');

    // Set up filter event listeners
    document.getElementById('bio-audit-severity-filter').addEventListener('change', () => filterBioAudit());
    document.getElementById('bio-audit-search').addEventListener('input', () => filterBioAudit());
}

function filterBioAudit() {
    const severity = document.getElementById('bio-audit-severity-filter').value;
    const search = document.getElementById('bio-audit-search').value.toLowerCase();
    renderBioAuditTable(bioAuditData.results, severity, search);
}

function renderBioAuditTable(results, severityFilter, searchFilter) {
    const filtered = results.filter(r => {
        const matchesSeverity = severityFilter === 'all' || r.severity === severityFilter;
        const matchesSearch = !searchFilter ||
            (r.designer_name && r.designer_name.toLowerCase().includes(searchFilter)) ||
            (r.designer_id && r.designer_id.toLowerCase().includes(searchFilter));
        return matchesSeverity && matchesSearch;
    });

    const tableContainer = document.getElementById('bio-audit-table-container');
    const countSpan = document.getElementById('bio-audit-count');
    countSpan.textContent = `${filtered.length} of ${results.length} bios`;

    if (filtered.length === 0) {
        tableContainer.innerHTML = '<p class="no-results">No bios match the current filters.</p>';
        return;
    }

    // Sort: major first, then minor, then pass
    const severityOrder = { major: 0, minor: 1, pass: 2 };
    const sorted = [...filtered].sort((a, b) => {
        const oa = severityOrder[a.severity] ?? 3;
        const ob = severityOrder[b.severity] ?? 3;
        if (oa !== ob) return oa - ob;
        return b.issue_count - a.issue_count;
    });

    const display = sorted.slice(0, 200);
    const hasMore = sorted.length > 200;

    const severityColors = {
        pass: '#4caf50',
        minor: '#ff9800',
        major: '#f44336',
    };

    const table = document.createElement('table');
    table.className = 'guide-table';
    table.innerHTML = `
        <thead>
            <tr>
                <th>Designer</th>
                <th>Severity</th>
                <th>Issues</th>
                <th>Details</th>
            </tr>
        </thead>
        <tbody>
            ${display.map(r => `
                <tr>
                    <td><strong>${escapeHtml(r.designer_name)}</strong><br><small style="color:#888">${escapeHtml(r.designer_id)}</small></td>
                    <td><span style="color: ${severityColors[r.severity] || '#888'}; font-weight: bold;">${r.severity === 'pass' ? 'PASS' : r.severity.toUpperCase()}</span></td>
                    <td>${r.issue_count}</td>
                    <td>${r.issues.length > 0
                        ? `<details><summary>${r.issue_count} issue${r.issue_count !== 1 ? 's' : ''}</summary><ul style="margin: 0.5em 0; padding-left: 1.2em;">${r.issues.map(i => `<li style="margin-bottom:0.3em;">${escapeHtml(i)}</li>`).join('')}</ul></details>`
                        : '<span style="color:#4caf50;">No issues</span>'
                    }</td>
                </tr>
            `).join('')}
        </tbody>
    `;

    tableContainer.innerHTML = '';
    tableContainer.appendChild(table);

    if (hasMore) {
        const msg = document.createElement('p');
        msg.className = 'more-results';
        msg.textContent = `Showing first 200 of ${sorted.length} results. Use filters to narrow down.`;
        tableContainer.appendChild(msg);
    }
}

// Pre-Build Research functionality
let prebuildData = null;

async function loadPrebuildResearch() {
    try {
        const response = await fetch('data/prebuild_research.json');
        prebuildData = await response.json();
        renderPrebuildResearch(prebuildData);
    } catch (error) {
        console.error('Error loading prebuild research:', error);
    }
}

function renderPrebuildResearch(data) {
    // Update timestamp
    const tsEl = document.getElementById('prebuild-timestamp');
    if (tsEl && data._metadata) {
        tsEl.textContent = data._metadata.generated;
    }

    // Build flat repo list for filtering
    const allRepos = [];
    const actionTypes = data.action_types;
    const repos = data.repos;

    // Compute totals
    let totalRepos = 0;
    const actionTypeEntries = [];

    for (const [key, info] of Object.entries(actionTypes)) {
        const count = info.total_repos || (info.total_repos_with_scripts || 0) + (info.total_repos_with_dependency || 0);
        totalRepos += count;
        actionTypeEntries.push({
            key,
            label: formatActionType(key),
            count,
            priority: info.priority,
            proposed: info.proposed_feature,
            description: info.description
        });
    }

    // Summary cards
    const totalEl = document.getElementById('prebuild-total-repos');
    if (totalEl) totalEl.textContent = totalRepos;

    const typesEl = document.getElementById('prebuild-action-types');
    if (typesEl) typesEl.textContent = Object.keys(actionTypes).length;

    const ufoEl = document.getElementById('prebuild-ufo-merge');
    if (ufoEl) {
        const ufo = actionTypes.ufo_merging;
        ufoEl.textContent = (ufo.total_repos_with_scripts || 0) + (ufo.total_repos_with_dependency || 0);
    }

    // Priority table (revised with existing feature overlap)
    const priorityRows = [
        { status: 'COVERED', type: 'UFO Source Merging', count: '~47', existing: 'includeSubsets + addSubset', gap: 'Complex multi-step merges need investigation' },
        { status: 'COVERED', type: 'Glyphs-to-UFO Conversion', count: '~29', existing: 'glyphs2ds (auto-triggered)', gap: 'Custom flags not covered' },
        { status: 'PARTIAL', type: 'Designspace Manipulation', count: '~10', existing: 'flattenComponents, subspace', gap: 'Source-level axis dropping' },
        { status: 'LOW', type: 'Glyphs Source Manipulation', count: '~8', existing: 'exec recipe operation', gap: 'Too diverse to standardize' },
        { status: 'LOW', type: 'UFO Source Manipulation', count: '~13', existing: 'exec recipe operation', gap: 'Too diverse to standardize' },
        { status: 'N/A', type: 'Direct addGlyph', count: '~11', existing: 'includeSubsets (if migrated)', gap: 'Repos don\'t use builder' },
        { status: 'N/A', type: 'Fully Custom Pipelines', count: '~66', existing: 'N/A', gap: 'Repos don\'t use builder' },
        { status: 'N/A', type: 'Config/Source Generation', count: '~3', existing: 'None', gap: 'Too niche' },
        { status: 'N/A', type: 'Repo Initialization', count: '~249', existing: 'N/A', gap: 'Not a build action' }
    ];

    const priorityTbody = document.getElementById('prebuild-priority-tbody');
    if (priorityTbody) {
        priorityTbody.innerHTML = priorityRows.map(r => {
            const statusColor = r.status === 'COVERED' ? '#4caf50' :
                                r.status === 'PARTIAL' ? '#ff9800' :
                                r.status === 'LOW' ? '#2196f3' : '#888';
            return `<tr>
                <td><strong style="color: ${statusColor}">${escapeHtml(r.status)}</strong></td>
                <td>${escapeHtml(r.type)}</td>
                <td>${escapeHtml(r.count)}</td>
                <td>${escapeHtml(r.existing)}</td>
                <td>${escapeHtml(r.gap)}</td>
            </tr>`;
        }).join('');
    }

    // Chart
    renderPrebuildChart(actionTypeEntries.filter(e => e.key !== 'repo_initialization'));

    // Merge repos detail
    renderMergeRepos(repos);

    // Full inventory table
    renderPrebuildInventory(repos);

    // Populate action type filter
    const filterSelect = document.getElementById('prebuild-action-filter');
    if (filterSelect) {
        for (const [key] of Object.entries(repos)) {
            const opt = document.createElement('option');
            opt.value = key;
            opt.textContent = formatActionType(key);
            filterSelect.appendChild(opt);
        }
        filterSelect.addEventListener('change', () => filterPrebuild());
    }

    const searchInput = document.getElementById('prebuild-search');
    if (searchInput) {
        searchInput.addEventListener('input', () => filterPrebuild());
    }
}

function formatActionType(key) {
    const labels = {
        ufo_merging: 'UFO Source Merging',
        glyphs_to_ufo_conversion: 'Glyphs-to-UFO Conversion',
        glyphs_source_manipulation: 'Glyphs Source Manipulation',
        designspace_manipulation: 'Designspace Manipulation',
        ufo_source_manipulation: 'UFO Source Manipulation',
        direct_glyph_addition: 'Direct Glyph Addition',
        fully_custom_pipeline: 'Fully Custom Pipeline',
        config_source_generation: 'Config/Source Generation',
        repo_initialization: 'Repo Initialization'
    };
    return labels[key] || key;
}

const PREBUILD_COLORS = {
    ufo_merging: '#f44336',
    glyphs_to_ufo_conversion: '#ff9800',
    designspace_manipulation: '#ff5722',
    glyphs_source_manipulation: '#9c27b0',
    ufo_source_manipulation: '#2196f3',
    direct_glyph_addition: '#4caf50',
    fully_custom_pipeline: '#795548',
    config_source_generation: '#607d8b',
    repo_initialization: '#9e9e9e'
};

function renderPrebuildChart(entries) {
    const canvas = document.getElementById('prebuild-types-chart');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    ctx.clearRect(0, 0, width, height);

    const data = entries.filter(e => e.count > 0).sort((a, b) => b.count - a.count);
    if (data.length === 0) return;

    const maxCount = Math.max(...data.map(d => d.count));
    const barHeight = 32;
    const barGap = 12;
    const labelWidth = 220;
    const valueWidth = 100;
    const startX = labelWidth;
    const maxBarWidth = width - labelWidth - valueWidth - 20;

    data.forEach((d, i) => {
        const y = 20 + i * (barHeight + barGap);
        const barWidth = Math.max(2, (d.count / maxCount) * maxBarWidth);

        ctx.fillStyle = '#e0e0e0';
        ctx.font = '13px system-ui, sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText(d.label, labelWidth - 10, y + barHeight / 2 + 4);

        ctx.fillStyle = PREBUILD_COLORS[d.key] || '#9e9e9e';
        ctx.fillRect(startX, y, barWidth, barHeight);

        ctx.fillStyle = '#e0e0e0';
        ctx.textAlign = 'left';

        const priorityTag = d.priority !== 'N/A' ? ` [${d.priority}]` : '';
        ctx.fillText(`${d.count} repos${priorityTag}`, startX + barWidth + 8, y + barHeight / 2 + 4);
    });
}

function renderMergeRepos(repos) {
    const container = document.getElementById('prebuild-merge-repos');
    if (!container || !repos.ufo_merging) return;

    const scripts = repos.ufo_merging.with_explicit_scripts || [];
    if (scripts.length === 0) {
        container.innerHTML = '<p>No explicit merge script repos found.</p>';
        return;
    }

    const table = document.createElement('table');
    table.className = 'guide-table';
    table.innerHTML = `
        <thead>
            <tr>
                <th>Repository</th>
                <th>Script(s)</th>
                <th>Details</th>
            </tr>
        </thead>
        <tbody>
            ${scripts.map(r => `
                <tr>
                    <td><a href="https://github.com/${escapeHtml(r.repo)}" target="_blank">${escapeHtml(r.repo)}</a></td>
                    <td>${r.scripts.map(s => `<code>${escapeHtml(s)}</code>`).join('<br>')}</td>
                    <td>${escapeHtml(r.details)}</td>
                </tr>
            `).join('')}
        </tbody>
    `;
    container.appendChild(table);
}

function renderPrebuildInventory(repos) {
    const container = document.getElementById('prebuild-table-container');
    if (!container) return;

    // Flatten all repos into a single list
    const allRepos = [];
    for (const [actionType, data] of Object.entries(repos)) {
        // Handle different data shapes
        if (Array.isArray(data)) {
            data.forEach(r => allRepos.push({ ...r, action_type: actionType }));
        } else if (typeof data === 'object') {
            for (const [subKey, subData] of Object.entries(data)) {
                if (Array.isArray(subData)) {
                    subData.forEach(r => allRepos.push({ ...r, action_type: actionType, sub_type: subKey }));
                }
            }
        }
    }

    renderPrebuildTable(container, allRepos, allRepos);
}

function renderPrebuildTable(container, repos, allRepos) {
    if (!repos || repos.length === 0) {
        container.innerHTML = '<p class="no-results">No repos match the current filters.</p>';
        return;
    }

    const countSpan = document.getElementById('prebuild-count');
    if (countSpan) {
        countSpan.textContent = `${repos.length} of ${allRepos.length} repos`;
    }

    const display = repos.slice(0, 200);
    const hasMore = repos.length > 200;

    const table = document.createElement('table');
    table.className = 'builds-table';
    table.innerHTML = `
        <thead>
            <tr>
                <th>Repository</th>
                <th>Action Type</th>
                <th>Tool</th>
                <th>Uses Builder?</th>
                <th>Details</th>
            </tr>
        </thead>
        <tbody>
            ${display.map(r => `
                <tr>
                    <td><a href="https://github.com/${escapeHtml(r.repo)}" target="_blank">${escapeHtml(r.repo)}</a></td>
                    <td><span class="category-badge" style="background: ${PREBUILD_COLORS[r.action_type] || '#9e9e9e'}; color: white; padding: 2px 8px; border-radius: 3px; font-size: 0.85em;">${escapeHtml(formatActionType(r.action_type))}</span></td>
                    <td><code>${escapeHtml(r.tool || '-')}</code></td>
                    <td>${r.uses_gftools_builder === true ? 'Yes' : r.uses_gftools_builder === false ? 'No' : '-'}</td>
                    <td>${r.details ? `<details><summary>Show</summary>${escapeHtml(r.details)}</details>` : '-'}</td>
                </tr>
            `).join('')}
        </tbody>
    `;

    container.innerHTML = '';
    container.appendChild(table);

    if (hasMore) {
        const msg = document.createElement('p');
        msg.className = 'more-results';
        msg.textContent = `Showing first 200 of ${repos.length} results.`;
        container.appendChild(msg);
    }
}

function filterPrebuild() {
    if (!prebuildData) return;

    const searchTerm = (document.getElementById('prebuild-search').value || '').toLowerCase();
    const actionValue = document.getElementById('prebuild-action-filter').value;

    // Rebuild flat list
    const allRepos = [];
    for (const [actionType, data] of Object.entries(prebuildData.repos)) {
        if (Array.isArray(data)) {
            data.forEach(r => allRepos.push({ ...r, action_type: actionType }));
        } else if (typeof data === 'object') {
            for (const [subKey, subData] of Object.entries(data)) {
                if (Array.isArray(subData)) {
                    subData.forEach(r => allRepos.push({ ...r, action_type: actionType, sub_type: subKey }));
                }
            }
        }
    }

    const filtered = allRepos.filter(r => {
        const matchesSearch = !searchTerm || r.repo.toLowerCase().includes(searchTerm);
        const matchesAction = actionValue === 'all' || r.action_type === actionValue;
        return matchesSearch && matchesAction;
    });

    renderPrebuildTable(document.getElementById('prebuild-table-container'), filtered, allRepos);
}
