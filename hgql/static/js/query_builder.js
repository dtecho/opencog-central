
// HGQL Query Builder JavaScript

class HGQLQueryBuilder {
    constructor() {
        this.currentQuery = {
            type: 'MATCH',
            pattern: '',
            conditions: [],
            bindings: {},
            rules: [],
            confidence: 0.5
        };
        
        this.hypergraphViz = null;
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.initializeVisualization();
        this.loadSchema();
    }
    
    setupEventListeners() {
        document.getElementById('query-type').addEventListener('change', (e) => {
            this.currentQuery.type = e.target.value;
            this.updateQueryBuilder();
        });
        
        document.getElementById('pattern-input').addEventListener('input', (e) => {
            this.currentQuery.pattern = e.target.value;
            this.validatePattern();
        });
        
        document.getElementById('confidence').addEventListener('input', (e) => {
            this.currentQuery.confidence = parseFloat(e.target.value);
            document.getElementById('confidence-value').textContent = e.target.value;
        });
        
        document.getElementById('execute-query').addEventListener('click', () => {
            this.executeQuery();
        });
        
        document.getElementById('new-query').addEventListener('click', () => {
            this.newQuery();
        });
        
        document.getElementById('save-query').addEventListener('click', () => {
            this.saveQuery();
        });
    }
    
    initializeVisualization() {
        const container = document.getElementById('hypergraph-viz');
        const data = {
            nodes: [
                {id: 1, label: 'Concept: Human', color: '#3498db'},
                {id: 2, label: 'Concept: Mortal', color: '#2ecc71'},
                {id: 3, label: 'Predicate: Inheritance', color: '#e74c3c'},
                {id: 4, label: 'Individual: Socrates', color: '#f39c12'}
            ],
            edges: [
                {from: 1, to: 2, label: 'inherits', arrows: 'to'},
                {from: 4, to: 1, label: 'instance-of', arrows: 'to'}
            ]
        };
        
        const options = {
            nodes: {
                shape: 'box',
                margin: 10,
                font: {size: 12, face: 'Arial'},
                borderWidth: 2,
                shadow: true
            },
            edges: {
                arrows: {to: {enabled: true, scaleFactor: 1}},
                color: {inherit: 'from'},
                width: 2,
                shadow: true
            },
            physics: {
                stabilization: {iterations: 100}
            }
        };
        
        this.hypergraphViz = new vis.Network(container, data, options);
    }
    
    async loadSchema() {
        try {
            const response = await fetch('/api/schema');
            const schema = await response.json();
            this.schema = schema;
            this.populateRuleOptions();
        } catch (error) {
            console.error('Failed to load schema:', error);
        }
    }
    
    populateRuleOptions() {
        if (!this.schema) return;
        
        // This would populate rule dropdowns with available inference rules
        console.log('Schema loaded:', this.schema);
    }
    
    updateQueryBuilder() {
        const queryType = this.currentQuery.type;
        
        // Show/hide relevant sections based on query type
        const inferenceSection = document.querySelector('.inference-rules');
        const confidenceSection = document.querySelector('.confidence-threshold');
        
        if (queryType === 'INFER') {
            inferenceSection.style.display = 'block';
            confidenceSection.style.display = 'block';
        } else {
            inferenceSection.style.display = 'none';
            confidenceSection.style.display = queryType === 'MATCH' ? 'block' : 'none';
        }
    }
    
    validatePattern() {
        const pattern = this.currentQuery.pattern;
        const patternInput = document.getElementById('pattern-input');
        
        // Basic pattern validation
        if (pattern.length > 0) {
            try {
                // Validate HGQL syntax
                this.parsePattern(pattern);
                patternInput.style.borderColor = '#2ecc71';
            } catch (error) {
                patternInput.style.borderColor = '#e74c3c';
            }
        } else {
            patternInput.style.borderColor = '#e0e0e0';
        }
    }
    
    parsePattern(pattern) {
        // Simplified pattern parsing for validation
        if (!pattern.includes('(') && pattern.length > 5) {
            throw new Error('Invalid pattern syntax');
        }
        return true;
    }
    
