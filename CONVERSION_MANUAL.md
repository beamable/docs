# ReadMe.io to MkDocs Conversion Manual

This manual documents the step-by-step process for converting ReadMe.io documentation to MkDocs-compatible markdown format.

## Overview

ReadMe.io uses custom markdown extensions and proprietary syntax that need to be converted to standard markdown compatible with MkDocs Material theme. This conversion process involves:

1. **Removing ReadMe.io header metadata and adding proper markdown headers**
2. Converting block quotes to MkDocs callouts
3. Removing ReadMe.io-specific HTML blocks
4. Converting parameter tables to standard markdown tables
5. **Converting [block:image] blocks to standard markdown images**
6. Replacing placeholder syntax with actual content
7. Converting external image links to local references
8. Cleaning up HTML elements and special syntax

## Step-by-Step Conversion Process

### 1. Remove ReadMe.io Header Metadata and Add Proper Markdown Headers

**Identify**: Look for YAML front matter at the top of ReadMe.io files

**ReadMe.io Header Format**:
```markdown
---
title: "Builds & Environments"
slug: "builds-environments"
excerpt: ""
hidden: false
createdAt: "Wed Jun 12 2024 17:42:51 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Nov 01 2024 17:14:03 GMT+0000 (Coordinated Universal Time)"
---
```

**Action**: 
1. **Remove the entire YAML front matter block** (everything between the `---` markers)
2. **Replace with a proper markdown H1 header** using the title from the metadata
3. Ensure only ONE H1 header (`#`) exists per document** - all other sections should use H2 (`##`) or lower

**Example Conversion**:

**Before**:
```markdown
---
title: "Builds & Environments"
slug: "builds-environments"
excerpt: ""
hidden: false
createdAt: "Wed Jun 12 2024 17:42:51 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Nov 01 2024 17:14:03 GMT+0000 (Coordinated Universal Time)"
---

If you run the project in the Unity editor...
```

**After**:
```markdown
# Builds & Environments

If you run the project in the Unity editor...
```

**Important Notes**:
- The title should be extracted from the `title` field in the metadata
- Remove quotes around the title when converting to the H1 header
- Ensure there's a blank line between the header and the first paragraph
- This creates proper document structure for MkDocs
- **ONLY ONE H1 HEADER PER DOCUMENT**: If a ReadMe.io file contains multiple documents (indicated by multiple `---` sections), convert additional titles to H2 headers (`##`) instead of H1 (`#`)

**Multi-Document Files**:
Some ReadMe.io exports contain multiple documents concatenated together. Handle these as follows:

**Before** (Multiple document sections):
```markdown
---
title: "Player Centric API - Overview"
---
Content here...

---
title: "Player Centric API - Lifecycle Functions"  
---
More content...

---
title: "Player Centric API - Code"
---
Even more content...
```

**After** (Single document with proper hierarchy):
```markdown
# Player Centric API - Overview

Content here...

## Player Centric API - Lifecycle Functions

More content...

## Player Centric API - Code

Even more content...
```

