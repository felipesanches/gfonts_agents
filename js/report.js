// Font Report Page Script

document.addEventListener('DOMContentLoaded', () => {
    loadReport();
});

async function loadReport() {
    const container = document.getElementById('report-content');
    const params = new URLSearchParams(window.location.search);
    const fontSlug = params.get('font');

    if (!fontSlug) {
        container.innerHTML = '<p class="error">No font specified. <a href="index.html">Return to dashboard</a></p>';
        return;
    }

    try {
        const response = await fetch(`data/reports/${fontSlug}.json`);
        if (!response.ok) throw new Error('Report not found');
        const report = await response.json();

        document.title = `${report.font} - Font Report`;
        container.innerHTML = renderReport(report);
    } catch (error) {
        container.innerHTML = `<p class="error">Failed to load report for "${fontSlug}". <a href="index.html">Return to dashboard</a></p>`;
    }
}

function renderReport(r) {
    const statusClass = r.status === 'verified' ? 'verified' : (r.status === 'error' ? 'error' : '');

    let html = `
        <div class="report-header">
            <h2>${escapeHtml(r.font)}</h2>
            <span class="status-badge ${r.status}">${r.status}</span>
        </div>

        <div class="report-section">
            <h3>Repository Information</h3>
            <div class="info-grid">
                <span class="info-label">Upstream Repo:</span>
                <span class="info-value"><a href="${escapeHtml(r.upstream_repo)}" target="_blank">${escapeHtml(r.upstream_repo)}</a></span>

                <span class="info-label">METADATA Commit:</span>
                <span class="info-value"><a href="${escapeHtml(r.upstream_repo)}/commit/${escapeHtml(r.metadata_commit)}" target="_blank">${escapeHtml(r.metadata_commit)}</a></span>

                <span class="info-label">Commit Exists:</span>
                <span class="info-value">${r.commit_exists === null ? 'Unknown' : (r.commit_exists ? 'Yes' : 'No')}</span>

                <span class="info-label">Commit Date:</span>
                <span class="info-value">${r.commit_date || 'Unknown'}</span>

                ${r.commit_author ? `
                <span class="info-label">Commit Author:</span>
                <span class="info-value">${escapeHtml(r.commit_author)}</span>
                ` : ''}

                ${r.commit_message ? `
                <span class="info-label">Commit Message:</span>
                <span class="info-value">${escapeHtml(r.commit_message)}</span>
                ` : ''}
            </div>
        </div>
    `;

    if (r.has_newer_commits && r.newer_commits && r.newer_commits.length > 0) {
        html += `
            <div class="report-section">
                <h3>Newer Commits in Upstream (${r.newer_commits.length})</h3>
                <ul class="commit-list">
                    ${r.newer_commits.map(c => `
                        <li>
                            <span class="commit-hash">${escapeHtml(c.hash.substring(0, 7))}</span>
                            <span class="commit-date">${escapeHtml(c.date)}</span>
                            <span class="commit-message">${escapeHtml(c.message)}</span>
                        </li>
                    `).join('')}
                </ul>
            </div>
        `;
    }

    if (r.google_fonts_pr) {
        html += `
            <div class="report-section">
                <h3>Google Fonts PR</h3>
                <div class="info-grid">
                    <span class="info-label">PR Number:</span>
                    <span class="info-value"><a href="${escapeHtml(r.pr_url)}" target="_blank">#${r.google_fonts_pr}</a></span>

                    ${r.pr_merged_date ? `
                    <span class="info-label">Merged Date:</span>
                    <span class="info-value">${escapeHtml(r.pr_merged_date)}</span>
                    ` : ''}

                    ${r.pr_author ? `
                    <span class="info-label">PR Author:</span>
                    <span class="info-value">${escapeHtml(r.pr_author)}</span>
                    ` : ''}

                    <span class="info-label">References Upstream:</span>
                    <span class="info-value">${r.pr_references_upstream ? 'Yes' : 'No'}</span>
                </div>
            </div>
        `;
    }

    if (r.notes) {
        html += `
            <div class="report-section">
                <h3>Notes</h3>
                <div class="notes-box ${statusClass}">
                    ${escapeHtml(r.notes)}
                </div>
            </div>
        `;
    }

    if (r.pending_questions && r.pending_questions.length > 0) {
        html += `
            <div class="report-section">
                <h3>Pending Questions</h3>
                ${r.pending_questions.map(q => `
                    <div class="question-card">
                        <div class="question-for">For: ${escapeHtml(q.for)}</div>
                        <div class="question-text">${escapeHtml(q.question)}</div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    return html;
}

function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