    async executeQuery() {
        const executeBtn = document.getElementById('execute-query');
        const originalText = executeBtn.textContent;
        
        executeBtn.innerHTML = '<span class="loading"></span> Executing...';
        executeBtn.disabled = true;
        
        try {
            const response = await fetch('/api/execute_query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.currentQuery)
            });
            
            const results = await response.json();
            this.displayResults(results);
            
        } catch (error) {
            console.error('Query execution failed:', error);
            this.displayError(error.message);
        } finally {
            executeBtn.textContent = originalText;
            executeBtn.disabled = false;
        }
    }
    
    displayResults(results) {
        const container = document.getElementById('results-container');
        
        if (results.matches) {
            this.displayMatchResults(results, container);
        } else if (results.inferences) {
            this.displayInferenceResults(results, container);
        } else {
            container.innerHTML = '<div class="result-item">No results found</div>';
        }
    }
    
    displayMatchResults(results, container) {
        let html = `<div class="results-summary">Found ${results.count} matches</div>`;
        
        results.matches.forEach((match, index) => {
            html += `
                <div class="result-item">
                    <div class="result-header">
                        Match ${index + 1}
                        <span class="confidence-badge">${(match.confidence * 100).toFixed(1)}%</span>
                    </div>
                    <div class="result-details">
                        Nodes: ${match.nodes.join(', ')}<br>
                        Edges: ${match.edges.length} connections
                    </div>
                </div>
            `;
        });
        
        container.innerHTML = html;
    }
    
    displayInferenceResults(results, container) {
        let html = `<div class="results-summary">Generated ${results.inferences.length} inferences</div>`;
        
        results.inferences.forEach((inference, index) => {
            html += `
                <div class="result-item">
                    <div class="result-header">
                        Inference ${index + 1}
                        <span class="confidence-badge">${(inference.confidence * 100).toFixed(1)}%</span>
                    </div>
                    <div class="result-details">
                        ${inference.conclusion || 'New knowledge inferred'}
                    </div>
                </div>
            `;
        });
        
        container.innerHTML = html;
    }
    
    displayError(message) {
        const container = document.getElementById('results-container');
        container.innerHTML = `
            <div class="result-item" style="border-left-color: #e74c3c;">
                <strong>Error:</strong> ${message}
            </div>
        `;
    }
    
    newQuery() {
        this.currentQuery = {
            type: 'MATCH',
            pattern: '',
            conditions: [],
            bindings: {},
            rules: [],
            confidence: 0.5
        };
        
        document.getElementById('query-type').value = 'MATCH';
        document.getElementById('pattern-input').value = '';
        document.getElementById('confidence').value = 0.5;
        document.getElementById('confidence-value').textContent = '0.5';
        document.getElementById('results-container').innerHTML = '';
        
        this.updateQueryBuilder();
    }
    
    saveQuery() {
        const queryData = JSON.stringify(this.currentQuery, null, 2);
        const blob = new Blob([queryData], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = `hgql_query_${new Date().toISOString().slice(0, 19)}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
}

// Global functions for dynamic UI elements
function addCondition() {
    const container = document.getElementById('conditions-list');
    const conditionItem = document.createElement('div');
    conditionItem.className = 'condition-item';
    conditionItem.innerHTML = `
        <input type="text" placeholder="Enter condition..." onchange="updateConditions()">
        <button class="remove-btn" onclick="removeCondition(this)">Remove</button>
    `;
    container.appendChild(conditionItem);
}

function removeCondition(button) {
    button.parentElement.remove();
    updateConditions();
}

function addRule() {
    const container = document.getElementById('rules-list');
    const ruleItem = document.createElement('div');
    ruleItem.className = 'rule-item';
    ruleItem.innerHTML = `
        <select onchange="updateRules()">
            <option value="deduction">Deduction</option>
            <option value="induction">Induction</option>
            <option value="abduction">Abduction</option>
            <option value="modus-ponens">Modus Ponens</option>
        </select>
        <button class="remove-btn" onclick="removeRule(this)">Remove</button>
    `;
    container.appendChild(ruleItem);
}

function removeRule(button) {
    button.parentElement.remove();
    updateRules();
}

function updateConditions() {
    // Update conditions in current query
    console.log('Conditions updated');
}

function updateRules() {
    // Update rules in current query
    console.log('Rules updated');
}

function exportResults() {
    const results = document.getElementById('results-container').textContent;
    const blob = new Blob([results], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = `hgql_results_${new Date().toISOString().slice(0, 19)}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function visualizeResults() {
    alert('Results visualization feature coming soon!');
}

// Initialize the query builder when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.hgqlBuilder = new HGQLQueryBuilder();
});
