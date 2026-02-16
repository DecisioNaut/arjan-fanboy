# Arjan Fanboy - Python Best Practices Skill

An AI skill that enables code review and refactoring following [Arjan Egges](https://github.com/ArjanCodes)' Python best practices and design principles.

## About

This skill teaches AI assistants to review and refactor Python code using the battle-tested principles from **ArjanCodes** - one of the most respected voices in Python software design. It's based on real code examples from Arjan's popular YouTube channel and GitHub repositories.

### Key Features

- **SOLID Principles** - Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **Design Patterns** - Strategy, Observer, Factory, Template Method, Bridge, MVC
- **Modern Python** - Type hints, dataclasses, Protocols, functional patterns
- **Code Quality** - Dependency injection, separation of concerns, testability
- **Anti-patterns** - Learn what to avoid and why

## Tribute & Permissions

This skill is built with deep respect for **Arjan Egges** and his educational work:

- 🙏 **Permission granted** by Arjan via LinkedIn to create this skill
- 📚 Based on his open-source repositories:
  - [ArjanCodes/betterpython](https://github.com/ArjanCodes/betterpython) - Write Better Python Code series
  - [ArjanCodes/examples](https://github.com/ArjanCodes/examples) - YouTube video examples
- 🎥 Subscribe to his channel: [ArjanCodes on YouTube](https://www.youtube.com/c/arjancodes)
- 💼 Learn more: [arjancodes.com](https://www.arjancodes.com/)

**Thank you, Arjan, for your invaluable contributions to the Python community!**

## Creation

This skill was created using the **[skill-creator](https://github.com/anthropics/anthropic-skills)** skill by Anthropic, which provides systematic guidance for building high-quality AI skills following best practices for:
- Progressive disclosure (avoiding context bloat)
- Knowledge organization
- Validation and packaging
- Skill metadata design

## Installation

### Recommended Folder Structure

For best practices, we recommend placing skills in a dedicated directory in your repository:

```
your-project/                    # Your project root
├── .agents/
│   └── skills/
│       └── arjan-fanboy/        # The skill installed here
│           ├── SKILL.md
│           ├── LICENSE.txt
│           └── references/
│               ├── principles.md
│               ├── patterns.md
│               ├── refactoring.md
│               ├── style.md
│               └── examples.md
├── src/                         # (Your application code)
├── tests/                       # (Your tests)
└── README.md                    # (Your project README)
```

**Why `.agents/skills/`?**
- Keeps AI-related resources organized and separate from source code
- Hidden folder (starting with `.`) keeps it unobtrusive
- Easy to add multiple skills in the same location
- Follows emerging community conventions for AI agent configurations

**Alternative locations:**
- `.copilot/skills/` - If using GitHub Copilot
- `.github/agents/skills/` - For GitHub-centric projects

### Option 1: Use the Packaged Skill

```bash
# Download the arjan-fanboy.skill file from the repository
wget https://github.com/DecisioNaut/arjan-fanboy/releases/download/v1.0.0/arjan-fanboy.skill

# Extract it to your skills directory
mkdir -p .agents/skills
unzip arjan-fanboy.skill -d .agents/skills/

# Your AI assistant should now detect the skill at:
# .agents/skills/arjan-fanboy/SKILL.md
```

### Option 2: Clone from Source

```bash
# Clone this repository
git clone https://github.com/DecisioNaut/arjan-fanboy.git

# Copy the skill folder to your project
cp -r arjan-fanboy/arjan-fanboy /path/to/your-project/.agents/skills/

# Or symlink it for development
ln -s $(pwd)/arjan-fanboy/arjan-fanboy /path/to/your-project/.agents/skills/arjan-fanboy
```

### Option 3: Git Submodule (For Teams)

```bash
# Add as a submodule in your project
cd your-project
git submodule add https://github.com/DecisioNaut/arjan-fanboy.git .agents/skills/arjan-fanboy-repo
ln -s .agents/skills/arjan-fanboy-repo/arjan-fanboy .agents/skills/arjan-fanboy

# Team members can then:
git submodule update --init --recursive
```

## Usage

Once installed, the skill activates automatically when you:

- Ask to refactor Python code
- Request code review focused on design principles
- Mention "Arjan", "ArjanCodes", or "How would Arjan..."
- Ask about SOLID principles or design patterns
- Need help with dependency injection, protocols, or type hints

### Example Prompts

```
"How would Arjan refactor this code?"
"Review this Python code following Arjan's principles"
"Apply SOLID principles to this class"
"Help me use dependency injection here"
"What would Arjan say about my code?"
```

## Repository Structure

```
arjan-fanboy/                    # Repository root
├── .gitignore
├── CHANGELOG.md                 # Version history
├── README.md                    # This file
├── arjan-fanboy.skill          # Packaged skill (13KB zip)
└── arjan-fanboy/                # The skill folder
    ├── SKILL.md                 # Main skill file (127 lines)
    ├── LICENSE.txt              # MIT License
    └── references/              # Domain-specific references
        ├── principles.md        # SOLID, coupling/cohesion (115 lines)
        ├── patterns.md          # Design patterns (90 lines)
        ├── refactoring.md       # Common refactoring patterns (174 lines)
        ├── style.md             # Code style & anti-patterns (365 lines)
        └── examples.md          # Complete refactoring examples (214 lines)
```

### What's Inside

**SKILL.md** - Core guidance covering:
- Arjan's philosophy (separation of concerns, dependency injection, protocols)
- Review checklist (architecture, SOLID, code quality)
- Common anti-patterns (god classes, hardcoded dependencies, primitive obsession)
- Quick refactoring patterns with examples
- References guide with load strategy

**Domain-Specific References** - Organized for efficient context usage:

- **principles.md** - SOLID principles (SRP, OCP, LSP, ISP, DIP), coupling/cohesion, dependency inversion, composition over inheritance, key philosophies, and checklist
- **patterns.md** - Design patterns: Strategy (OOP & functional), Observer, Factory, Template Method, Bridge, MVC with practical examples
- **refactoring.md** - 6 common refactoring patterns showing step-by-step transformations from anti-patterns to SOLID code
- **style.md** - Code style conventions (type hints, dataclasses, protocols, naming, modern Python) plus 10 anti-patterns to avoid with examples
- **examples.md** - 5 complete refactoring journeys from Arjan's repositories showing evolution through all SOLID principles

## License

MIT License - See [LICENSE.txt](arjan-fanboy/LICENSE.txt)

Based on code examples from [Arjan Egges' repositories](https://github.com/ArjanCodes), which are also MIT licensed.

## Contributing

Contributions are welcome! If you find examples from Arjan's repositories that should be included, or spot inaccuracies, please open an issue or pull request.

## Acknowledgments

- **Arjan Egges** - For creating amazing Python educational content and granting permission for this skill
- **Anthropic** - For the skill-creator framework that made building this skill systematic and maintainable
- **ArjanCodes Community** - For supporting quality Python education

## Learn More

- [ArjanCodes YouTube Channel](https://www.youtube.com/c/arjancodes)
- [ArjanCodes Website](https://www.arjancodes.com/)
- [Arjan on Twitter/X](https://twitter.com/arjancodes)
- [Arjan on LinkedIn](https://www.linkedin.com/company/arjancodes)

---

*This is an educational skill based on publicly available code examples. It is not officially endorsed by or affiliated with Arjan Egges or ArjanCodes, though permission was granted for its creation.*