**Header Hierarchy Rules**:
- **H1 (`#`)**: Document title only (one per file)
- **H2 (`##`)**: Major sections
- **H3 (`###`)**: Subsections
- **H4 (`####`)**: Sub-subsections
- Never skip header levels (e.g., don't go from H2 directly to H4)

### 2. Convert Block Quotes to MkDocs Callouts

**Identify**: Look for sections starting with `>` (block quotes)

**Convert based on emoji/content type**:

- `> 📘` → `!!! info "Title"`
- `> 🚧` → `!!! warning "Title"`
- `> ❗️` → `!!! danger "Title"`

**Example Conversion**:

**Before**:
```markdown
> 📘 Compatibility
> 
> • Beamable supports Unity versions 2021.3 to 2023.3
> • Beamable supports Windows, Mac, iOS, Android platforms
```

**After**:
```markdown
!!! info "Compatibility"

    • Beamable supports Unity versions 2021.3 to 2023.3
    • Beamable supports Windows, Mac, iOS, Android platforms
```

### 3. Remove ReadMe.io HTML Blocks

**Identify**: Look for `[block:html]` sections

**Action**: Remove entire blocks as they contain ReadMe.io-specific CSS that won't work in MkDocs

**Example**:
```markdown
[block:html]
{
  "html": "<style>\n  .aInCallout\n  {\n    text-decoration:underline !important;\n  }\n</style>"
}
[/block]
```
→ **DELETE ENTIRELY**

### 4. Convert Parameter Tables

**Identify**: Look for `[block:parameters]` sections

**Convert**: Transform JSON-structured tables to standard markdown tables

**Example Conversion**:

**Before**:
```markdown
[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Detail",
    "0-0": "Customer Alias",
    "0-1": "Enter studio name",
    "1-0": "Game Name",
    "1-1": "Enter game project name"
  },
  "cols": 2,
  "rows": 2
}
[/block]
```

**After**:
```markdown
| Field | Detail |
|-------|--------|
| Customer Alias | Enter studio name |
| Game Name | Enter game project name |
```

### 5. Convert [block:image] Blocks to Standard Markdown Images

**Identify**: Look for `[block:image]` sections containing JSON-structured image data

**Process**:
1. **Extract the image URL** from the JSON structure (first element in the "image" array)
2. **Check if image exists** in `docs/media/imgs/` directory
3. **Download if missing** using curl with a descriptive filename
4. **Convert to standard markdown** image syntax

**Example Conversion**:

**Before**:
```markdown
[block:image]
{
"images": [
{
"image": [
"https://files.readme.io/cc24bbf-Screenshot_2024-06-12_at_5.00.58_PM.png",
"",
""
],
"align": "center"
}
]
}
[/block]
```

**Steps**:
1. Extract URL: `https://files.readme.io/cc24bbf-Screenshot_2024-06-12_at_5.00.58_PM.png`
2. Check if image exists in `docs/media/imgs/`
3. If not found, download with descriptive name:
   ```bash
   curl -o "docs/media/imgs/realm-selector-screenshot.png" "https://files.readme.io/cc24bbf-Screenshot_2024-06-12_at_5.00.58_PM.png"
   ```
4. Convert to markdown:

**After**:
```markdown
![Realm Selector](../../media/imgs/realm-selector-screenshot.png)
```

**Image Naming Convention**:
- Use descriptive, kebab-case filenames
- Include context from surrounding content
- Examples:
  - `realm-selector-screenshot.png`
  - `config-defaults-save-button.png`
  - `build-environments-config-files.png`

**Common [block:image] Patterns**:

**Single Image**:
```markdown
[block:image]
{
"images": [
{
"image": ["URL", "alt-text", "caption"],
"align": "center"
}
]
}
[/block]
```
→ `![Alt Text](../../media/imgs/filename.png)`

**Multiple Images** (convert each separately):
```markdown
[block:image]
{
"images": [
{
"image": ["URL1", "", ""],
"align": "left"
},
{
"image": ["URL2", "", ""],
"align": "right"
}
]
}
[/block]
```
→ 
```markdown
![Image 1](../../media/imgs/filename1.png)

![Image 2](../../media/imgs/filename2.png)
```

**Download Script Example**:
```bash
# Extract image URL from [block:image]
# Download with descriptive filename
curl -o "docs/media/imgs/unity-editor-realm-selector.png" "https://files.readme.io/cc24bbf-Screenshot_2024-06-12_at_5.00.58_PM.png"

# Verify download
ls -la docs/media/imgs/unity-editor-realm-selector.png
```

### 6. Replace Placeholder Syntax

**Identify**: Look for `<<TEXT_*>>` and `<<glossary:*>>` placeholders

**Convert**: Replace with appropriate content or plain text

**Common Replacements**:
- `<<TXT_CALLOUT_COMPATIBILITY_TITLE>>` → "Compatibility"
- `<<TXT_BEAMABLE_SUPPORTS>>` → "Beamable supports"
- `<<TXT_OPEN_TOOLBOX_WINDOW>>` → "Open the Beamable Toolbox Window by clicking the Beamable button in the Unity toolbar."
- `<<glossary:Login>>` → "Login"
- `<<glossary:PlayerId>>` → "PlayerId"
- `<<TXT_GOTCHAS>>` → "Here are some common issues and solutions:"

### 7. Convert Links and Remove Special Attributes

**Identify**: HTML anchor tags with special classes

**Example Conversion**:

**Before**:
```html
<a href="https://www.beamable.com/pricing" class="aInCallout" target="_blank">choosing a plan</a>
```

**After**:
```markdown
[choosing a plan](https://www.beamable.com/pricing)
```

### 8. Download External Images and Use Local References

**Process for each external image**:

1. **Identify external image URLs** (typically ReadMe.io hosted)
2. **Download images** using curl:
   ```bash
   curl -o "docs/media/imgs/descriptive-filename.png" "https://external-url.com/image.png"
   ```
3. **Update markdown references**:
   ```markdown
   ![Alt Text](../../media/imgs/descriptive-filename.png)
   ```

**Example**:

**Before**:
```markdown
![Import Package](https://files.readme.io/f7a8964-step-1.png)
```

**Commands**:
```bash
curl -o "docs/media/imgs/step-1-import-package.png" "https://files.readme.io/f7a8964-step-1.png"
```

**After**:
```markdown
![Import Package](../../media/imgs/step-1-import-package.png)
```

### 9. Clean Up HTML Elements

**Remove or Convert**:
- `<br />` tags (use line breaks instead)
- Custom HTML styling
- ReadMe.io-specific attributes

### 10. Fix Table Formatting

**Ensure proper markdown table syntax**:
- Headers separated by `|`
- Header row followed by separator row with `|------|`
- Consistent column alignment
- Handle multi-line content with `<br>` tags where needed

## Quality Checklist

After conversion, verify:

- [ ] **ReadMe.io header metadata removed and replaced with proper H1 markdown header**
- [ ] All block quotes converted to appropriate callouts
- [ ] All ReadMe.io HTML blocks removed
- [ ] All parameter tables converted to markdown tables
- [ ] All placeholder syntax replaced with actual content
- [ ] All external images downloaded and referenced locally
- [ ] **All image paths use correct relative paths based on file location depth**
- [ ] All HTML links converted to markdown format
- [ ] All `<br />` tags removed or replaced with proper line breaks
- [ ] Tables have proper markdown syntax
- [ ] No ReadMe.io-specific syntax remains

## File Structure Considerations

### Image Organization
- Store all images in `docs/media/imgs/` folder
- Use descriptive filenames (e.g., `step-1-import-package.png`)
- **CRITICAL: Calculate correct relative paths based on file location depth**

### Calculating Correct Relative Paths to Images

**Important**: The relative path to `media/imgs/` depends on how deep your markdown file is nested within the `docs/` folder structure.

**Path Calculation Formula**:
- Count the number of folder levels from your `.md` file to the `docs/` root
- Use that many `../` segments to go back to the docs root
- Then add `media/imgs/filename.png`

**Examples by File Location**:

**Level 1** - Files directly in `docs/` folder:
```
docs/
├── index.md                    → media/imgs/filename.png
└── media/imgs/filename.png
```
Path: `media/imgs/filename.png`

**Level 2** - Files one folder deep:
```
docs/
├── unity/
│   └── getting-started.md      → ../media/imgs/filename.png
└── media/imgs/filename.png
```
Path: `../media/imgs/filename.png`

**Level 3** - Files two folders deep:
```
docs/
├── unity/
│   └── user-reference/
│       └── overview.md         → ../../media/imgs/filename.png
└── media/imgs/filename.png
```
Path: `../../media/imgs/filename.png`

**Level 4** - Files three folders deep:
```
docs/
├── unity/
│   └── user-reference/
│       └── editor-systems/
│           └── builds-environments.md → ../../../media/imgs/filename.png
└── media/imgs/filename.png
```
Path: `../../../media/imgs/filename.png`

**Level 5** - Files four folders deep:
```
docs/
├── unity/
│   └── user-reference/
│       └── editor-systems/
│           └── subsection/
│               └── detail.md   → ../../../../media/imgs/filename.png
└── media/imgs/filename.png
```
Path: `../../../../media/imgs/filename.png`

**Quick Reference Table**:

| File Depth | Relative Path Pattern | Example File Location |
|-------------|----------------------|----------------------|
| 1 level | `media/imgs/` | `docs/index.md` |
| 2 levels | `../media/imgs/` | `docs/unity/overview.md` |
| 3 levels | `../../media/imgs/` | `docs/unity/user-reference/index.md` |
| 4 levels | `../../../media/imgs/` | `docs/unity/user-reference/editor-systems/builds-environments.md` |
| 5 levels | `../../../../media/imgs/` | `docs/unity/user-reference/editor-systems/subsection/detail.md` |

**How to Count Levels**:
1. Start from the `docs/` folder (this is level 0)
2. Count each folder you go into as +1 level
3. Your markdown file's level = number of `../` needed

**Example Walkthrough**:
For file: `docs/unity/user-reference/editor-systems/builds-environments.md`
- `docs/` (level 0 - root)
- `unity/` (level 1)
- `user-reference/` (level 2) 
- `editor-systems/` (level 3)
- `builds-environments.md` (level 4)

Result: Need 3 `../` to get back to docs root → `../../../media/imgs/filename.png`

**Common Mistakes to Avoid**:
- ❌ Using `../../media/imgs/` for all files (only works for level 3)
- ❌ Not counting the file's own folder level
- ❌ Forgetting to update paths when moving files to different depths

**Verification Method**:
After conversion, always verify that:
1. The path correctly navigates to the `docs/media/imgs/` folder
2. The image file actually exists in that location
3. The relative path works from the markdown file's location
