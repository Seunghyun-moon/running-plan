# Running Plan — Design System

## Philosophy
Daily training tracker. Data (paces, distances, progress) is the hero — not branding.
Calm, confident, premium-athletic. Apple/Linear-inspired restraint.

## Color Tokens

| Token | Hex | Use |
|---|---|---|
| --bg | #fafafa | Page background — warm off-white |
| --surface | #ffffff | Cards, elevated content |
| --surface-soft | #f5f5f4 | Subtle backgrounds, hover states |
| --border | #e4e4e7 | Default 1px card border |
| --border-soft | #f4f4f5 | Light dividers (between day rows) |
| --border-strong | #d4d4d8 | Hover border, input focus |
| --text | #18181b | Primary text, action color |
| --text-2 | #52525b | Secondary running text |
| --text-3 | #a1a1aa | Muted, captions, metadata |
| --text-4 | #d4d4d8 | Disabled, ghost elements |
| --accent | #18181b | Primary actions — minimalist black |
| --highlight | #ea580c | Race day / today emphasis (sparingly) |
| --highlight-soft | #fff7ed | Race day soft background |

### Workout type colors (used only on pill tags)
- LSD — blue (#2563eb on #eff6ff)
- Interval — red (#dc2626 on #fef2f2)
- Tempo — orange (#ea580c on #fff7ed)
- Jog — green (#16a34a on #f0fdf4)
- Race — filled black
- Rest — gray (#71717a on #f4f4f5)

## Typography
Font: Inter (variable)
- Display headings: 700, tight letter-spacing (-0.5px)
- Body: 400
- Labels / buttons: 500-600
- Numbers (VDOT, distances): 700 with tight tracking

## Shapes
- Buttons: 10px radius
- Cards: 14px radius
- Inputs: 10px radius
- Pills/badges: 9999px (full round)

## Spacing
4px base — 4 / 8 / 12 / 16 / 20 / 24 / 32 / 48 / 64

## Elevation
- Card resting: 1px border only, no shadow
- Card hover: `0 4px 12px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)`
- That's it — no other elevation tiers

## Principles
- Numbers and progress are visually loudest
- One accent (black) for actions — no decorative color
- Workout categorization through subtle pills, not heavy chrome
- Generous internal padding, tighter external gaps (marketplace feel without clutter)
- No UPPERCASE except letter-tracked badges
