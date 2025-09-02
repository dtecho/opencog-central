
"""
Statistical Analysis Tools for SkinTwin

Provides comprehensive statistical analysis capabilities for skin modeling data.
"""

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import logging

logger = logging.getLogger(__name__)

class StatisticalAnalyzer:
    """Statistical analysis tools for skin model data"""
    
    def __init__(self):
        self.results = {}
    
    def analyze_molecular_dynamics(self, molecular_data):
        """Analyze molecular dynamics simulation data"""
        if not molecular_data:
            return {}
        
        analysis = {}
        
        # Convert to DataFrame if needed
        if isinstance(molecular_data, list):
            df = pd.DataFrame(molecular_data)
        else:
            df = pd.DataFrame([molecular_data])
        
        # Basic statistics
        analysis['mean_concentrations'] = df.mean().to_dict()
        analysis['std_concentrations'] = df.std().to_dict()
        analysis['variance'] = df.var().to_dict()
        
        # Correlation analysis
        if len(df.columns) > 1:
            analysis['correlation_matrix'] = df.corr().to_dict()
        
        # Time series analysis if time column exists
        if 'time' in df.columns:
            analysis['time_trends'] = self._analyze_time_trends(df)
        
        return analysis
    
    def analyze_cellular_behavior(self, cellular_data):
        """Analyze cellular behavior patterns"""
        if not cellular_data:
            return {}
        
        analysis = {}
        
        # Convert to appropriate format
        if isinstance(cellular_data, list):
            df = pd.DataFrame(cellular_data)
        else:
            df = pd.DataFrame([cellular_data])
        
        # Cell population statistics
        if 'cell_count' in df.columns:
            analysis['population_stats'] = {
                'mean_count': df['cell_count'].mean(),
                'std_count': df['cell_count'].std(),
                'growth_rate': self._calculate_growth_rate(df['cell_count'])
            }
        
        # Viability analysis
        if 'viability' in df.columns:
            analysis['viability_stats'] = {
                'mean_viability': df['viability'].mean(),
                'std_viability': df['viability'].std()
            }
        
        return analysis
    
    def analyze_tissue_properties(self, tissue_data):
        """Analyze tissue-level properties"""
        if not tissue_data:
            return {}
        
        analysis = {}
        
        # Mechanical properties analysis
        if 'elastic_modulus' in tissue_data:
            analysis['mechanical_properties'] = {
                'elastic_modulus': tissue_data['elastic_modulus'],
                'yield_strength': tissue_data.get('yield_strength'),
                'ultimate_strength': tissue_data.get('ultimate_strength')
            }
        
        # Barrier function analysis
        if 'permeability' in tissue_data:
            analysis['barrier_function'] = {
                'permeability': tissue_data['permeability'],
                'selectivity': tissue_data.get('selectivity', 1.0)
            }
        
        return analysis
    
    def analyze_permeation_profile(self, concentrations, time_points=None):
        """Analyze molecular permeation profiles"""
        if not concentrations:
            return {}
        
        conc_array = np.array(concentrations)
        analysis = {}
        
        # Basic permeation statistics
        analysis['peak_concentration'] = np.max(conc_array)
        analysis['peak_time_index'] = np.argmax(conc_array)
        analysis['initial_concentration'] = conc_array[0]
        analysis['final_concentration'] = conc_array[-1]
        
        # Calculate steady-state metrics
        if len(conc_array) > 10:
            steady_state = conc_array[-10:]
            analysis['steady_state_mean'] = np.mean(steady_state)
            analysis['steady_state_std'] = np.std(steady_state)
        
        # Calculate flux if time points provided
        if time_points is not None:
            time_array = np.array(time_points)
            flux = np.gradient(conc_array, time_array)
            analysis['max_flux'] = np.max(flux)
            analysis['mean_flux'] = np.mean(flux)
        
        # Lag time analysis
        threshold = 0.1 * analysis['peak_concentration']
        lag_indices = np.where(conc_array > threshold)[0]
        if len(lag_indices) > 0:
            analysis['lag_time_index'] = lag_indices[0]
        
        return analysis
    
    def perform_pca_analysis(self, data_matrix):
        """Perform Principal Component Analysis"""
        if data_matrix.size == 0:
            return {}
        
        pca = PCA()
        pca_result = pca.fit_transform(data_matrix)
        
        analysis = {
            'explained_variance_ratio': pca.explained_variance_ratio_.tolist(),
            'cumulative_variance': np.cumsum(pca.explained_variance_ratio_).tolist(),
            'components': pca.components_.tolist(),
            'n_components': pca.n_components_
        }
        
        return analysis
    
    def cluster_analysis(self, data_matrix, n_clusters=3):
        """Perform clustering analysis"""
        if data_matrix.size == 0:
            return {}
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(data_matrix)
        
        analysis = {
            'cluster_labels': clusters.tolist(),
            'cluster_centers': kmeans.cluster_centers_.tolist(),
            'inertia': kmeans.inertia_,
            'n_clusters': n_clusters
        }
        
        return analysis
    
    def _analyze_time_trends(self, df):
        """Analyze time series trends in data"""
        trends = {}
        
        time_col = df['time']
        for col in df.columns:
            if col != 'time':
                # Linear regression for trend
                slope, intercept, r_value, p_value, std_err = stats.linregress(time_col, df[col])
                trends[col] = {
                    'slope': slope,
                    'intercept': intercept,
                    'r_squared': r_value**2,
                    'p_value': p_value
                }
        
        return trends
    
    def _calculate_growth_rate(self, cell_counts):
        """Calculate population growth rate"""
        if len(cell_counts) < 2:
            return 0.0
        
        # Simple exponential growth rate calculation
        initial = cell_counts.iloc[0]
        final = cell_counts.iloc[-1]
        time_points = len(cell_counts) - 1
        
        if initial > 0 and final > 0 and time_points > 0:
            growth_rate = (np.log(final) - np.log(initial)) / time_points
            return growth_rate
        
        return 0.0
    
    def generate_summary_report(self, all_data):
        """Generate comprehensive summary report"""
        report = {
            'timestamp': pd.Timestamp.now().isoformat(),
            'data_summary': {},
            'key_findings': [],
            'recommendations': []
        }
        
        # Analyze each data type
        for data_type, data in all_data.items():
            if data_type == 'molecular':
                report['data_summary']['molecular'] = self.analyze_molecular_dynamics(data)
            elif data_type == 'cellular':
                report['data_summary']['cellular'] = self.analyze_cellular_behavior(data)
            elif data_type == 'tissue':
                report['data_summary']['tissue'] = self.analyze_tissue_properties(data)
        
        # Generate key findings
        self._extract_key_findings(report)
        
        return report
    
    def _extract_key_findings(self, report):
        """Extract key findings from analysis results"""
        findings = []
        
        # Check molecular dynamics
        if 'molecular' in report['data_summary']:
            mol_data = report['data_summary']['molecular']
            if 'mean_concentrations' in mol_data:
                findings.append(f"Mean molecular concentrations analyzed across {len(mol_data['mean_concentrations'])} species")
        
        # Check cellular behavior
        if 'cellular' in report['data_summary']:
            cell_data = report['data_summary']['cellular']
            if 'population_stats' in cell_data:
                growth_rate = cell_data['population_stats'].get('growth_rate', 0)
                if growth_rate > 0.1:
                    findings.append("High cellular growth rate detected")
                elif growth_rate < -0.1:
                    findings.append("Cellular population decline observed")
        
        report['key_findings'] = findings
