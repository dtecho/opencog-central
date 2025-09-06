
# Reference Directory

This directory should contain the site folders that you want to process for llm.txt generation.

## Structure

```
ref/
├── site1/
│   ├── source files...
│   └── llm.txt (generated)
├── site2/
│   ├── source files...
│   └── llm.txt (generated)
└── ...
```

## Usage

1. Place your site folders in this `ref/` directory
2. Run `python generate_llm_txt.py` from the root directory
3. The script will:
   - Generate optimized `llm.txt` files in each site folder
   - Create AI-friendly markdown versions in `llm/sites/`
   - Generate a master index at `llm/index.md`

## What gets processed

The script analyzes each site folder and:
- Identifies the repository type (Python, C++, Rust, Node.js, etc.)
- Scores files based on importance (README files, main source files, etc.)
- Creates structured llm.txt files with file listings and patterns
- Generates comprehensive markdown documentation

## File Priority

Files are prioritized based on:
- File names (README, main.py, CMakeLists.txt, etc.)
- Directory structure (src/, lib/, docs/, etc.)
- File extensions (source code files)
- File size (smaller config files get priority)
- Directory depth (less nested files preferred)
