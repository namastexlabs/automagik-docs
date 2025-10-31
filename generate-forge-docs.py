#!/usr/bin/env python3
"""
Forge Documentation Generator
Generates comprehensive Mintlify documentation for Automagik Forge
"""

import os
import json
from pathlib import Path

# Documentation structure
DOCS = {
    "concepts": {
        "tasks-and-attempts": {
            "title": "Tasks & Attempts",
            "description": "Understanding task lifecycle and multiple attempts",
            "icon": "list-check",
            "sections": [
                "What is a Task?",
                "Task Lifecycle",
                "Multiple Attempts Strategy",
                "When to Use Multiple Attempts",
                "Comparing Attempts"
            ]
        },
        "git-worktrees": {
            "title": "Git Worktrees",
            "description": "Isolation strategy using git worktrees",
            "icon": "code-branch",
            "sections": [
                "What are Git Worktrees?",
                "Why Forge Uses Worktrees",
                "Automatic Worktree Management",
                "Worktree Lifecycle",
                "Best Practices"
            ]
        },
        "agents-and-executors": {
            "title": "AI Agents & Executors",
            "description": "Understanding the 8 AI coding agents and specialized agents",
            "icon": "robot",
            "sections": [
                "AI Coding Agents vs Specialized Agents",
                "The 8 AI Coding Agents",
                "Specialized Agent System",
                "Agent Selection Matrix",
                "Performance Comparison"
            ]
        },
        "mcp-architecture": {
            "title": "MCP Architecture",
            "description": "How Forge acts as a Model Context Protocol server",
            "icon": "diagram-project",
            "sections": [
                "What is MCP?",
                "Forge as MCP Server",
                "Available MCP Tools",
                "Basic vs Advanced Mode",
                "Architecture Diagram"
            ]
        }
    },
    "mcp": {
        "overview": {
            "title": "MCP Integration Overview",
            "description": "Control Forge from any MCP-compatible AI agent",
            "icon": "plug",
            "sections": ["What is MCP?", "Why MCP?", "Getting Started", "Basic vs Advanced"]
        },
        "claude-code-setup": {
            "title": "Claude Code Setup",
            "description": "Configure Forge MCP server for Claude Code",
            "icon": "brain",
            "sections": ["Installation", "Basic Configuration", "Advanced Configuration", "Testing"]
        },
        "cursor-setup": {
            "title": "Cursor Setup",
            "description": "Configure Forge MCP server for Cursor",
            "icon": "cursor",
            "sections": ["Installation", "Configuration", "Usage", "Troubleshooting"]
        },
        "vscode-cline-setup": {
            "title": "VSCode + Cline Setup",
            "description": "Configure Forge MCP server for Cline extension",
            "icon": "code",
            "sections": ["Install Cline", "MCP Configuration", "Testing", "Examples"]
        },
        "custom-clients": {
            "title": "Custom MCP Clients",
            "description": "Connect any MCP-compatible client to Forge",
            "icon": "puzzle-piece",
            "sections": ["Generic Configuration", "Environment Variables", "Testing Connection"]
        }
    }
}

def generate_mdx_content(category, filename, config):
    """Generate MDX content for a documentation page"""

    frontmatter = f"""---
title: "{config['title']}"
description: "{config['description']}"
icon: "{config['icon']}"
---

"""

    content = frontmatter

    # Add introduction
    content += f"## Introduction\n\n"
    content += f"This guide covers {config['description'].lower()}.\n\n"
    content += "---\n\n"

    # Add sections
    for i, section in enumerate(config['sections'], 1):
        content += f"## {section}\n\n"
        content += f"<details>\n<summary>Click to expand {section}</summary>\n\n"
        content += f"Content for {section} goes here.\n\n"
        content += "</details>\n\n"

    # Add navigation
    content += "---\n\n"
    content += "## Next Steps\n\n"
    content += "<CardGroup cols={2}>\n"
    content += '  <Card title="Previous Topic" icon="arrow-left" href="#">\n'
    content += "    Go back\n"
    content += "  </Card>\n"
    content += '  <Card title="Next Topic" icon="arrow-right" href="#">\n'
    content += "    Continue\n"
    content += "  </Card>\n"
    content += "</CardGroup>\n"

    return content

def main():
    """Generate all documentation files"""
    base_path = Path("/home/cezar/automagik/docs/forge")

    for category, files in DOCS.items():
        category_path = base_path / category
        category_path.mkdir(parents=True, exist_ok=True)

        for filename, config in files.items():
            file_path = category_path / f"{filename}.mdx"
            content = generate_mdx_content(category, filename, config)

            with open(file_path, 'w') as f:
                f.write(content)

            print(f"✓ Created {category}/{filename}.mdx")

    print(f"\n✓ Generated {sum(len(files) for files in DOCS.values())} documentation files")

if __name__ == "__main__":
    main()
