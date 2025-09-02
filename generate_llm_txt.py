
#!/usr/bin/env python3
"""
Generate optimal llm.txt files for each site folder in 'ref' directory
and create AI-friendly markdown versions under 'llm/sites'
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict

class LLMTxtGenerator:
    def __init__(self):
        self.ref_dir = Path("ref")
        self.llm_dir = Path("llm")
        self.sites_dir = self.llm_dir / "sites"
        
        # File extensions to include in llm.txt
        self.code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx', '.cpp', '.c', '.h', '.hpp',
            '.scm', '.lisp', '.cl', '.rs', '.go', '.java', '.scala', '.kt',
            '.rb', '.php', '.css', '.html', '.xml', '.yaml', '.yml', '.json',
            '.md', '.txt', '.rst', '.toml', '.cfg', '.conf', '.ini'
        }
        
        # Directories to prioritize
        self.priority_dirs = {
            'src', 'lib', 'opencog', 'atomspace', 'examples', 'docs', 
            'scripts', 'tests', 'include', 'api', 'core'
        }
        
        # Files to always include if present
        self.priority_files = {
            'README.md', 'README.txt', 'README', 'INSTALL', 'LICENSE',
            'main.py', 'app.py', 'index.js', 'main.cpp', 'CMakeLists.txt',
            'Cargo.toml', 'package.json', 'setup.py', 'pyproject.toml'
        }

    def create_directories(self):
        """Create necessary directories"""
        self.llm_dir.mkdir(exist_ok=True)
        self.sites_dir.mkdir(exist_ok=True)

    def get_file_importance_score(self, file_path: Path, base_path: Path) -> int:
        """Calculate importance score for a file"""
        score = 0
        rel_path = file_path.relative_to(base_path)
        
        # Priority for certain file names
        if file_path.name in self.priority_files:
            score += 100
        
        # Priority for certain directories
        for part in rel_path.parts[:-1]:  # Exclude filename
            if part.lower() in self.priority_dirs:
                score += 50
        
        # Priority for certain extensions
        if file_path.suffix.lower() in self.code_extensions:
            score += 20
        
        # Penalty for deep nesting
        depth = len(rel_path.parts)
        score -= max(0, (depth - 3) * 5)
        
        # Priority for smaller files (more likely to be important config/docs)
        try:
            size = file_path.stat().st_size
            if size < 10000:  # Files under 10KB
                score += 10
            elif size > 1000000:  # Files over 1MB
                score -= 20
        except:
            pass
        
        return score

    def analyze_repository_structure(self, repo_path: Path) -> Dict:
        """Analyze repository structure and identify key components"""
        analysis = {
            'type': 'unknown',
            'main_language': 'unknown',
            'key_directories': [],
            'key_files': [],
            'description': ''
        }
        
        # Detect repository type
        if (repo_path / 'CMakeLists.txt').exists():
            analysis['type'] = 'cmake'
            analysis['main_language'] = 'cpp'
        elif (repo_path / 'Cargo.toml').exists():
            analysis['type'] = 'rust'
            analysis['main_language'] = 'rust'
        elif (repo_path / 'package.json').exists():
            analysis['type'] = 'nodejs'
            analysis['main_language'] = 'javascript'
        elif (repo_path / 'setup.py').exists() or (repo_path / 'pyproject.toml').exists():
            analysis['type'] = 'python'
            analysis['main_language'] = 'python'
        
        # Find key directories
        for item in repo_path.iterdir():
            if item.is_dir() and item.name.lower() in self.priority_dirs:
                analysis['key_directories'].append(item.name)
        
        # Read description from README if available
        for readme in ['README.md', 'README.txt', 'README']:
            readme_path = repo_path / readme
            if readme_path.exists():
                try:
                    content = readme_path.read_text(encoding='utf-8', errors='ignore')
                    # Extract first paragraph as description
                    lines = content.split('\n')
                    for line in lines:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            analysis['description'] = line[:200] + '...' if len(line) > 200 else line
                            break
                except:
                    pass
                break
        
        return analysis

    def generate_llm_txt_content(self, repo_path: Path) -> str:
        """Generate optimized llm.txt content for a repository"""
        analysis = self.analyze_repository_structure(repo_path)
        
        content = []
        content.append(f"# {repo_path.name}")
        content.append("")
        
        if analysis['description']:
            content.append(f"## Description")
            content.append(analysis['description'])
            content.append("")
        
        content.append(f"## Repository Type: {analysis['type']}")
        content.append(f"## Main Language: {analysis['main_language']}")
        content.append("")
        
        # Collect files with importance scores
        files_with_scores = []
        
        for root, dirs, files in os.walk(repo_path):
            root_path = Path(root)
            
            # Skip hidden directories and common build/cache directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {
                'node_modules', 'build', 'dist', 'target', '__pycache__',
                '.git', '.svn', 'venv', 'env'
            }]
            
            for file in files:
                file_path = root_path / file
                if file.startswith('.'):
                    continue
                
                score = self.get_file_importance_score(file_path, repo_path)
                if score > 0:
                    files_with_scores.append((file_path, score))
        
        # Sort by importance and limit
        files_with_scores.sort(key=lambda x: x[1], reverse=True)
        top_files = files_with_scores[:100]  # Limit to top 100 files
        
        # Group files by category
        categories = defaultdict(list)
        for file_path, score in top_files:
            rel_path = file_path.relative_to(repo_path)
            
            if file_path.name in self.priority_files:
                categories['Core Files'].append(str(rel_path))
            elif any(part in self.priority_dirs for part in rel_path.parts[:-1]):
                parent_dir = next((part for part in rel_path.parts[:-1] if part in self.priority_dirs), rel_path.parts[0])
                categories[f"{parent_dir.title()} Files"].append(str(rel_path))
            else:
                categories['Other Files'].append(str(rel_path))
        
        # Add categorized file listings
        for category, file_list in categories.items():
            if file_list:
                content.append(f"## {category}")
                for file_path in sorted(file_list):
                    content.append(f"- {file_path}")
                content.append("")
        
        # Add file patterns to include
        content.append("## Include Patterns")
        content.append("- *.py")
        content.append("- *.cpp")
        content.append("- *.h")
        content.append("- *.scm")
        content.append("- *.js")
        content.append("- *.md")
        content.append("- CMakeLists.txt")
        content.append("- Cargo.toml")
        content.append("- package.json")
        content.append("")
        
        # Add exclude patterns
        content.append("## Exclude Patterns")
        content.append("- .git/")
        content.append("- node_modules/")
        content.append("- build/")
        content.append("- target/")
        content.append("- __pycache__/")
        content.append("- *.pyc")
        content.append("- *.o")
        content.append("- *.so")
        content.append("- *.dll")
        content.append("")
        
        return '\n'.join(content)

    def create_ai_friendly_markdown(self, repo_path: Path, llm_txt_content: str) -> str:
        """Create AI-friendly markdown version of the repository"""
        markdown_content = []
        
        # Header
        markdown_content.append(f"# {repo_path.name} - AI-Friendly Documentation")
        markdown_content.append("")
        markdown_content.append("Generated from repository structure and key files.")
        markdown_content.append("")
        
        # Include the llm.txt content
        markdown_content.append("## Repository Overview")
        markdown_content.append("```")
        markdown_content.append(llm_txt_content)
        markdown_content.append("```")
        markdown_content.append("")
        
        # Extract and include key file contents
        key_files_to_include = []
        
        # Always include README files
        for readme in ['README.md', 'README.txt', 'README']:
            readme_path = repo_path / readme
            if readme_path.exists():
                key_files_to_include.append(readme_path)
                break
        
        # Include main configuration files
        for config_file in ['CMakeLists.txt', 'Cargo.toml', 'package.json', 'setup.py', 'pyproject.toml']:
            config_path = repo_path / config_file
            if config_path.exists():
                key_files_to_include.append(config_path)
        
        # Include main source files
        main_files = ['main.py', 'app.py', 'index.js', 'main.cpp', 'lib.rs']
        for main_file in main_files:
            main_path = repo_path / main_file
            if main_path.exists():
                key_files_to_include.append(main_path)
        
        # Add key file contents
        for file_path in key_files_to_include:
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                rel_path = file_path.relative_to(repo_path)
                
                markdown_content.append(f"## {rel_path}")
                markdown_content.append("")
                
                # Determine file type for syntax highlighting
                if file_path.suffix in ['.py']:
                    lang = 'python'
                elif file_path.suffix in ['.js', '.ts']:
                    lang = 'javascript'
                elif file_path.suffix in ['.cpp', '.c', '.h', '.hpp']:
                    lang = 'cpp'
                elif file_path.suffix in ['.rs']:
                    lang = 'rust'
                elif file_path.suffix in ['.scm', '.lisp']:
                    lang = 'lisp'
                elif file_path.suffix in ['.json']:
                    lang = 'json'
                elif file_path.suffix in ['.yaml', '.yml']:
                    lang = 'yaml'
                elif file_path.suffix in ['.toml']:
                    lang = 'toml'
                elif file_path.suffix in ['.md']:
                    lang = 'markdown'
                else:
                    lang = ''
                
                markdown_content.append(f"```{lang}")
                # Limit content length to avoid huge files
                if len(content) > 10000:
                    content = content[:10000] + "\n... (truncated)"
                markdown_content.append(content)
                markdown_content.append("```")
                markdown_content.append("")
                
            except Exception as e:
                markdown_content.append(f"Error reading {rel_path}: {e}")
                markdown_content.append("")
        
        return '\n'.join(markdown_content)

    def process_all_sites(self):
        """Process all site folders in ref directory"""
        if not self.ref_dir.exists():
            print(f"Reference directory '{self.ref_dir}' not found")
            return
        
        self.create_directories()
        
        processed_count = 0
        
        for site_path in self.ref_dir.iterdir():
            if site_path.is_dir():
                print(f"Processing {site_path.name}...")
                
                try:
                    # Generate llm.txt content
                    llm_txt_content = self.generate_llm_txt_content(site_path)
                    
                    # Write llm.txt file
                    llm_txt_path = site_path / "llm.txt"
                    llm_txt_path.write_text(llm_txt_content, encoding='utf-8')
                    
                    # Create AI-friendly markdown
                    markdown_content = self.create_ai_friendly_markdown(site_path, llm_txt_content)
                    
                    # Write markdown file
                    markdown_path = self.sites_dir / f"{site_path.name}.md"
                    markdown_path.write_text(markdown_content, encoding='utf-8')
                    
                    processed_count += 1
                    print(f"✓ Generated llm.txt and markdown for {site_path.name}")
                    
                except Exception as e:
                    print(f"✗ Error processing {site_path.name}: {e}")
        
        print(f"\nProcessed {processed_count} sites")
        print(f"llm.txt files generated in individual site directories")
        print(f"AI-friendly markdown files generated in {self.sites_dir}")

    def generate_master_index(self):
        """Generate a master index of all processed sites"""
        index_content = []
        index_content.append("# OpenCog Ecosystem - Master Index")
        index_content.append("")
        index_content.append("Auto-generated index of all OpenCog-related repositories and projects.")
        index_content.append("")
        
        # Group by category based on naming patterns
        categories = defaultdict(list)
        
        for site_path in self.ref_dir.iterdir():
            if site_path.is_dir():
                site_name = site_path.name
                
                if 'atomspace' in site_name.lower():
                    categories['AtomSpace'].append(site_name)
                elif any(term in site_name.lower() for term in ['learn', 'language', 'nlp']):
                    categories['Language Learning'].append(site_name)
                elif any(term in site_name.lower() for term in ['vision', 'perception', 'sensory']):
                    categories['Perception'].append(site_name)
                elif any(term in site_name.lower() for term in ['robot', 'embodiment', 'ros']):
                    categories['Robotics'].append(site_name)
                elif any(term in site_name.lower() for term in ['bio', 'chem', 'medical']):
                    categories['Bioinformatics'].append(site_name)
                elif any(term in site_name.lower() for term in ['moses', 'pln', 'reason']):
                    categories['Reasoning'].append(site_name)
                elif any(term in site_name.lower() for term in ['cogserver', 'network', 'api']):
                    categories['Infrastructure'].append(site_name)
                else:
                    categories['General'].append(site_name)
        
        for category, sites in sorted(categories.items()):
            if sites:
                index_content.append(f"## {category}")
                index_content.append("")
                for site in sorted(sites):
                    index_content.append(f"- [{site}](sites/{site}.md)")
                index_content.append("")
        
        # Write master index
        index_path = self.llm_dir / "index.md"
        index_path.write_text('\n'.join(index_content), encoding='utf-8')
        print(f"Generated master index at {index_path}")

def main():
    generator = LLMTxtGenerator()
    generator.process_all_sites()
    generator.generate_master_index()

if __name__ == "__main__":
    main()
