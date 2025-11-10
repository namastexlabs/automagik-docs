# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Mintlify documentation repository** for the Automagik Suite - a collection of 6 AI automation tools:

- **Forge**: AI Orchestration Kanban (NPM package: `automagik-forge`)
- **Hive**: Multi-Agent Factory (Python package: `automagik-hive`)
- **Omni**: Omnipresent Messaging (Python package: `automagik-omni`)
- **Spark**: Temporal Automation (Python package: `automagik-spark`)
- **Genie**: Universal AI Companion (NPM package: `automagik-genie`)
- **Tools**: Instant MCP Generator (Python package: `automagik-tools`)

**Important**: This repository contains ONLY documentation. The actual tool implementations live in separate repositories under the `namastexlabs` GitHub organization.

## Development Commands

### Preview Documentation Locally

```bash
mint dev
```

This starts a local Mintlify development server at `http://localhost:3000`.

### Custom Port

```bash
mint dev --port 3333
```

### Validate Links

```bash
mint broken-links
```

Identifies any broken internal or external links in the documentation.

### Update Mintlify CLI

```bash
npm mint update
```

## Documentation Structure

### Source of Truth: `docs.json`

The **`docs.json`** file is the single source of truth for:
- Navigation structure
- Tab organization
- Page grouping
- API configuration
- Branding/theming

**Before adding new documentation pages**, you MUST update `docs.json` to include them in the navigation.

### Directory Organization

```
.
├── docs.json                  # Navigation & config (SOURCE OF TRUTH)
├── openapi.yaml              # API specification for Forge
├── index.mdx                 # Homepage
├── quickstart.mdx            # Quick start guide
├── development.mdx           # Generic Mintlify development guide
│
├── forge/                    # Forge documentation
│   ├── introduction.mdx
│   ├── quickstart.mdx
│   ├── concepts/            # Core concepts
│   ├── working/             # User guides
│   ├── agents/              # AI agents documentation
│   ├── mcp/                 # MCP integration guides
│   ├── workflows/           # Workflow patterns
│   ├── config/              # Configuration guides
│   ├── api/                 # API reference
│   ├── cli/                 # CLI reference
│   ├── advanced/            # Advanced features
│   └── troubleshooting/
│
├── hive/                    # Hive documentation
├── omni/                    # Omni documentation
├── spark/                   # Spark documentation
├── genie/                   # Genie documentation
├── tools/                   # Tools documentation
├── suite/                   # Suite overview pages
└── essentials/              # Mintlify essentials (rarely modified)
```

### Planning Files (Metadata, Not Published)

The following files are internal planning documents and are NOT published as documentation:

- `.doc-generation-plan.md` - Overall documentation planning
- `.spark-documentation-plan.md` - Spark-specific planning
- `.spark-execution-plan.md` - Spark implementation execution plan
- `.spark-final-audit.md` - Spark documentation audit

These files track documentation work-in-progress and provide guidance for maintaining consistency.

## Automation Scripts

### `convert_api_examples.py`

**Purpose**: Converts old-style API examples to Mintlify's `RequestExample`/`ResponseExample` format.

**Usage**:
```bash
python3 convert_api_examples.py <file.mdx>
```

This creates a `.backup` file before modifying the original. Use this when updating API documentation to the new format.

### `generate-forge-docs.py`

**Purpose**: Template generator for Forge documentation files.

**Note**: This script contains hardcoded paths and is mostly for reference. Review before using.

## Writing Documentation

### Philosophy: "Linus-Approved" Documentation

The Automagik Suite documentation follows a **grounded reality** approach:

- ❌ No marketing fluff or vaporware claims
- ❌ No "revolutionary" or "groundbreaking" unless it actually is
- ✅ Show actual code and real examples
- ✅ Document what exists NOW, not future plans
- ✅ Be honest about limitations
- ✅ Use casual but precise language

### Mintlify Components

Common components used throughout:

```mdx
<CardGroup cols={2}>
  <Card title="Title" icon="icon-name" href="/path">
    Description
  </Card>
</CardGroup>

<AccordionGroup>
  <Accordion title="Question">
    Answer
  </Accordion>
</AccordionGroup>

<Steps>
  <Step title="First Step">
    Content
  </Step>
</Steps>

<Tip>Helpful tip</Tip>
<Warning>Warning message</Warning>
<Info>Information</Info>

<RequestExample>
  ```bash cURL
  curl -X GET http://localhost:8887/api/endpoint
  ```
</RequestExample>

<ResponseExample>
  ```json 200 Success
  { "status": "ok" }
  ```
</ResponseExample>
```

