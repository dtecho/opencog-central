
"""
Data Export Tools for SkinTwin

Provides comprehensive data export capabilities for analysis and archival.
"""

import json
import csv
import pandas as pd
import numpy as np
from pathlib import Path
import logging
import h5py
import pickle

logger = logging.getLogger(__name__)

class DataExporter:
    """Data export tools for skin model results"""
    
    def __init__(self, output_dir="output/data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def export_to_json(self, data, filename):
        """Export data to JSON format"""
        output_path = self.output_dir / f"{filename}.json"
        
        try:
            # Convert numpy arrays to lists for JSON serialization
            json_data = self._convert_for_json(data)
            
            with open(output_path, 'w') as f:
                json.dump(json_data, f, indent=2, default=str)
            
            logger.info(f"Data exported to {output_path}")
            return str(output_path)
        
        except Exception as e:
            logger.error(f"Failed to export JSON: {e}")
            return None
    
    def export_to_csv(self, data, filename):
        """Export tabular data to CSV format"""
        output_path = self.output_dir / f"{filename}.csv"
        
        try:
            if isinstance(data, dict):
                # Convert dict to DataFrame
                df = pd.DataFrame([data])
            elif isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                df = pd.DataFrame(data)
            
            df.to_csv(output_path, index=False)
            logger.info(f"Data exported to {output_path}")
            return str(output_path)
        
        except Exception as e:
            logger.error(f"Failed to export CSV: {e}")
            return None
    
    def export_to_hdf5(self, data, filename):
        """Export large datasets to HDF5 format"""
        output_path = self.output_dir / f"{filename}.h5"
        
        try:
            with h5py.File(output_path, 'w') as f:
                self._write_hdf5_group(f, '', data)
            
            logger.info(f"Data exported to {output_path}")
            return str(output_path)
        
        except Exception as e:
            logger.error(f"Failed to export HDF5: {e}")
            return None
    
    def export_simulation_results(self, results, experiment_name):
        """Export complete simulation results in multiple formats"""
        exports = {}
        
        # JSON export for metadata and small datasets
        json_path = self.export_to_json(results, f"{experiment_name}_results")
        if json_path:
            exports['json'] = json_path
        
        # CSV export for time series data
        if 'time_points' in results:
            time_series_data = {
                'time': results['time_points']
            }
            
            # Add molecular data if available
            if results.get('molecular_data'):
                for i, mol_data in enumerate(results['molecular_data']):
                    time_series_data[f'molecular_components_{i}'] = mol_data.get('component_count', 0)
            
            # Add cellular data if available
            if results.get('cellular_data'):
                for i, cell_data in enumerate(results['cellular_data']):
                    time_series_data[f'cellular_components_{i}'] = cell_data.get('component_count', 0)
            
            csv_path = self.export_to_csv(time_series_data, f"{experiment_name}_timeseries")
            if csv_path:
                exports['csv'] = csv_path
        
        # HDF5 export for large datasets
        if self._is_large_dataset(results):
            hdf5_path = self.export_to_hdf5(results, f"{experiment_name}_large")
            if hdf5_path:
                exports['hdf5'] = hdf5_path
        
        return exports
    
    def export_atomspace_state(self, atomspace_manager, filename):
        """Export AtomSpace state for analysis"""
        output_path = self.output_dir / f"{filename}_atomspace.scm"
        
        try:
            # Export in Scheme format (OpenCog standard)
            atomspace_manager.export_atomspace(str(output_path))
            logger.info(f"AtomSpace state exported to {output_path}")
            return str(output_path)
        
        except Exception as e:
            logger.error(f"Failed to export AtomSpace: {e}")
            return None
    
    def export_model_parameters(self, model_params, filename):
        """Export model parameters and configuration"""
        output_path = self.output_dir / f"{filename}_params.json"
        
        try:
            with open(output_path, 'w') as f:
                json.dump(model_params, f, indent=2, default=str)
            
            logger.info(f"Model parameters exported to {output_path}")
            return str(output_path)
        
        except Exception as e:
            logger.error(f"Failed to export parameters: {e}")
            return None
    
    def create_analysis_report(self, analysis_results, filename):
        """Create comprehensive analysis report"""
        output_path = self.output_dir / f"{filename}_report.html"
        
        try:
            html_content = self._generate_html_report(analysis_results)
            
            with open(output_path, 'w') as f:
                f.write(html_content)
            
            logger.info(f"Analysis report created at {output_path}")
            return str(output_path)
        
        except Exception as e:
            logger.error(f"Failed to create report: {e}")
            return None
    
    def _convert_for_json(self, obj):
        """Convert numpy arrays and other objects for JSON serialization"""
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {key: self._convert_for_json(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self._convert_for_json(item) for item in obj]
        elif isinstance(obj, (np.integer, np.floating)):
            return obj.item()
        else:
            return obj
    
    def _write_hdf5_group(self, group, prefix, data):
        """Recursively write data to HDF5 group"""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    subgroup = group.create_group(key)
                    self._write_hdf5_group(subgroup, f"{prefix}/{key}", value)
                else:
                    try:
                        group.create_dataset(key, data=value)
                    except:
                        # Handle non-numeric data as strings
                        group.create_dataset(key, data=str(value))
        
        elif isinstance(data, list):
            try:
                # Try to create dataset from list
                group.create_dataset('data', data=np.array(data))
            except:
                # Handle mixed-type lists
                for i, item in enumerate(data):
                    self._write_hdf5_group(group, f"{prefix}/{i}", {f"item_{i}": item})
    
    def _is_large_dataset(self, data):
        """Check if dataset is large enough to warrant HDF5 export"""
        def count_elements(obj):
            if isinstance(obj, dict):
                return sum(count_elements(v) for v in obj.values())
            elif isinstance(obj, list):
                return len(obj) + sum(count_elements(item) for item in obj if isinstance(item, (dict, list)))
            else:
                return 1
        
        return count_elements(data) > 1000
    
    def _generate_html_report(self, analysis_results):
        """Generate HTML report from analysis results"""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>SkinTwin Analysis Report</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .header { background-color: #f0f0f0; padding: 20px; border-radius: 5px; }
                .section { margin: 20px 0; padding: 15px; border: 1px solid #ddd; }
                .metric { margin: 10px 0; }
                .value { font-weight: bold; color: #2c3e50; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>SkinTwin Analysis Report</h1>
                <p>Generated on: {timestamp}</p>
            </div>
        """.format(timestamp=pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        # Add analysis sections
        for section_name, section_data in analysis_results.items():
            html += f'<div class="section"><h2>{section_name.title()}</h2>'
            
            if isinstance(section_data, dict):
                for key, value in section_data.items():
                    html += f'<div class="metric">{key}: <span class="value">{value}</span></div>'
            else:
                html += f'<div class="metric">{section_data}</div>'
            
            html += '</div>'
        
        html += """
        </body>
        </html>
        """
        
        return html
