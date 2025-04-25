use std::env;
use std::process::{Command, exit};
use std::collections::HashMap;

// Define repository categories
const ATOMSPACE_REPOS: &[&str] = &[
    "atomspace", "atomspace-rocks", "atomspace-cog", "cogserver", "unify",
    "atomspace-bridge", "atomspace-dht", "atomspace-ipfs", "atomspace-restful",
    "atomspace-rpc", "atomspace-websockets"
];

const LANGUAGE_REPOS: &[&str] = &[
    "lg-atomese", "link-grammar", "learn", "sensory", "generate", "vision", "language-learning"
];

const REASONING_REPOS: &[&str] = &[
    "ure", "pln", "miner", "attention", "spacetime"
];

const AGENTS_REPOS: &[&str] = &[
    "agents", "atomspace-agents", "ros-behavior-scripting", "agi-bio"
];

const TOOLS_REPOS: &[&str] = &[
    "cogutil", "asmoses", "moses", "opencog", "TinyCog", "benchmark", "pattern-index"
];

const UI_REPOS: &[&str] = &[
    "atomspace-explorer", "atomspace-js", "atomspace-typescript", "atomspace-metta"
];

// Define core repositories for minicog
const MINICOG_REPOS: &[&str] = &[
    "cogutil", "atomspace", "atomspace-rocks", "cogserver", "unify", "ure"
];

fn main() {
    let args: Vec<String> = env::args().collect();
    
    if args.len() < 2 {
        print_usage();
        exit(1);
    }

    match args[1].as_str() {
        "install" => {
            if args.len() < 3 {
                println!("Please specify a package to install");
                exit(1);
            }
            install_package(&args[2]);
        },
        "update" => {
            update_packages();
        },
        "build" => {
            build_projects();
        },
        "list" => {
            list_repositories();
        },
        "minicog" => {
            install_minicog();
        },
        "full" => {
            install_full();
        },
        "help" | "--help" | "-h" => {
            print_usage();
        },
        _ => {
            println!("Unknown command: {}", args[1]);
            print_usage();
            exit(1);
        }
    }
}

fn print_usage() {
    println!("OpenCog Package Manager (ocpkg)");
    println!("Usage:");
    println!("  ocpkg install <package>  - Install a specific OpenCog package/component");
    println!("  ocpkg update             - Update all installed packages");
    println!("  ocpkg build              - Build from source");
    println!("  ocpkg list               - List all available repositories by category");
    println!("  ocpkg minicog            - Install minimal OpenCog (core components only)");
    println!("  ocpkg full               - Install full OpenCog (all components)");
    println!("  ocpkg help               - Show this help message");
}

fn install_package(package: &str) {
    println!("Installing package: {}", package);
    
    // Call the bash script for actual installation logic
    let status = Command::new("/workspaces/opencog-central/ocpkg/ocpkg")
        .arg("-d")        // Install dependencies
        .arg("-f")        // Install from repo
        .arg(package)     // Package/repo name
        .status()
        .expect("Failed to execute bash script");
    
    if !status.success() {
        println!("Failed to install package");
        exit(status.code().unwrap_or(1));
    }
    
    println!("Package {} installed successfully", package);
}

fn update_packages() {
    println!("Updating packages...");
    
    let status = Command::new("/workspaces/opencog-central/ocpkg/ocpkg")
        .arg("-u")        // Update OpenCog
        .status()
        .expect("Failed to execute bash script");
    
    if !status.success() {
        println!("Failed to update packages");
        exit(status.code().unwrap_or(1));
    }
    
    println!("Packages updated successfully");
}

fn build_projects() {
    println!("Building projects...");
    
    let status = Command::new("/workspaces/opencog-central/ocpkg/ocpkg")
        .arg("-b")        // Build source
        .status()
        .expect("Failed to execute bash script");
    
    if !status.success() {
        println!("Failed to build projects");
        exit(status.code().unwrap_or(1));
    }
    
    println!("Projects built successfully");
}

fn list_repositories() {
    println!("OpenCog Repositories by Category:\n");
    
    println!("AtomSpace Components:");
    for repo in ATOMSPACE_REPOS {
        println!("  - {}", repo);
    }
    
    println!("\nLanguage Processing:");
    for repo in LANGUAGE_REPOS {
        println!("  - {}", repo);
    }
    
    println!("\nReasoning Systems:");
    for repo in REASONING_REPOS {
        println!("  - {}", repo);
    }
    
    println!("\nAgents and Bio:");
    for repo in AGENTS_REPOS {
        println!("  - {}", repo);
    }
    
    println!("\nTools and Utilities:");
    for repo in TOOLS_REPOS {
        println!("  - {}", repo);
    }
    
    println!("\nUser Interfaces:");
    for repo in UI_REPOS {
        println!("  - {}", repo);
    }
    
    println!("\nMiniCog Components (minimal installation):");
    for repo in MINICOG_REPOS {
        println!("  - {}", repo);
    }
    
    println!("\nUse 'ocpkg install REPO_NAME' to install a specific repository");
    println!("Use 'ocpkg minicog' for minimal installation");
    println!("Use 'ocpkg full' for full installation");
}

fn install_minicog() {
    println!("Installing MiniCog (minimal OpenCog configuration)...");
    
    let status = Command::new("/workspaces/opencog-central/ocpkg/ocpkg")
        .arg("-M")        // Install MiniCog
        .status()
        .expect("Failed to execute bash script");
    
    if !status.success() {
        println!("Failed to install MiniCog");
        exit(status.code().unwrap_or(1));
    }
    
    println!("MiniCog installed successfully");
}

fn install_full() {
    println!("Installing Full OpenCog (all components)...");
    println!("This may take a long time to complete.");
    
    let status = Command::new("/workspaces/opencog-central/ocpkg/ocpkg")
        .arg("-F")        // Install Full OpenCog
        .status()
        .expect("Failed to execute bash script");
    
    if !status.success() {
        println!("Failed to install Full OpenCog");
        exit(status.code().unwrap_or(1));
    }
    
    println!("Full OpenCog installation completed successfully");
}