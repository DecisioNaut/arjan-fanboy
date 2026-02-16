# Changelog

All notable changes to the arjan-fanboy skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-16

### Added
- Initial release of arjan-fanboy skill
- Core skill structure based on ArjanCodes principles from GitHub repositories
- SKILL.md with core philosophy, anti-patterns, and refactoring guidance
- Five domain-specific reference files for optimal AI context usage:
  - `principles.md` - SOLID principles, coupling/cohesion, core design principles (115 lines)
  - `patterns.md` - Design patterns (Strategy, Observer, Factory, etc.) (90 lines)
  - `refactoring.md` - Common refactoring transformations with examples (174 lines)
  - `style.md` - Code style conventions and 10 anti-patterns (365 lines)
  - `examples.md` - Complete refactoring journeys from Arjan's repos (214 lines)
- MIT License matching original ArjanCodes repositories
- README.md with tribute to Arjan Egges, installation instructions, and usage guide
- Packaged skill file (arjan-fanboy.skill) ready for distribution

### Design Decisions
- Split content into domain-specific files (<500 lines each) following skill-creator best practices
- Progressive disclosure pattern to minimize AI context usage (60-90% reduction per query)
- Load strategy guidance in SKILL.md to help AI choose relevant domain
- Authentic content extracted from Arjan's actual GitHub repositories (betterpython, examples)

### Credits
- Content based on ArjanCodes repositories by Arjan Egges (with permission via LinkedIn)
- Skill structure created using Anthropic's skill-creator framework
- MIT License maintained from original source repositories
