{**
 * templates/management/agents.tpl
 *
 * Copyright (c) 2014-2021 Simon Fraser University
 * Copyright (c) 2003-2021 John Willinsky
 * Distributed under the GNU GPL v3. For full terms see the file docs/COPYING.
 *
 * Agent management interface template
 *}
{extends file="layouts/backend.tpl"}

{block name="page"}
	<div id="agents">
		{if !$pluginEnabled}
			<div class="pkp_notification_error">
				{if $errorMessage}
					{$errorMessage}
				{else}
					{translate key="plugins.generic.skzAgents.management.notEnabled"}
				{/if}
				<p>
					<a href="{url router=$smarty.const.ROUTE_PAGE page="management" op="settings" path="website"}">
						{translate key="plugins.generic.skzAgents.management.enablePlugin"}
					</a>
				</p>
			</div>
		{else}
			<div class="agent-dashboard">
				<h1>{translate key="plugins.generic.skzAgents.management.title"}</h1>
				
				{if $errorMessage}
					<div class="pkp_notification_error">
						{$errorMessage}
					</div>
				{/if}

				<div class="agent-overview">
					<div class="agent-stats">
						<div class="stat-card">
							<h3>{translate key="plugins.generic.skzAgents.management.totalAgents"}</h3>
							<span class="stat-number" id="total-agents">7</span>
						</div>
						<div class="stat-card">
							<h3>{translate key="plugins.generic.skzAgents.management.activeAgents"}</h3>
							<span class="stat-number" id="active-agents">0</span>
						</div>
						<div class="stat-card">
							<h3>{translate key="plugins.generic.skzAgents.management.tasksCompleted"}</h3>
							<span class="stat-number" id="tasks-completed">0</span>
						</div>
					</div>
				</div>

				<div class="agent-controls">
					<div class="control-buttons">
						<button type="button" class="pkp_button pkp_button_primary" id="start-all-agents">
							{translate key="plugins.generic.skzAgents.management.startAll"}
						</button>
						<button type="button" class="pkp_button pkp_button_secondary" id="stop-all-agents">
							{translate key="plugins.generic.skzAgents.management.stopAll"}
						</button>
						<button type="button" class="pkp_button pkp_button_secondary" id="refresh-status">
							{translate key="plugins.generic.skzAgents.management.refreshStatus"}
						</button>
					</div>
				</div>

				<div class="agents-list">
					<h2>{translate key="plugins.generic.skzAgents.management.agentsList"}</h2>
					<div class="agents-grid" id="agents-grid">
						{if $agentStatus}
							{foreach from=$agentStatus key="agentId" item="agent"}
								<div class="agent-card" data-agent-id="{$agentId}">
									<div class="agent-header">
										<h3>{$agent.name}</h3>
										<span class="agent-status-indicator status-unknown" id="status-{$agentId}">
											{translate key="plugins.generic.skzAgents.management.status.unknown"}
										</span>
									</div>
									<div class="agent-details">
										<p class="agent-id">{translate key="plugins.generic.skzAgents.management.agentId"}: {$agentId}</p>
										<p class="agent-tasks">
											{translate key="plugins.generic.skzAgents.management.processedTasks"}: 
											<span id="tasks-{$agentId}">0</span>
										</p>
										<p class="agent-activity">
											{translate key="plugins.generic.skzAgents.management.lastActivity"}: 
											<span id="activity-{$agentId}">-</span>
										</p>
									</div>
									<div class="agent-actions">
										<button type="button" class="pkp_button pkp_button_primary start-agent" 
											data-agent-id="{$agentId}">
											{translate key="plugins.generic.skzAgents.management.start"}
										</button>
										<button type="button" class="pkp_button pkp_button_secondary stop-agent" 
											data-agent-id="{$agentId}">
											{translate key="plugins.generic.skzAgents.management.stop"}
										</button>
										<button type="button" class="pkp_button pkp_button_secondary configure-agent" 
											data-agent-id="{$agentId}">
											{translate key="plugins.generic.skzAgents.management.configure"}
										</button>
									</div>
								</div>
							{/foreach}
						{else}
							<p>{translate key="plugins.generic.skzAgents.management.noAgents"}</p>
						{/if}
					</div>
				</div>

				<div class="agent-logs">
					<h2>{translate key="plugins.generic.skzAgents.management.recentActivity"}</h2>
					<div class="log-container" id="agent-logs">
						<p class="loading">{translate key="plugins.generic.skzAgents.management.loadingLogs"}</p>
					</div>
				</div>
			</div>
		{/if}
	</div>

	{if $pluginEnabled}
		<script type="text/javascript">
			// Agent management JavaScript
			$(document).ready(function() {
				var agentManager = {
					apiBaseUrl: '{$apiBaseUrl|escape:javascript}',
					refreshInterval: null,

					init: function() {
						this.bindEvents();
						this.refreshStatus();
						this.startAutoRefresh();
					},

					bindEvents: function() {
						$('#start-all-agents').click(function() {
							agentManager.startAllAgents();
						});

						$('#stop-all-agents').click(function() {
							agentManager.stopAllAgents();
						});

						$('#refresh-status').click(function() {
							agentManager.refreshStatus();
						});

						$('.start-agent').click(function() {
							var agentId = $(this).data('agent-id');
							agentManager.startAgent(agentId);
						});

						$('.stop-agent').click(function() {
							var agentId = $(this).data('agent-id');
							agentManager.stopAgent(agentId);
						});

						$('.configure-agent').click(function() {
							var agentId = $(this).data('agent-id');
							agentManager.configureAgent(agentId);
						});
					},

					startAgent: function(agentId) {
						this.apiCall('POST', '/startAgent', {ldelim}agentId: agentId{rdelim}, function(response) {
							if (response.success) {
								agentManager.showNotification('Agent started successfully', 'success');
								agentManager.refreshStatus();
							} else {
								agentManager.showNotification('Failed to start agent: ' + response.error, 'error');
							}
						});
					},

					stopAgent: function(agentId) {
						this.apiCall('POST', '/stopAgent', {ldelim}agentId: agentId{rdelim}, function(response) {
							if (response.success) {
								agentManager.showNotification('Agent stopped successfully', 'success');
								agentManager.refreshStatus();
							} else {
								agentManager.showNotification('Failed to stop agent: ' + response.error, 'error');
							}
						});
					},

					startAllAgents: function() {
						$('.agent-card').each(function() {
							var agentId = $(this).data('agent-id');
							agentManager.startAgent(agentId);
						});
					},

					stopAllAgents: function() {
						$('.agent-card').each(function() {
							var agentId = $(this).data('agent-id');
							agentManager.stopAgent(agentId);
						});
					},

					refreshStatus: function() {
						this.apiCall('GET', '/getStatus', null, function(response) {
							if (response.success) {
								agentManager.updateAgentStatus(response.data);
							}
						});
					},

					updateAgentStatus: function(statusData) {
						var activeCount = 0;
						var totalTasks = 0;

						$.each(statusData, function(agentId, status) {
							$('#status-' + agentId)
								.removeClass('status-unknown status-running status-stopped')
								.addClass('status-' + status.status)
								.text(status.status);

							$('#tasks-' + agentId).text(status.processedTasks || 0);
							$('#activity-' + agentId).text(status.lastActivity || '-');

							if (status.status === 'running') {
								activeCount++;
							}
							totalTasks += (status.processedTasks || 0);
						});

						$('#active-agents').text(activeCount);
						$('#tasks-completed').text(totalTasks);
					},

					configureAgent: function(agentId) {
						// Open configuration modal or redirect to configuration page
						window.open(this.apiBaseUrl + '/configure?agentId=' + agentId, '_blank');
					},

					apiCall: function(method, endpoint, data, callback) {
						$.ajax({
							url: this.apiBaseUrl + endpoint,
							method: method,
							data: data,
							dataType: 'json',
							success: callback,
							error: function() {
								agentManager.showNotification('API call failed', 'error');
							}
						});
					},

					showNotification: function(message, type) {
						// Create notification element
						var notification = $('<div class="pkp_notification pkp_notification_' + type + '">' + message + '</div>');
						$('#agents').prepend(notification);
						
						// Auto-remove after 5 seconds
						setTimeout(function() {
							notification.fadeOut(function() {
								$(this).remove();
							});
						}, 5000);
					},

					startAutoRefresh: function() {
						this.refreshInterval = setInterval(function() {
							agentManager.refreshStatus();
						}, 30000); // Refresh every 30 seconds
					}
				};

				agentManager.init();
			});
		</script>

		<style>
			.agent-dashboard {
				max-width: 1200px;
				margin: 0 auto;
			}

			.agent-overview {
				margin-bottom: 2em;
			}

			.agent-stats {
				display: flex;
				gap: 1em;
				margin-bottom: 2em;
			}

			.stat-card {
				background: #f8f9fa;
				border: 1px solid #dee2e6;
				border-radius: 8px;
				padding: 1em;
				text-align: center;
				flex: 1;
			}

			.stat-card h3 {
				margin: 0 0 0.5em 0;
				font-size: 0.9em;
				color: #6c757d;
				text-transform: uppercase;
				font-weight: 600;
			}

			.stat-number {
				font-size: 2em;
				font-weight: bold;
				color: #007bff;
			}

			.agent-controls {
				margin-bottom: 2em;
			}

			.control-buttons {
				display: flex;
				gap: 0.5em;
			}

			.agents-grid {
				display: grid;
				grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
				gap: 1em;
			}

			.agent-card {
				border: 1px solid #dee2e6;
				border-radius: 8px;
				padding: 1em;
				background: #fff;
			}

			.agent-header {
				display: flex;
				justify-content: space-between;
				align-items: center;
				margin-bottom: 1em;
			}

			.agent-header h3 {
				margin: 0;
				font-size: 1.1em;
			}

			.agent-status-indicator {
				padding: 0.25em 0.5em;
				border-radius: 4px;
				font-size: 0.8em;
				font-weight: bold;
				text-transform: uppercase;
			}

			.status-unknown {
				background-color: #6c757d;
				color: white;
			}

			.status-running {
				background-color: #28a745;
				color: white;
			}

			.status-stopped {
				background-color: #dc3545;
				color: white;
			}

			.agent-details {
				margin-bottom: 1em;
			}

			.agent-details p {
				margin: 0.25em 0;
				font-size: 0.9em;
				color: #6c757d;
			}

			.agent-actions {
				display: flex;
				gap: 0.5em;
				flex-wrap: wrap;
			}

			.agent-actions button {
				flex: 1;
				min-width: 80px;
			}

			.agent-logs {
				margin-top: 2em;
				padding-top: 2em;
				border-top: 1px solid #dee2e6;
			}

			.log-container {
				background: #f8f9fa;
				border: 1px solid #dee2e6;
				border-radius: 4px;
				padding: 1em;
				height: 200px;
				overflow-y: auto;
				font-family: monospace;
				font-size: 0.9em;
			}

			@media (max-width: 768px) {
				.agent-stats {
					flex-direction: column;
				}

				.control-buttons {
					flex-direction: column;
				}

				.agents-grid {
					grid-template-columns: 1fr;
				}
			}
		</style>
	{/if}
{/block}