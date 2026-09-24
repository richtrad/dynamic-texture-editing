"""Create the conservative typo-only working copy from the archival source."""

from __future__ import annotations

from pathlib import Path


root = Path(__file__).resolve().parents[1]
source = root / "original" / "15sccg_v_fin_v2.tex"
target = Path(__file__).resolve().parent / "15sccg_v_fin_v2_typos.tex"

# These are mechanical spelling or unmistakable local grammar fixes. The
# archival source is never modified, and ambiguous technical sentences are
# deliberately excluded.
replacements = [
    ("QA fast  simple method", "A fast, simple method"),
    ("can by  applied", "can be applied"),
    ("can by done", "can be done"),
    ("as as a realization", "as a realization"),
    ("temporaly", "temporally"),
    ("samplig", "sampling"),
    ("of consists time consuming", "or consists of time-consuming"),
    ("featues", "features"),
    ("adventage", "advantage"),
    ("parellely analyzed", "analyzed in parallel"),
    ("Ftom", "From"),
    ("Teporal jumps", "Temporal jumps"),
    ("promary", "primary"),
    ("demaged", "damaged"),
    ("unwainted", "unwanted"),
    ("ilustrated", "illustrated"),
    ("horisontal", "horizontal"),
    ("respectivelly", "respectively"),
    ("aditional", "additional"),
    ("Harlick", "Haralick"),
    ("rectangular shepe", "rectangular shape"),
    ("dhet the convolution", "then the convolution"),
    ("time indices od pixels", "time indices of pixels"),
    ("many inconsistence in", "many inconsistencies in"),
]

text = source.read_text(encoding="utf-8")
counts: list[tuple[str, str, int]] = []
for old, new in replacements:
    count = text.count(old)
    if count:
        text = text.replace(old, new)
        counts.append((old, new, count))

target.write_text(text, encoding="utf-8")
log = [
    "# Typo-only source working copy",
    "",
    "Generated from `source/original/15sccg_v_fin_v2.tex`. The archival source",
    "is unchanged. Only the listed mechanical corrections were applied; no",
    "equation, number, citation key, figure, table, or experimental claim was",
    "changed. Ambiguous prose remains for author review.",
    "",
    "| Original | Replacement | Occurrences |",
    "| --- | --- | ---: |",
]
log.extend(f"| `{old}` | `{new}` | {count} |" for old, new, count in counts)
log.extend(
    [
        "",
        "The file still references the historical class, image directory, and",
        "bibliography described in `source/original/SOURCE_INFO.md`; it is not a",
        "self-contained build until those dependencies are recovered.",
    ]
)
(target.parent / "CHANGELOG.md").write_text("\n".join(log) + "\n", encoding="utf-8")
print(f"wrote {target}")
print(f"applied {len(counts)} replacement rules")