### Mermaid Diagrams

Use mermaid for architecture and flow diagrams:

```mermaid
graph LR
    A[Start] --> B[Process]
    B --> C[End]
```

### Code Examples

Always include:
- Multiple language examples where relevant (bash, JavaScript, Python)
- Real, working code (not pseudocode)
- Context explaining what the code does

## API Documentation

### openapi.yaml

The `openapi.yaml` file defines the Forge API specification. Mintlify automatically generates API reference pages from this file.

**Key Details**:
- Base URL: `http://localhost:8887` (default Forge development server)
- Authentication: Bearer token (GitHub OAuth)
- OpenAPI 3.0.3 specification

When updating API documentation:
1. Modify `openapi.yaml` for spec changes
2. Update corresponding MDX files in `forge/api/` for detailed guides
3. Test with `mint dev` to ensure proper rendering

## Navigation Updates

When adding new documentation pages:

1. Create the `.mdx` file in the appropriate directory
2. Update `docs.json` to include it in the navigation structure
3. Follow the existing grouping patterns:
   - Getting Started
   - Learn / Core Concepts
   - API Reference
   - Configuration
   - Troubleshooting

Example `docs.json` entry:
```json
{
  "group": "Core Concepts",
  "pages": [
    "forge/concepts/existing-page",
    "forge/concepts/new-page"
  ]
}
```

## Architecture Patterns

### Product Documentation Pattern

Each tool follows this structure:
1. **Phase 1: Get It Running** (introduction, installation, quickstart)
2. **Phase 2: Reference** (CLI/API reference)
3. **Phase 3: Real Examples** (practical examples, workflows)
4. **Phase 4: Deep Concepts** (architecture, advanced topics)

This pattern ensures users can get started quickly while having deep reference material available.

### Forge-Specific Architecture

Forge documentation emphasizes:
- **Vibe Coding++™** philosophy (human orchestration, AI execution)
- Git worktree isolation for safe experimentation
- Multi-LLM support (8+ agents)
- MCP (Model Context Protocol) integration
- Task-based workflow management

### Cross-Tool Integration

When documenting integrations between tools:
- Link to both tools' documentation
- Show concrete examples
- Explain the data flow
- Include troubleshooting for common integration issues

## Common Tasks

### Adding a New Concept Page

1. Create `<tool>/concepts/new-concept.mdx`
2. Use this frontmatter template:
```mdx
---
title: "Concept Title"
description: "Brief description"
icon: "icon-name"
---
```
3. Update `docs.json` in the appropriate tool's "Core Concepts" group
4. Link from related pages

### Updating API Documentation

1. Update `openapi.yaml` if changing API spec
2. Update corresponding `forge/api/*.mdx` file for detailed guide
3. Use `convert_api_examples.py` if converting old examples
4. Test with `mint dev`

### Adding Code Examples

Always include:
- Clear context about what the example demonstrates
- Installation/setup requirements
- Expected output
- Explanation of key lines

### Cross-Referencing

Use relative paths for internal links:
```mdx
See [Tasks & Attempts](/forge/concepts/tasks-and-attempts) for details.
```

## Quality Standards

Before committing documentation:

1. ✅ Run `mint dev` and verify the page renders correctly
2. ✅ Check that all links work (`mint broken-links`)
3. ✅ Ensure code examples are tested and working
4. ✅ Follow the "grounded reality" philosophy (no vaporware)
5. ✅ Use proper Mintlify components (not raw HTML/markdown)
6. ✅ Include icons in Card/Accordion components
7. ✅ Verify navigation is updated in `docs.json`

## Troubleshooting Development Issues

### Port Already in Use

Mintlify will automatically try the next available port:
```
Port 3000 is already in use. Trying 3001 instead.
```

### Sharp Module Error (macOS ARM)

```bash
npm remove -g mint
# Upgrade to Node v19+
npm i -g mint
```

### Unknown Error

```bash
rm -rf ~/.mintlify
mint dev
```

## Key Principles

1. **docs.json is the source of truth** - Always update it when adding pages
2. **Test locally** - Run `mint dev` before committing
3. **Real examples only** - No theoretical or future features
4. **User-first structure** - Follow the 4-phase pattern for each tool
5. **Cross-link aggressively** - Help users discover related content
6. **Visual aids** - Use mermaid diagrams, comparison tables, and accordions
7. **Code that works** - Test all examples before documenting them
