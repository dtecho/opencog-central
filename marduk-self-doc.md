// =========================================================
// MARDUK'S SELF-DOCUMENTING CODE SYSTEM
// A recursive code analysis and documentation generator
// =========================================================

const fs = require('fs');
const path = require('path');
const chalk = require('chalk');

// Configuration - adjust recursive depth and patterns
const CONFIG = {
  recursionDepth: 2,
  targetExtensions: ['.js', '.ts', '.jsx', '.tsx'],
  ignoreFolders: ['node_modules', '.git', 'dist', 'build'],
  patternWeights: {
    functionPattern: 3,
    classPattern: 4,
    commentPattern: 1,
    complexityPattern: 2
  }
};

// ANSI color codes for terminal output
const colors = {
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m',
  white: '\x1b[37m',
  reset: '\x1b[0m'
};

// Print section header
function printSection(title) {
  console.log('\n' + '='.repeat(50));
  console.log(`${colors.cyan}${title}${colors.reset}`);
  console.log('='.repeat(50) + '\n');
}

// Pattern detection algorithms
const patternDetectors = {
  // Detect functions without documentation
  detectUndocumentedFunctions(code) {
    const functionRegex = /function\s+(\w+)\s*\([^)]*\)\s*\{(?!\s*\/\*\*)/g;
    const arrowFunctionRegex = /const\s+(\w+)\s*=\s*(?:\([^)]*\)|[^=]*)\s*=>\s*\{(?!\s*\/\*\*)/g;

    const functions = [...code.matchAll(functionRegex)].map(match => match[1]);
    const arrowFunctions = [...code.matchAll(arrowFunctionRegex)].map(match => match[1]);

    return [...functions, ...arrowFunctions];
  },

  // Detect classes without documentation
  detectUndocumentedClasses(code) {
    const classRegex = /class\s+(\w+)(?:\s+extends\s+\w+)?\s*\{(?!\s*\/\*\*)/g;
    return [...code.matchAll(classRegex)].map(match => match[1]);
  },

  // Detect code complexity markers (nested loops, conditionals)
  detectComplexPatterns(code) {
    const nestedLoopsRegex = /for\s*\([^{]*\{[^}]*for\s*\([^{]*\{/g;
    const nestedConditionalsRegex = /if\s*\([^{]*\{[^}]*if\s*\([^{]*\{/g;

    const nestedLoops = (code.match(nestedLoopsRegex) || []).length;
    const nestedConditionals = (code.match(nestedConditionalsRegex) || []).length;

    return {
      nestedLoops,
      nestedConditionals,
      complexity: nestedLoops * 2 + nestedConditionals
    };
  }
};

// Documentation generators
const documentationGenerators = {
  // Generate function documentation
  generateFunctionDocs(functionName, fileContent) {
    // Extract function body and parameters through regex
    const functionRegex = new RegExp(`function\\s+${functionName}\\s*\\(([^)]*)\\)\\s*\\{([^}]*?)\\}`, 's');
    const arrowFunctionRegex = new RegExp(`const\\s+${functionName}\\s*=\\s*(?:\\(([^)]*)\\)|([^=]*))\\s*=>\\s*\\{([^}]*?)\\}`, 's');

    let params = [];
    let functionBody = '';

    const functionMatch = fileContent.match(functionRegex);
    const arrowMatch = fileContent.match(arrowFunctionRegex);

    if (functionMatch) {
      params = functionMatch[1].split(',').map(p => p.trim());
      functionBody = functionMatch[2];
    } else if (arrowMatch) {
      params = (arrowMatch[1] || arrowMatch[2] || '').split(',').map(p => p.trim());
      functionBody = arrowMatch[3];
    }

    // Analyze function purpose
    const purpose = this.inferPurpose(functionName, functionBody);

    // Generate JSDoc style comment
    return `/**
 * ${purpose}
 *${params.map(p => `\n * @param {any} ${p} - Parameter description`).join('')}
 * @returns {any} Return value description
 */`;
  },

  // Generate class documentation
  generateClassDocs(className, fileContent) {
    // Extract class definition
    const classRegex = new RegExp(`class\\s+${className}(?:\\s+extends\\s+(\\w+))?\\s*\\{([^}]*?)\\}`, 's');
    const match = fileContent.match(classRegex);

    if (!match) return `/**\n * Class ${className}\n */`;

    const extendsClass = match[1] ? ` Extends ${match[1]}.` : '';
    const classBody = match[2];

    // Extract methods
    const methodRegex = /(\w+)\s*\([^)]*\)\s*\{/g;
    const methods = [...classBody.matchAll(methodRegex)].map(m => m[1]);

    return `/**
 * Class ${className}.${extendsClass}
 *${methods.map(m => `\n * @method ${m} - Method description`).join('')}
 */`;
  },

  // Infer purpose from function name and body
  inferPurpose(name, body) {
    // Handle common prefixes
    if (name.startsWith('get')) {
      return `Retrieves ${name.substring(3)}`;
    } else if (name.startsWith('set')) {
      return `Sets ${name.substring(3)}`;
    } else if (name.startsWith('is')) {
      return `Checks if ${name.substring(2)}`;
    } else if (name.startsWith('has')) {
      return `Determines if ${name.substring(3)} exists`;
    }

    // Look for common patterns in the function body
    if (body.includes('return') && body.includes('filter')) {
      return `Filters data based on specific criteria`;
    } else if (body.includes('return') && body.includes('map')) {
      return `Transforms data using a mapping function`;
    } else if (body.includes('fetch') || body.includes('axios')) {
      return `Fetches data from an external source`;
    }

    return `The ${name} function`;
  }
};

// Analyze a file and generate documentation
function analyzeFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const fileName = path.basename(filePath);

    console.log(`${colors.green}Analyzing ${fileName}...${colors.reset}`);

    // Detect patterns
    const undocumentedFunctions = patternDetectors.detectUndocumentedFunctions(content);
    const undocumentedClasses = patternDetectors.detectUndocumentedClasses(content);
    const complexityMetrics = patternDetectors.detectComplexPatterns(content);

    // Generate documentation suggestions
    const suggestions = [];

    undocumentedFunctions.forEach(func => {
      const docs = documentationGenerators.generateFunctionDocs(func, content);
      suggestions.push({
        type: 'function',
        name: func,
        documentation: docs
      });
    });

    undocumentedClasses.forEach(cls => {
      const docs = documentationGenerators.generateClassDocs(cls, content);
      suggestions.push({
        type: 'class',
        name: cls,
        documentation: docs
      });
    });

    return {
      filePath,
      fileName,
      metrics: {
        undocumentedFunctions: undocumentedFunctions.length,
        undocumentedClasses: undocumentedClasses.length,
        complexity: complexityMetrics.complexity
      },
      suggestions
    };
  } catch (error) {
    console.error(`Error analyzing ${filePath}:`, error.message);
    return null;
  }
}

// Process a directory recursively
function processDirectory(dir, depth = 0) {
  if (depth > CONFIG.recursionDepth) return [];

  let results = [];

  try {
    const files = fs.readdirSync(dir);

    for (const file of files) {
      const filePath = path.join(dir, file);
      const stats = fs.statSync(filePath);

      if (stats.isDirectory()) {
        if (!CONFIG.ignoreFolders.includes(file)) {
          results = results.concat(processDirectory(filePath, depth + 1));
        }
      } else {
        const ext = path.extname(file);
        if (CONFIG.targetExtensions.includes(ext)) {
          const analysis = analyzeFile(filePath);
          if (analysis) results.push(analysis);
        }
      }
    }
  } catch (error) {
    console.error(`Error processing directory ${dir}:`, error.message);
  }

  return results;
}

// Apply documentation to a file
function applyDocumentation(filePath, suggestions) {
  try {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;

    // Sort suggestions by their position in the file (to avoid offset issues)
    suggestions.sort((a, b) => {
      const posA = content.indexOf(`function ${a.name}`) !== -1
        ? content.indexOf(`function ${a.name}`)
        : content.indexOf(`const ${a.name} =`);

      const posB = content.indexOf(`function ${b.name}`) !== -1
        ? content.indexOf(`function ${b.name}`)
        : content.indexOf(`const ${b.name} =`);

      return posA - posB;
    });

    // Apply each suggestion
    for (const suggestion of suggestions) {
      let regex;
      if (suggestion.type === 'function') {
        // Match both regular and arrow functions
        regex = new RegExp(`(function\\s+${suggestion.name}|const\\s+${suggestion.name}\\s*=\\s*(?:\\([^)]*\\)|[^=]*)\\s*=>)`, 'g');
      } else if (suggestion.type === 'class') {
        regex = new RegExp(`(class\\s+${suggestion.name})`, 'g');
      }

      if (regex) {
        // Add documentation before the matched pattern
        content = content.replace(regex, `${suggestion.documentation}\n$1`);
        modified = true;
      }
    }

    if (modified) {
      // Create a backup
      fs.writeFileSync(`${filePath}.bak`, fs.readFileSync(filePath));
      // Write the updated content
      fs.writeFileSync(filePath, content);
      console.log(`${colors.green}Updated documentation in ${filePath}${colors.reset}`);
      return true;
    }

    return false;
  } catch (error) {
    console.error(`Error applying documentation to ${filePath}:`, error.message);
    return false;
  }
}

// Generate a documentation report
function generateReport(results) {
  printSection("DOCUMENTATION ANALYSIS REPORT");

  // Summary statistics
  const totalFiles = results.length;
  const totalUndocumentedFunctions = results.reduce((sum, r) => sum + r.metrics.undocumentedFunctions, 0);
  const totalUndocumentedClasses = results.reduce((sum, r) => sum + r.metrics.undocumentedClasses, 0);
  const avgComplexity = results.reduce((sum, r) => sum + r.metrics.complexity, 0) / totalFiles || 0;

  console.log(`${colors.yellow}Files analyzed:${colors.reset} ${totalFiles}`);
  console.log(`${colors.yellow}Undocumented functions:${colors.reset} ${totalUndocumentedFunctions}`);
  console.log(`${colors.yellow}Undocumented classes:${colors.reset} ${totalUndocumentedClasses}`);
  console.log(`${colors.yellow}Average code complexity:${colors.reset} ${avgComplexity.toFixed(2)}`);

  // Files with highest documentation needs
  const topNeedsDocs = [...results]
    .sort((a, b) => {
      const scoreA = a.metrics.undocumentedFunctions * 2 + a.metrics.undocumentedClasses * 3;
      const scoreB = b.metrics.undocumentedFunctions * 2 + b.metrics.undocumentedClasses * 3;
      return scoreB - scoreA;
    })
    .slice(0, 5);

  console.log(`\n${colors.magenta}Top 5 files needing documentation:${colors.reset}`);

  topNeedsDocs.forEach((file, i) => {
    const total = file.metrics.undocumentedFunctions + file.metrics.undocumentedClasses;
    console.log(`${i+1}. ${file.fileName} (${total} items)`);
  });

  // Files with highest complexity
  const topComplexity = [...results]
    .sort((a, b) => b.metrics.complexity - a.metrics.complexity)
    .slice(0, 5);

  console.log(`\n${colors.magenta}Top 5 files by complexity:${colors.reset}`);

  topComplexity.forEach((file, i) => {
    console.log(`${i+1}. ${file.fileName} (complexity: ${file.metrics.complexity})`);
  });
}

// Main function
async function main() {
  printSection("MARDUK'S SELF-DOCUMENTING CODE SYSTEM");

  console.log(`${colors.green}Initializing documentation analysis...${colors.reset}`);
  console.log(`${colors.blue}Recursion depth:${colors.reset} ${CONFIG.recursionDepth}`);
  console.log(`${colors.blue}Target extensions:${colors.reset} ${CONFIG.targetExtensions.join(', ')}`);

  // Process the current directory
  const projectDir = process.cwd();
  console.log(`${colors.yellow}Analyzing project:${colors.reset} ${projectDir}`);

  const startTime = Date.now();
  const results = processDirectory(projectDir);
  const endTime = Date.now();

  // Generate the documentation report
  generateReport(results);

  console.log(`\n${colors.yellow}Analysis completed in ${(endTime - startTime) / 1000} seconds${colors.reset}`);

  // Ask if user wants to apply documentation
  console.log(`\n${colors.cyan}Would you like to apply suggested documentation to files? (y/n)${colors.reset}`);
  // In a real interactive scenario, we'd wait for user input
  // For this demo, we'll just show what would happen
  console.log(`${colors.green}Sample documentation application:${colors.reset}`);

  if (results.length > 0 && results[0].suggestions.length > 0) {
    const sample = results[0];
    console.log(`\nFor file: ${sample.fileName}`);

    if (sample.suggestions.length > 0) {
      const suggestion = sample.suggestions[0];
      console.log(`\n${colors.yellow}${suggestion.type} ${suggestion.name}:${colors.reset}`);
      console.log(suggestion.documentation);

      // Simulate applying documentation
      const applied = applyDocumentation(sample.filePath, sample.suggestions);
      console.log(`${colors.green}Documentation applied: ${applied}${colors.reset}`);
    }
  }

  console.log(`\n${colors.magenta}Documentation system execution complete!${colors.reset}`);
}

// Execute the main function
main().catch(err => {
  console.error('Error:', err);
});


import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import express from 'express';

const colors = {
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m',
  reset: '\x1b[0m',
  dim: '\x1b[2m'
};

console.log(`\n${colors.cyan}==============================================${colors.reset}`);
console.log(`${colors.yellow}MARDUK'S SELF-DOCUMENTING CODE - EXPERIMENTAL${colors.reset}`);
console.log(`${colors.cyan}==============================================${colors.reset}\n`);

// Configuration options
const config = {
  // Directories to exclude from analysis
  excludeDirs: ['node_modules', '.git', '.github', '.husky', '.wrangler', '.config'],
  // File extensions to analyze
  fileExtensions: ['.js', '.jsx', '.ts', '.tsx', '.py', '.md'],
  // Output directory for generated documentation
  outputDir: './generated-docs',
  // Maximum number of files to process
  maxFiles: 100,
  // Enable pattern recognition
  enablePatternRecognition: true,
  // Enable function usage tracking
  enableUsageTracking: true
};

// Types of code elements to detect
const ELEMENT_TYPES = {
  FUNCTION: 'function',
  CLASS: 'class',
  METHOD: 'method',
  COMPONENT: 'component',
  VARIABLE: 'variable',
  IMPORT: 'import',
  EXPORT: 'export',
  COMMENT: 'comment'
};

// Structure to store the recognized code elements
const codebase = {
  files: new Map(),
  elements: new Map(),
  patterns: new Map(),
  usageGraph: new Map(),
  // Store stats for reporting
  stats: {
    totalFiles: 0,
    totalFunctions: 0,
    totalClasses: 0,
    totalComponents: 0,
    totalVariables: 0,
    totalComments: 0,
    totalUndocumented: 0
  }
};

// Helper to identify file type from extension
const getFileType = (filePath) => {
  const ext = path.extname(filePath).toLowerCase();
  if (['.js', '.jsx', '.ts', '.tsx'].includes(ext)) return 'javascript';
  if (ext === '.py') return 'python';
  if (ext === '.md') return 'markdown';
  return 'unknown';
};

// Scan directory recursively and analyze files
const scanDirectory = async (dir, baseDir = '', depth = 0) => {
  // Stop if we've reached the max file limit
  if (codebase.stats.totalFiles >= config.maxFiles) return;

  try {
    const entries = fs.readdirSync(dir);

    for (const entry of entries) {
      const fullPath = path.join(dir, entry);
      const relativePath = path.join(baseDir, entry);

      // Skip excluded directories
      if (config.excludeDirs.includes(entry)) continue;

      const stats = fs.statSync(fullPath);

      if (stats.isDirectory()) {
        // Recursively scan subdirectories
        await scanDirectory(fullPath, relativePath, depth + 1);
      } else if (stats.isFile()) {
        const ext = path.extname(fullPath).toLowerCase();

        // Only process files with specified extensions
        if (config.fileExtensions.includes(ext)) {
          console.log(`${colors.dim}Analyzing ${relativePath}...${colors.reset}`);

          // Analyze the file
          await analyzeFile(fullPath, relativePath);

          // Increment analyzed files counter
          codebase.stats.totalFiles++;

          // Stop if we've reached the max file limit
          if (codebase.stats.totalFiles >= config.maxFiles) {
            console.log(`${colors.yellow}Reached maximum file limit (${config.maxFiles}). Stopping analysis.${colors.reset}`);
            break;
          }
        }
      }
    }
  } catch (error) {
    console.error(`${colors.red}Error scanning directory ${dir}: ${error.message}${colors.reset}`);
  }
};

// Analyze a single file
const analyzeFile = async (filePath, relativePath) => {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const fileType = getFileType(filePath);

    // Store file data
    codebase.files.set(relativePath, {
      path: relativePath,
      type: fileType,
      size: content.length,
      elements: []
    });

    // Process based on file type
    switch (fileType) {
      case 'javascript':
        analyzeJavaScript(content, relativePath);
        break;
      case 'python':
        analyzePython(content, relativePath);
        break;
      case 'markdown':
        analyzeMarkdown(content, relativePath);
        break;
    }

  } catch (error) {
    console.error(`${colors.red}Error analyzing file ${filePath}: ${error.message}${colors.reset}`);
  }
};

// Analyze JavaScript/TypeScript files
const analyzeJavaScript = (content, filePath) => {
  const file = codebase.files.get(filePath);

  // Extract functions
  extractJSFunctions(content, filePath);

  // Extract classes
  extractJSClasses(content, filePath);

  // Extract React components
  extractReactComponents(content, filePath);

  // Extract imports/exports
  extractJSImportsExports(content, filePath);

  // Extract JSDoc comments
  extractJSDocComments(content, filePath);
};

// Extract JavaScript functions
const extractJSFunctions = (content, filePath) => {
  // Match regular functions and arrow functions
  const functionRegex = /(?:function\s+([a-zA-Z0-9_$]+)\s*\([^)]*\)\s*{)|(?:(?:const|let|var)\s+([a-zA-Z0-9_$]+)\s*=\s*(?:function\s*\([^)]*\)|(?:\([^)]*\)\s*=>))/g;

  let match;
  while ((match = functionRegex.exec(content)) !== null) {
    const functionName = match[1] || match[2];

    if (functionName) {
      const element = {
        id: `${filePath}:${functionName}`,
        name: functionName,
        type: ELEMENT_TYPES.FUNCTION,
        filePath,
        location: match.index,
        documentation: extractDocumentation(content, match.index)
      };

      // Add to elements map
      codebase.elements.set(element.id, element);

      // Add to file's elements list
      const file = codebase.files.get(filePath);
      file.elements.push(element.id);

      // Update stats
      codebase.stats.totalFunctions++;

      if (!element.documentation) {
        codebase.stats.totalUndocumented++;
      }
    }
  }
};

// Extract JavaScript classes
const extractJSClasses = (content, filePath) => {
  const classRegex = /class\s+([a-zA-Z0-9_$]+)(?:\s+extends\s+([a-zA-Z0-9_$.]+))?\s*{/g;

  let match;
  while ((match = classRegex.exec(content)) !== null) {
    const className = match[1];
    const extendsClass = match[2];

    const element = {
      id: `${filePath}:${className}`,
      name: className,
      type: ELEMENT_TYPES.CLASS,
      filePath,
      location: match.index,
      extends: extendsClass,
      methods: [],
      documentation: extractDocumentation(content, match.index)
    };

    // Extract methods
    const classBody = extractBalancedBlock(content.slice(match.index + match[0].length - 1));
    if (classBody) {
      extractClassMethods(classBody, element);
    }

    // Add to elements map
    codebase.elements.set(element.id, element);

    // Add to file's elements list
    const file = codebase.files.get(filePath);
    file.elements.push(element.id);

    // Update stats
    codebase.stats.totalClasses++;

    if (!element.documentation) {
      codebase.stats.totalUndocumented++;
    }
  }
};

// Extract methods from a class body
const extractClassMethods = (classBody, classElement) => {
  // Match class methods
  const methodRegex = /(?:async\s+)?([a-zA-Z0-9_$]+)\s*\([^)]*\)\s*{/g;

  let match;
  while ((match = methodRegex.exec(classBody)) !== null) {
    const methodName = match[1];

    // Skip constructor and private methods (starting with _)
    if (methodName !== 'constructor' && !methodName.startsWith('_')) {
      const methodId = `${classElement.id}:${methodName}`;

      const element = {
        id: methodId,
        name: methodName,
        type: ELEMENT_TYPES.METHOD,
        filePath: classElement.filePath,
        parentClass: classElement.id,
        location: match.index,
        documentation: extractDocumentation(classBody, match.index)
      };

      // Add to elements map
      codebase.elements.set(element.id, element);

      // Add to class's methods
      classElement.methods.push(methodId);

      if (!element.documentation) {
        codebase.stats.totalUndocumented++;
      }
    }
  }
};

// Extract React components
const extractReactComponents = (content, filePath) => {
  // Match functional components (function Component or const Component = ...)
  const componentRegex = /(?:function\s+([A-Z][a-zA-Z0-9_$]*)\s*\([^)]*\)\s*{)|(?:(?:const|let|var)\s+([A-Z][a-zA-Z0-9_$]*)\s*=\s*(?:function\s*\([^)]*\)|(?:\([^)]*\)\s*=>)))/g;

  let match;
  while ((match = componentRegex.exec(content)) !== null) {
    const componentName = match[1] || match[2];

    // Check if it returns JSX by looking for return statements followed by JSX-like code
    const nextChunk = content.slice(match.index, match.index + 500); // Look at next 500 chars
    if (nextChunk.match(/return\s*\(/)) {
      const element = {
        id: `${filePath}:${componentName}`,
        name: componentName,
        type: ELEMENT_TYPES.COMPONENT,
        filePath,
        location: match.index,
        documentation: extractDocumentation(content, match.index),
        props: extractReactProps(nextChunk)
      };

      // Add to elements map
      codebase.elements.set(element.id, element);

      // Add to file's elements list
      const file = codebase.files.get(filePath);
      file.elements.push(element.id);

      // Update stats
      codebase.stats.totalComponents++;

      if (!element.documentation) {
        codebase.stats.totalUndocumented++;
      }
    }
  }
};

// Extract React props from component
const extractReactProps = (componentCode) => {
  const props = [];

  // Match destructured props in function parameters
  const propsRegex = /\(\s*{\s*([^}]+)\s*}\s*\)/;
  const match = componentCode.match(propsRegex);

  if (match) {
    const propsString = match[1];
    // Split by commas and clean up
    const propsList = propsString.split(',').map(p => p.trim());

    for (const prop of propsList) {
      // Handle default values and type annotations
      const [propName] = prop.split(/\s*[=:]\s*/);

      if (propName && propName !== '') {
        props.push({
          name: propName.trim(),
          required: !prop.includes('=')
        });
      }
    }
  }

  return props;
};

// Extract imports and exports
const extractJSImportsExports = (content, filePath) => {
  // Extract imports
  const importRegex = /import\s+(?:{([^}]+)}\s+from\s+['"]([^'"]+)['"]|([^;]+)\s+from\s+['"]([^'"]+)['"])/g;

  let match;
  while ((match = importRegex.exec(content)) !== null) {
    const namedImports = match[1] ? match[1].split(',').map(i => i.trim()) : [];
    const defaultImport = match[3] ? match[3].trim() : null;
    const source = match[2] || match[4];

    const element = {
      id: `${filePath}:import:${source}`,
      type: ELEMENT_TYPES.IMPORT,
      filePath,
      source,
      namedImports,
      defaultImport,
      location: match.index
    };

    // Add to elements map
    codebase.elements.set(element.id, element);

    // Add to file's elements list
    const file = codebase.files.get(filePath);
    file.elements.push(element.id);
  }

  // Extract exports
  const exportRegex = /export\s+(?:default\s+([^;\s]+)|(?:{([^}]+)}))/g;

  while ((match = exportRegex.exec(content)) !== null) {
    const defaultExport = match[1] ? match[1].trim() : null;
    const namedExports = match[2] ? match[2].split(',').map(e => e.trim()) : [];

    const element = {
      id: `${filePath}:export:${defaultExport || namedExports.join(',')}`,
      type: ELEMENT_TYPES.EXPORT,
      filePath,
      defaultExport,
      namedExports,
      location: match.index
    };

    // Add to elements map
    codebase.elements.set(element.id, element);

    // Add to file's elements list
    const file = codebase.files.get(filePath);
    file.elements.push(element.id);
  }
};

// Extract JSDoc comments
const extractJSDocComments = (content, filePath) => {
  const jsdocRegex = /\/\*\*\s*([\s\S]*?)\s*\*\//g;

  let match;
  while ((match = jsdocRegex.exec(content)) !== null) {
    const commentContent = match[1].replace(/\s*\*\s?/gm, '\n').trim();

    const element = {
      id: `${filePath}:comment:${match.index}`,
      type: ELEMENT_TYPES.COMMENT,
      filePath,
      content: commentContent,
      location: match.index
    };

    // Parse JSDoc tags
    const tags = parseJSDocTags(commentContent);
    if (tags.length > 0) {
      element.tags = tags;
    }

    // Add to elements map
    codebase.elements.set(element.id, element);

    // Add to file's elements list
    const file = codebase.files.get(filePath);
    file.elements.push(element.id);

    // Update stats
    codebase.stats.totalComments++;
  }
};

// Parse JSDoc tags from comment content
const parseJSDocTags = (content) => {
  const tags = [];
  const tagRegex = /@([a-zA-Z]+)\s+([^\n@]*)/g;

  let match;
  while ((match = tagRegex.exec(content)) !== null) {
    const tagName = match[1];
    const tagValue = match[2].trim();

    tags.push({ tagName, tagValue });
  }

  return tags;
};

// Extract Python functions and classes
const analyzePython = (content, filePath) => {
  // Extract Python functions
  const functionRegex = /def\s+([a-zA-Z0-9_]+)\s*\([^)]*\)\s*:/g;

  let match;
  while ((match = functionRegex.exec(content)) !== null) {
    const functionName = match[1];

    const element = {
      id: `${filePath}:${functionName}`,
      name: functionName,
      type: ELEMENT_TYPES.FUNCTION,
      filePath,
      location: match.index,
      documentation: extractPythonDocstring(content, match.index + match[0].length)
    };

    // Add to elements map
    codebase.elements.set(element.id, element);

    // Add to file's elements list
    const file = codebase.files.get(filePath);
    file.elements.push(element.id);

    // Update stats
    codebase.stats.totalFunctions++;

    if (!element.documentation) {
      codebase.stats.totalUndocumented++;
    }
  }

  // Extract Python classes
  const classRegex = /class\s+([a-zA-Z0-9_]+)(?:\s*\(([^)]*)\))?\s*:/g;

  while ((match = classRegex.exec(content)) !== null) {
    const className = match[1];
    const inherits = match[2] ? match[2].split(',').map(c => c.trim()) : [];

    const element = {
      id: `${filePath}:${className}`,
      name: className,
      type: ELEMENT_TYPES.CLASS,
      filePath,
      location: match.index,
      inherits,
      methods: [],
      documentation: extractPythonDocstring(content, match.index + match[0].length)
    };

    // Add to elements map
    codebase.elements.set(element.id, element);

    // Add to file's elements list
    const file = codebase.files.get(filePath);
    file.elements.push(element.id);

    // Update stats
    codebase.stats.totalClasses++;

    if (!element.documentation) {
      codebase.stats.totalUndocumented++;
    }
  }
};

// Extract Python docstring
const extractPythonDocstring = (content, startIndex) => {
  const nextChunk = content.slice(startIndex, startIndex + 200);

  // Look for triple-quoted docstring
  const docstringMatch = nextChunk.match(/^\s*(?:'''|""")([\s\S]*?)(?:'''|""")/);

  if (docstringMatch) {
    return docstringMatch[1].trim();
  }

  return null;
};

// Analyze Markdown files
const analyzeMarkdown = (content, filePath) => {
  // Extract headers and build a structure
  const headerRegex = /^(#{1,6})\s+(.+)$/gm;

  const headers = [];
  let match;

  while ((match = headerRegex.exec(content)) !== null) {
    const level = match[1].length;
    const text = match[2].trim();

    headers.push({
      id: `${filePath}:header:${match.index}`,
      level,
      text,
      location: match.index
    });
  }

  // Store file with headers
  const file = codebase.files.get(filePath);
  file.headers = headers;
};

// Helper to extract documentation comment before a code element
const extractDocumentation = (content, elementIndex) => {
  // Look backwards from the element to find the closest comment
  const prevContent = content.slice(0, elementIndex);

  // Try to find JSDoc comment
  const jsdocMatch = prevContent.match(/\/\*\*\s*([\s\S]*?)\s*\*\/\s*$/);

  if (jsdocMatch) {
    return jsdocMatch[1].replace(/\s*\*\s?/gm, '\n').trim();
  }

  // Try to find single-line comments
  const lineCommentMatch = prevContent.match(/(\/\/.*\n)+\s*$/);

  if (lineCommentMatch) {
    return lineCommentMatch[0].replace(/\/\//g, '').trim();
  }

  return null;
};

// Helper to extract a balanced code block with matching braces
const extractBalancedBlock = (content) => {
  let depth = 0;
  let endIndex = -1;

  for (let i = 0; i < content.length; i++) {
    if (content[i] === '{') {
      depth++;
    } else if (content[i] === '}') {
      depth--;
      if (depth === 0) {
        endIndex = i;
        break;
      }
    }
  }

  if (endIndex > 0) {
    return content.slice(0, endIndex + 1);
  }

  return null;
};

// Analyze patterns across the codebase
const analyzePatterns = () => {
  console.log(`\n${colors.blue}Analyzing code patterns...${colors.reset}`);

  // Naming patterns
  analyzeNamingPatterns();

  // Architecture patterns
  analyzeArchitecturePatterns();

  // Usage patterns (how functions are called)
  analyzeUsagePatterns();
};

// Analyze naming patterns
const analyzeNamingPatterns = () => {
  const namingPatterns = {
    camelCase: 0,
    pascalCase: 0,
    snake_case: 0,
    UPPER_CASE: 0
  };

  const functionNaming = {
    camelCase: 0,
    pascalCase: 0,
    snake_case: 0
  };

  const componentNaming = {
    pascalCase: 0,
    other: 0
  };

  // Check naming patterns
  for (const [, element] of codebase.elements) {
    if (element.name) {
      // Check overall patterns
      if (/^[a-z][a-zA-Z0-9]*$/.test(element.name)) {
        namingPatterns.camelCase++;
      } else if (/^[A-Z][a-zA-Z0-9]*$/.test(element.name)) {
        namingPatterns.pascalCase++;
      } else if (/^[a-z][a-z0-9_]*$/.test(element.name)) {
        namingPatterns.snake_case++;
      } else if (/^[A-Z][A-Z0-9_]*$/.test(element.name)) {
        namingPatterns.UPPER_CASE++;
      }

      // Function naming
      if (element.type === ELEMENT_TYPES.FUNCTION) {
        if (/^[a-z][a-zA-Z0-9]*$/.test(element.name)) {
          functionNaming.camelCase++;
        } else if (/^[A-Z][a-zA-Z0-9]*$/.test(element.name)) {
          functionNaming.pascalCase++;
        } else if (/^[a-z][a-z0-9_]*$/.test(element.name)) {
          functionNaming.snake_case++;
        }
      }

      // Component naming
      if (element.type === ELEMENT_TYPES.COMPONENT) {
        if (/^[A-Z][a-zA-Z0-9]*$/.test(element.name)) {
          componentNaming.pascalCase++;
        } else {
          componentNaming.other++;
        }
      }
    }
  }

  // Store the naming patterns
  codebase.patterns.set('naming', {
    overall: namingPatterns,
    functions: functionNaming,
    components: componentNaming
  });
};

// Analyze architecture patterns
const analyzeArchitecturePatterns = () => {
  const architecturePatterns = {
    moduleTypes: {},
    dependencies: {},
    projectStructure: {}
  };

  // Check for common architecture patterns
  const filesByDirectory = {};

  for (const [path, file] of codebase.files) {
    const dir = path.includes('/') ? path.split('/')[0] : 'root';

    if (!filesByDirectory[dir]) {
      filesByDirectory[dir] = [];
    }

    filesByDirectory[dir].push(file);
  }

  // Analyze project structure
  architecturePatterns.projectStructure = filesByDirectory;

  // Check for common module types
  const moduleTypes = {
    components: 0,
    utils: 0,
    services: 0,
    hooks: 0,
    models: 0
  };

  for (const [path] of codebase.files) {
    if (path.includes('/components/') || path.includes('Component')) moduleTypes.components++;
    if (path.includes('/utils/') || path.includes('Util')) moduleTypes.utils++;
    if (path.includes('/services/') || path.includes('Service')) moduleTypes.services++;
    if (path.includes('/hooks/') || path.includes('Hook')) moduleTypes.hooks++;
    if (path.includes('/models/') || path.includes('Model')) moduleTypes.models++;
  }

  architecturePatterns.moduleTypes = moduleTypes;

  // Store architecture patterns
  codebase.patterns.set('architecture', architecturePatterns);
};

// Analyze usage patterns
const analyzeUsagePatterns = () => {
  const usagePatterns = {};

  // Build a graph of function calls
  for (const [, element] of codebase.elements) {
    if (element.type === ELEMENT_TYPES.FUNCTION || element.type === ELEMENT_TYPES.METHOD) {
      // Get the file content
      try {
        const filePath = element.filePath;
        const content = fs.readFileSync(filePath, 'utf-8');

        // Check which other functions this function calls
        const calls = [];

        for (const [, otherElement] of codebase.elements) {
          if (
            (otherElement.type === ELEMENT_TYPES.FUNCTION || otherElement.type === ELEMENT_TYPES.METHOD) &&
            otherElement.name !== element.name
          ) {
            // Check for function calls with simple regex - this is an approximation
            const callRegex = new RegExp(`\\b${otherElement.name}\\s*\\(`, 'g');

            // Find the function body
            const elementMatch = content.slice(element.location).match(/\{[\s\S]*\}/);

            if (elementMatch) {
              const functionBody = elementMatch[0];
              if (callRegex.test(functionBody)) {
                calls.push(otherElement.id);
              }
            }
          }
        }

        if (calls.length > 0) {
          codebase.usageGraph.set(element.id, calls);
        }
      } catch (error) {
        console.error(`${colors.red}Error analyzing calls for ${element.name}: ${error.message}${colors.reset}`);
      }
    }
  }
};

// Generate documentation from the analyzed codebase
const generateDocumentation = async () => {
  console.log(`\n${colors.blue}Generating documentation...${colors.reset}`);

  try {
    // Create output directory if it doesn't exist
    if (!fs.existsSync(config.outputDir)) {
      fs.mkdirSync(config.outputDir, { recursive: true });
    }

    // Generate index file
    await generateIndexPage();

    // Generate files documentation
    await generateFilePages();

    // Generate elements documentation
    await generateElementPages();

    // Generate pattern analysis
    await generatePatternAnalysis();

    console.log(`${colors.green}✓ Documentation generated in ${config.outputDir}${colors.reset}`);
  } catch (error) {
    console.error(`${colors.red}Error generating documentation: ${error.message}${colors.reset}`);
  }
};

// Generate index page
const generateIndexPage = async () => {
  const content = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Self-Documenting Code Analysis</title>
  <style>
    :root {
      --bg-color: #1a1a2e;
      --text-color: #e1e2e3;
      --primary: #9c27b0;
      --secondary: #00bcd4;
      --success: #50fa7b;
      --warning: #ffb86c;
      --danger: #ff5555;
    }

    body {
      font-family: 'Courier New', monospace;
      background-color: var(--bg-color);
      color: var(--text-color);
      margin: 0;
      padding: 20px;
    }

    h1, h2, h3 {
      color: var(--primary);
    }

    a {
      color: var(--secondary);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin: 20px 0;
    }

    .stat-card {
      background-color: rgba(0, 0, 0, 0.2);
      border-left: 4px solid var(--primary);
      padding: 15px;
      border-radius: 4px;
    }

    .stat-value {
      font-size: 2rem;
      font-weight: bold;
      color: var(--secondary);
    }

    .file-list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 10px;
      margin: 20px 0;
    }

    .file-item {
      background-color: rgba(0, 0, 0, 0.2);
      padding: 10px;
      border-radius: 4px;
    }

    .progress-bar {
      width: 100%;
      background-color: rgba(0, 0, 0, 0.3);
      height: 20px;
      border-radius: 10px;
      overflow: hidden;
      margin: 10px 0;
    }

    .progress-fill {
      height: 100%;
      background-color: var(--primary);
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Self-Documenting Code Analysis</h1>
    <p>Generated on ${new Date().toLocaleString()}</p>

    <h2>Project Statistics</h2>
    <div class="stats">
      <div class="stat-card">
        <div class="stat-value">${codebase.stats.totalFiles}</div>
        <div>Files Analyzed</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">${codebase.stats.totalFunctions}</div>
        <div>Functions</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">${codebase.stats.totalClasses}</div>
        <div>Classes</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">${codebase.stats.totalComponents}</div>
        <div>Components</div>
      </div>
    </div>

    <h2>Documentation Coverage</h2>
    <div class="progress-bar">
      <div class="progress-fill" style="width: ${calculateDocumentationCoverage()}%"></div>
    </div>
    <p>${calculateDocumentationCoverage()}% of code elements have documentation</p>

    <h2>Files</h2>
    <div class="file-list">
      ${generateFileList()}
    </div>

    <h2>Code Elements</h2>
    <ul>
      <li><a href="elements-functions.html">Functions (${codebase.stats.totalFunctions})</a></li>
      <li><a href="elements-classes.html">Classes (${codebase.stats.totalClasses})</a></li>
      <li><a href="elements-components.html">Components (${codebase.stats.totalComponents})</a></li>
    </ul>

    <h2>Pattern Analysis</h2>
    <ul>
      <li><a href="patterns-naming.html">Naming Patterns</a></li>
      <li><a href="patterns-architecture.html">Architecture Patterns</a></li>
      <li><a href="patterns-usage.html">Usage Patterns</a></li>
    </ul>
  </div>
</body>
</html>
`;

  fs.writeFileSync(path.join(config.outputDir, 'index.html'), content);
};

// Generate file list HTML
const generateFileList = () => {
  let html = '';

  for (const [filePath, fileData] of codebase.files) {
    html += `
      <div class="file-item">
        <a href="file-${encodeFilePath(filePath)}.html">${filePath}</a>
        <div>Type: ${fileData.type}</div>
        <div>Elements: ${fileData.elements.length}</div>
      </div>
    `;
  }

  return html;
};

// Generate pages for each file
const generateFilePages = async () => {
  for (const [filePath, fileData] of codebase.files) {
    const elements = fileData.elements
      .map(id => codebase.elements.get(id))
      .filter(Boolean);

    const content = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>File: ${filePath}</title>
  <style>
    :root {
      --bg-color: #1a1a2e;
      --text-color: #e1e2e3;
      --primary: #9c27b0;
      --secondary: #00bcd4;
      --success: #50fa7b;
      --warning: #ffb86c;
      --danger: #ff5555;
    }

    body {
      font-family: 'Courier New', monospace;
      background-color: var(--bg-color);
      color: var(--text-color);
      margin: 0;
      padding: 20px;
    }

    h1, h2, h3 {
      color: var(--primary);
    }

    a {
      color: var(--secondary);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .element {
      background-color: rgba(0, 0, 0, 0.2);
      border-left: 4px solid var(--primary);
      padding: 15px;
      border-radius: 4px;
      margin-bottom: 20px;
    }

    .element-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .element-name {
      color: var(--secondary);
      font-weight: bold;
      font-size: 1.2rem;
    }

    .element-type {
      background-color: var(--primary);
      color: white;
      padding: 3px 8px;
      border-radius: 12px;
      font-size: 0.8rem;
      text-transform: uppercase;
    }

    .element-docs {
      background-color: rgba(0, 0, 0, 0.3);
      padding: 10px;
      border-radius: 4px;
      margin-top: 10px;
      white-space: pre-wrap;
    }

    .back-link {
      display: inline-block;
      margin-bottom: 20px;
    }

    .tag {
      display: inline-block;
      background-color: var(--warning);
      color: black;
      padding: 2px 6px;
      border-radius: 4px;
      margin-right: 5px;
      font-size: 0.8rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <a href="index.html" class="back-link">← Back to Index</a>

    <h1>File: ${filePath}</h1>
    <p>Type: ${fileData.type}</p>

    <h2>Elements (${elements.length})</h2>
    ${generateFileElementsList(elements)}
  </div>
</body>
</html>
`;

    fs.writeFileSync(path.join(config.outputDir, `file-${encodeFilePath(filePath)}.html`), content);
  }
};

// Generate HTML for file elements
const generateFileElementsList = (elements) => {
  let html = '';

  const sortedElements = [...elements].sort((a, b) => {
    // Sort by type first, then by name
    if (a.type !== b.type) {
      const typeOrder = {
        [ELEMENT_TYPES.CLASS]: 1,
        [ELEMENT_TYPES.COMPONENT]: 2,
        [ELEMENT_TYPES.FUNCTION]: 3,
        [ELEMENT_TYPES.METHOD]: 4,
        [ELEMENT_TYPES.VARIABLE]: 5,
        [ELEMENT_TYPES.IMPORT]: 6,
        [ELEMENT_TYPES.EXPORT]: 7,
        [ELEMENT_TYPES.COMMENT]: 8
      };

      return typeOrder[a.type] - typeOrder[b.type];
    }

    return a.name < b.name ? -1 : 1;
  });

  for (const element of sortedElements) {
    let specialContent = '';

    if (element.type === ELEMENT_TYPES.CLASS) {
      specialContent = `
        <div>
          ${element.extends ? `<p>Extends: ${element.extends}</p>` : ''}
          ${element.methods && element.methods.length > 0 ? `
            <p>Methods:</p>
            <ul>
              ${element.methods.map(methodId => {
                const method = codebase.elements.get(methodId);
                return method ? `<li>${method.name}</li>` : '';
              }).join('')}
            </ul>
          ` : ''}
        </div>
      `;
    } else if (element.type === ELEMENT_TYPES.COMPONENT) {
      specialContent = `
        <div>
          ${element.props && element.props.length > 0 ? `
            <p>Props:</p>
            <ul>
              ${element.props.map(prop => `
                <li>${prop.name}${prop.required ? ' (required)' : ''}</li>
              `).join('')}
            </ul>
          ` : ''}
        </div>
      `;
    } else if (element.type === ELEMENT_TYPES.IMPORT) {
      specialContent = `
        <div>
          <p>Imports from: ${element.source}</p>
          ${element.defaultImport ? `<p>Default import: ${element.defaultImport}</p>` : ''}
          ${element.namedImports && element.namedImports.length > 0 ? `
            <p>Named imports: ${element.namedImports.join(', ')}</p>
          ` : ''}
        </div>
      `;
    } else if (element.type === ELEMENT_TYPES.EXPORT) {
      specialContent = `
        <div>
          ${element.defaultExport ? `<p>Default export: ${element.defaultExport}</p>` : ''}
          ${element.namedExports && element.namedExports.length > 0 ? `
            <p>Named exports: ${element.namedExports.join(', ')}</p>
          ` : ''}
        </div>
      `;
    }

    html += `
      <div class="element">
        <div class="element-header">
          <span class="element-name">${element.name || element.id}</span>
          <span class="element-type">${element.type}</span>
        </div>

        ${specialContent}

        ${element.documentation ? `
          <div class="element-docs">
            ${element.documentation}

            ${element.tags ? `
              <div class="tags">
                ${element.tags.map(tag => `
                  <span class="tag">@${tag.tagName}</span>
                `).join('')}
              </div>
            ` : ''}
          </div>
        ` : `<p><em>No documentation available</em></p>`}
      </div>
    `;
  }

  return html;
};

// Generate pages for elements grouped by type
const generateElementPages = async () => {
  // Generate functions page
  generateElementTypePage('functions', ELEMENT_TYPES.FUNCTION, 'Functions');

  // Generate classes page
  generateElementTypePage('classes', ELEMENT_TYPES.CLASS, 'Classes');

  // Generate components page
  generateElementTypePage('components', ELEMENT_TYPES.COMPONENT, 'Components');
};

// Generate a page for a specific element type
const generateElementTypePage = (slug, elementType, title) => {
  const elements = Array.from(codebase.elements.values())
    .filter(element => element.type === elementType)
    .sort((a, b) => a.name < b.name ? -1 : 1);

  const content = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} - Self-Documenting Code Analysis</title>
  <style>
    :root {
      --bg-color: #1a1a2e;
      --text-color: #e1e2e3;
      --primary: #9c27b0;
      --secondary: #00bcd4;
      --success: #50fa7b;
      --warning: #ffb86c;
      --danger: #ff5555;
    }

    body {
      font-family: 'Courier New', monospace;
      background-color: var(--bg-color);
      color: var(--text-color);
      margin: 0;
      padding: 20px;
    }

    h1, h2, h3 {
      color: var(--primary);
    }

    a {
      color: var(--secondary);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .element {
      background-color: rgba(0, 0, 0, 0.2);
      border-left: 4px solid var(--primary);
      padding: 15px;
      border-radius: 4px;
      margin-bottom: 20px;
    }

    .element-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .element-name {
      color: var(--secondary);
      font-weight: bold;
      font-size: 1.2rem;
    }

    .element-file {
      color: var(--warning);
    }

    .element-docs {
      background-color: rgba(0, 0, 0, 0.3);
      padding: 10px;
      border-radius: 4px;
      margin-top: 10px;
      white-space: pre-wrap;
    }

    .back-link {
      display: inline-block;
      margin-bottom: 20px;
    }

    .search-box {
      width: 100%;
      background-color: rgba(0, 0, 0, 0.3);
      border: 1px solid var(--primary);
      padding: 10px;
      color: var(--text-color);
      font-family: 'Courier New', monospace;
      border-radius: 4px;
      margin-bottom: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <a href="index.html" class="back-link">← Back to Index</a>

    <h1>${title} (${elements.length})</h1>

    <input type="text" id="searchBox" class="search-box" placeholder="Search ${title.toLowerCase()}...">

    <div id="elementsList">
      ${elements.map(element => `
        <div class="element" data-name="${element.name.toLowerCase()}">
          <div class="element-header">
            <span class="element-name">${element.name}</span>
            <span class="element-file">
              <a href="file-${encodeFilePath(element.filePath)}.html">${element.filePath}</a>
            </span>
          </div>

          ${element.documentation ? `
            <div class="element-docs">
              ${element.documentation}
            </div>
          ` : `<p><em>No documentation available</em></p>`}
        </div>
      `).join('')}
    </div>

    <script>
      // Simple search functionality
      const searchBox = document.getElementById('searchBox');
      const elementsList = document.getElementById('elementsList');
      const elements = elementsList.querySelectorAll('.element');

      searchBox.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();

        elements.forEach(element => {
          const name = element.dataset.name;

          if (name.includes(searchTerm)) {
            element.style.display = 'block';
          } else {
            element.style.display = 'none';
          }
        });
      });
    </script>
  </div>
</body>
</html>
`;

  fs.writeFileSync(path.join(config.outputDir, `elements-${slug}.html`), content);
};

// Generate pattern analysis pages
const generatePatternAnalysis = async () => {
  // Naming patterns
  generateNamingPatternsPage();

  // Architecture patterns
  generateArchitecturePatternsPage();

  // Usage patterns
  generateUsagePatternsPage();
};

// Generate naming patterns page
const generateNamingPatternsPage = () => {
  const namingPattern = codebase.patterns.get('naming');

  const content = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Naming Patterns - Self-Documenting Code Analysis</title>
  <style>
    :root {
      --bg-color: #1a1a2e;
      --text-color: #e1e2e3;
      --primary: #9c27b0;
      --secondary: #00bcd4;
      --success: #50fa7b;
      --warning: #ffb86c;
      --danger: #ff5555;
    }

    body {
      font-family: 'Courier New', monospace;
      background-color: var(--bg-color);
      color: var(--text-color);
      margin: 0;
      padding: 20px;
    }

    h1, h2, h3 {
      color: var(--primary);
    }

    a {
      color: var(--secondary);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .back-link {
      display: inline-block;
      margin-bottom: 20px;
    }

    .chart-container {
      background-color: rgba(0, 0, 0, 0.2);
      border-radius: 4px;
      padding: 20px;
      margin-bottom: 20px;
    }

    .bar-chart {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .bar-row {
      display: flex;
      align-items: center;
    }

    .bar-label {
      width: 120px;
      text-align: right;
      padding-right: 10px;
    }

    .bar {
      height: 30px;
      background-color: var(--primary);
      border-radius: 4px;
    }

    .bar-value {
      margin-left: 10px;
    }

    .recommendations {
      background-color: rgba(0, 0, 0, 0.2);
      border-left: 4px solid var(--warning);
      padding: 15px;
      border-radius: 4px;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <a href="index.html" class="back-link">← Back to Index</a>

    <h1>Naming Patterns Analysis</h1>

    <h2>Overall Naming Patterns</h2>
    <div class="chart-container">
      <div class="bar-chart">
        ${generateBarChart(namingPattern.overall)}
      </div>
    </div>

    <h2>Function Naming Patterns</h2>
    <div class="chart-container">
      <div class="bar-chart">
        ${generateBarChart(namingPattern.functions)}
      </div>
    </div>

    <h2>Component Naming Patterns</h2>
    <div class="chart-container">
      <div class="bar-chart">
        ${generateBarChart(namingPattern.components)}
      </div>
    </div>

    <div class="recommendations">
      <h3>Naming Recommendations</h3>
      <ul>
        ${generateNamingRecommendations(namingPattern)}
      </ul>
    </div>
  </div>
</body>
</html>
`;

  fs.writeFileSync(path.join(config.outputDir, 'patterns-naming.html'), content);
};

// Generate bar chart HTML
const generateBarChart = (data) => {
  if (!data) return '<p>No data available</p>';

  const total = Object.values(data).reduce((sum, value) => sum + value, 0);
  if (total === 0) return '<p>No data available</p>';

  let html = '';

  for (const [label, value] of Object.entries(data)) {
    const percentage = (value / total * 100).toFixed(1);

    html += `
      <div class="bar-row">
        <div class="bar-label">${label}</div>
        <div class="bar" style="width: ${percentage}%"></div>
        <div class="bar-value">${value} (${percentage}%)</div>
      </div>
    `;
  }

  return html;
};

// Generate naming recommendations
const generateNamingRecommendations = (namingPattern) => {
  const recommendations = [];

  // Overall conventions
  const dominantStyle = Object.entries(namingPattern.overall)
    .sort((a, b) => b[1] - a[1])[0];

  recommendations.push(`
    <li>
      The dominant naming convention in the codebase is <strong>${dominantStyle[0]}</strong> (${dominantStyle[1]} instances).
      Consider standardizing on this convention for consistency.
    </li>
  `);

  // Function recommendations
  const functionStyles = Object.entries(namingPattern.functions)
    .filter(([, value]) => value > 0);

  if (functionStyles.length > 1) {
    recommendations.push(`
      <li>
        Functions use mixed naming styles (${functionStyles.map(([style]) => style).join(', ')}).
        Consider standardizing on one style, preferably camelCase for JavaScript functions.
      </li>
    `);
  }

  // Component recommendations
  if (namingPattern.components.other > 0) {
    recommendations.push(`
      <li>
        Some components (${namingPattern.components.other}) do not use PascalCase naming.
        React components should consistently use PascalCase.
      </li>
    `);
  }

  return recommendations.join('');
};

// Generate architecture patterns page
const generateArchitecturePatternsPage = () => {
  const architecturePattern = codebase.patterns.get('architecture');

  const content = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Architecture Patterns - Self-Documenting Code Analysis</title>
  <style>
    :root {
      --bg-color: #1a1a2e;
      --text-color: #e1e2e3;
      --primary: #9c27b0;
      --secondary: #00bcd4;
      --success: #50fa7b;
      --warning: #ffb86c;
      --danger: #ff5555;
    }

    body {
      font-family: 'Courier New', monospace;
      background-color: var(--bg-color);
      color: var(--text-color);
      margin: 0;
      padding: 20px;
    }

    h1, h2, h3 {
      color: var(--primary);
    }

    a {
      color: var(--secondary);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .back-link {
      display: inline-block;
      margin-bottom: 20px;
    }

    .section {
      background-color: rgba(0, 0, 0, 0.2);
      border-radius: 4px;
      padding: 20px;
      margin-bottom: 20px;
    }

    .directory {
      margin-bottom: 15px;
    }

    .directory-name {
      font-weight: bold;
      color: var(--secondary);
      margin-bottom: 5px;
    }

    .recommendations {
      background-color: rgba(0, 0, 0, 0.2);
      border-left: 4px solid var(--warning);
      padding: 15px;
      border-radius: 4px;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <a href="index.html" class="back-link">← Back to Index</a>

    <h1>Architecture Patterns Analysis</h1>

    <h2>Project Structure</h2>
    <div class="section">
      ${generateProjectStructureHtml(architecturePattern.projectStructure)}
    </div>

    <h2>Module Types</h2>
    <div class="section">
      ${generateModuleTypesHtml(architecturePattern.moduleTypes)}
    </div>

    <div class="recommendations">
      <h3>Architecture Recommendations</h3>
      <ul>
        ${generateArchitectureRecommendations(architecturePattern)}
      </ul>
    </div>
  </div>
</body>
</html>
`;

  fs.writeFileSync(path.join(config.outputDir, 'patterns-architecture.html'), content);
};

// Generate HTML for project structure
const generateProjectStructureHtml = (projectStructure) => {
  if (!projectStructure) return '<p>No data available</p>';

  let html = '';

  for (const [directory, files] of Object.entries(projectStructure)) {
    html += `
      <div class="directory">
        <div class="directory-name">/${directory}</div>
        <div>${files.length} files</div>
      </div>
    `;
  }

  return html;
};

// Generate HTML for module types
const generateModuleTypesHtml = (moduleTypes) => {
  if (!moduleTypes) return '<p>No data available</p>';

  let html = '<ul>';

  for (const [type, count] of Object.entries(moduleTypes)) {
    if (count > 0) {
      html += `<li>${type}: ${count} files</li>`;
    }
  }

  html += '</ul>';

  return html;
};

// Generate architecture recommendations
const generateArchitectureRecommendations = (architecturePattern) => {
  const recommendations = [];

  // Project structure recommendations
  const directoryCount = Object.keys(architecturePattern.projectStructure).length;
  if (directoryCount > 10) {
    recommendations.push(`
      <li>
        The project has ${directoryCount} top-level directories, which could indicate a complex structure.
        Consider grouping related directories to simplify navigation.
      </li>
    `);
  }

  // Module type recommendations
  const moduleTypes = architecturePattern.moduleTypes;
  if (moduleTypes.components > 0 && moduleTypes.utils > 0) {
    recommendations.push(`
      <li>
        The project uses both component and utility modules, indicating a good separation of concerns.
      </li>
    `);
  }

  if (moduleTypes.services === 0 && moduleTypes.components > 10) {
    recommendations.push(`
      <li>
        The project has many components (${moduleTypes.components}) but no service modules.
        Consider adding service modules to separate business logic from presentation components.
      </li>
    `);
  }

  if (recommendations.length === 0) {
    recommendations.push(`
      <li>
        The project structure appears to be well-organized. Continue with the current architecture patterns.
      </li>
    `);
  }

  return recommendations.join('');
};

// Generate usage patterns page
const generateUsagePatternsPage = () => {
  const content = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Usage Patterns - Self-Documenting Code Analysis</title>
  <style>
    :root {
      --bg-color: #1a1a2e;
      --text-color: #e1e2e3;
      --primary: #9c27b0;
      --secondary: #00bcd4;
      --success: #50fa7b;
      --warning: #ffb86c;
      --danger: #ff5555;
    }

    body {
      font-family: 'Courier New', monospace;
      background-color: var(--bg-color);
      color: var(--text-color);
      margin: 0;
      padding: 20px;
    }

    h1, h2, h3 {
      color: var(--primary);
    }

    a {
      color: var(--secondary);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .back-link {
      display: inline-block;
      margin-bottom: 20px;
    }

    .section {
      background-color: rgba(0, 0, 0, 0.2);
      border-radius: 4px;
      padding: 20px;
      margin-bottom: 20px;
    }

    .usage-item {
      margin-bottom: 15px;
    }

    .function-name {
      font-weight: bold;
      color: var(--secondary);
    }

    #graph {
      width: 100%;
      height: 600px;
      background-color: rgba(0, 0, 0, 0.3);
      border-radius: 4px;
    }
  </style>
  <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
  <div class="container">
    <a href="index.html" class="back-link">← Back to Index</a>

    <h1>Usage Patterns Analysis</h1>

    <h2>Function Usage Graph</h2>
    <div class="section">
      <svg id="graph"></svg>
    </div>

    <h2>Most Used Functions</h2>
    <div class="section">
      ${generateMostUsedFunctionsHtml()}
    </div>

    <script>
      // Create a function usage graph visualization
      const usageData = ${JSON.stringify({
        nodes: Array.from(codebase.elements.values())
          .filter(e => e.type === ELEMENT_TYPES.FUNCTION || e.type === ELEMENT_TYPES.METHOD)
          .map(e => ({
            id: e.id,
            name: e.name,
            type: e.type,
            group: e.filePath.split('/')[0]
          })),
        links: Array.from(codebase.usageGraph.entries())
          .flatMap(([sourceId, targetIds]) =>
            targetIds.map(targetId => ({
              source: sourceId,
              target: targetId
            }))
          )
      })};

      const width = document.getElementById('graph').clientWidth;
      const height = 600;

      const svg = d3.select('#graph')
        .attr('width', width)
        .attr('height', height);

      // Create a force simulation
      const simulation = d3.forceSimulation(usageData.nodes)
        .force('link', d3.forceLink(usageData.links).id(d => d.id))
        .force('charge', d3.forceManyBody().strength(-300))
        .force('center', d3.forceCenter(width / 2, height / 2));

      // Create links
      const link = svg.append('g')
        .selectAll('line')
        .data(usageData.links)
        .enter().append('line')
        .attr('stroke', '#9c27b0')
        .attr('stroke-opacity', 0.6)
        .attr('stroke-width', 1.5);

      // Create nodes
      const node = svg.append('g')
        .selectAll('circle')
        .data(usageData.nodes)
        .enter().append('circle')
        .attr('r', 5)
        .attr('fill', d => d.type === 'method' ? '#ffb86c' : '#00bcd4')
        .call(d3.drag()
          .on('start', dragstarted)
          .on('drag', dragged)
          .on('end', dragended));

      // Add node labels
      const label = svg.append('g')
        .selectAll('text')
        .data(usageData.nodes)
        .enter().append('text')
        .text(d => d.name)
        .attr('font-size', 10)
        .attr('dx', 8)
        .attr('dy', '.35em')
        .style('fill', '#e1e2e3');

      // Update positions on each tick
      simulation.on('tick', () => {
        link
          .attr('x1', d => d.source.x)
          .attr('y1', d => d.source.y)
          .attr('x2', d => d.target.x)
          .attr('y2', d => d.target.y);

        node
          .attr('cx', d => d.x)
          .attr('cy', d => d.y);

        label
          .attr('x', d => d.x)
          .attr('y