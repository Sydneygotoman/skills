---
name: obsidian
description: Build and maintain a local-first Obsidian knowledge vault - capture sources with citations, write connected notes, answer questions strictly from vault evidence, and keep the vault healthy. Use for set up an Obsidian vault, second brain, ingest this source into my notes, save this to my vault, query my wiki, or check my vault for dead links and orphan pages.
---

# Obsidian Vault Manager

Turn scattered source material and conversation answers into a linked,
citation-backed Obsidian vault, and answer future questions from that vault
instead of re-deriving them from scratch. The vault is a normal folder of
Markdown files that the user owns - never a hidden cache or a database only
Claude can read.

This skill distills the workflow of the open-source
[claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) project
(MIT license, by AgriciDaniel). If that project is installed locally, prefer
its `scripts/claude-obsidian.py` core for transactional writes, link linting,
and BM25 retrieval - it is more rigorous than the manual steps below. If it
is not installed, follow the manual workflow directly against the vault's
Markdown files.

## When to Use This Skill

- Setting up a new Obsidian vault (or adopting an existing one) as a
  persistent knowledge base for a project, topic, or research area.
- Ingesting a source (pasted text, a local file, or an approved URL) into
  cited, cross-linked vault notes.
- Saving a specific answer, decision, or insight from the current
  conversation into the vault on explicit request.
- Answering a question strictly from what is already in the vault, without
  inventing facts the vault doesn't support.
- Auditing vault health - dead links, orphan pages, missing frontmatter.

## What This Skill Does

1. **Capture with context**: Stage incoming sources in a visible `inbox/`
   folder and keep an unmodified copy before writing any note derived from
   them.
2. **Ground every claim**: Every non-obvious claim in a generated note
   carries a link or citation back to the source it came from. Claims the
   sources don't support are marked as such instead of smoothed over.
3. **Connect the knowledge**: New notes link to related existing notes,
   and get referenced from an index or Map of Content (MOC) page so nothing
   becomes an orphan.
4. **Answer from evidence**: When asked to query the vault, read the
   relevant notes and answer only from what they contain, citing which note
   supported which claim.
5. **Keep it healthy**: On request, scan for dead links, orphan pages, and
   notes missing required frontmatter (e.g. `title`).

## How to Use

### Basic Usage

```
Set up an Obsidian vault at ~/Documents/ResearchVault for my competitor
research.
```
Confirm the target folder, then create it with a `wiki/` folder for notes,
`wiki/index.md` as the entry point, and `inbox/` for staged sources.

```
Ingest inbox/pricing-report.pdf into the vault.
```
Read the source, extract the material worth keeping, write one or more
notes under `wiki/` with citations back to the source file, and link the
new notes from the relevant index or MOC page. Leave the original file in
`inbox/` untouched.

```
Save that last answer to my vault under "Q3 pricing decision".
```
Only save the scope the user pointed at - never the whole transcript.
Check whether a note with that title already exists and update it instead
of creating a duplicate if so.

```
What does my vault say about competitor pricing?
```
Read `wiki/index.md`, follow links to the pages that actually cover the
topic, and answer from their content only. State explicitly if the vault
doesn't have an answer instead of falling back to general knowledge.

### Advanced Usage

```
Check my vault for dead links and orphan pages.
```
Walk every Markdown file under `wiki/`, parse `[[wikilinks]]` and
`[Markdown links](...)`, and report: links that point to nonexistent
notes, notes no other note links to, and notes missing required
frontmatter. This is a report only - don't auto-fix findings without
asking.

```
Research "vector database options" and file a cited summary in the vault.
```
Only fetch external sources with explicit consent on domains and scope.
Draft a cited summary, show it to the user, and only write it into the
vault after they approve filing it - findings from the web don't become
vault knowledge automatically.

## Example

**User**: "Ingest this article into my vault and link it from my AI-tools MOC."

**Output**:
```
Created wiki/sources/anthropic-mcp-announcement.md
  - 3 claims cited to the article
Updated wiki/moc-ai-tools.md
  - added link to the new note
inbox/mcp-article.html left unchanged as the source of record
```
