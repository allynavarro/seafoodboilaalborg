# Aalborg Seafood Boil — website

## Filer

- `index.html` — den færdige side. Kan åbnes direkte i en browser, eller
  hostes som en almindelig statisk side (fx GitHub Pages, Netlify, Vercel).
- `build_site.py` — kildekoden. Al tekst, HTML, CSS og JavaScript på siden
  bliver genereret herfra. **Ret aldrig i `index.html` direkte** — ændringer
  forsvinder, næste gang siden bygges. Ret i stedet i `build_site.py` og
  byg siden igen.
- `logo-mark.png`, `hero-poster.jpg`, `hero-video.mp4` — billeder/video som
  siden bruger. Skal ligge i samme mappe som `index.html`.

## Sådan bygger du siden igen efter en rettelse

Kræver Python 3 (ingen andre pakker nødvendige).

```bash
python3 build_site.py
```

Det genererer en ny `index.html` ud fra `build_site.py`. Genindlæs siden i
browseren for at se ændringen.

## Sådan åbner du siden i VS Code

1. Pak zip-filen ud, og åbn mappen i VS Code (`File → Open Folder…`).
2. Højreklik på `index.html` og vælg "Open with Live Server" (kræver
   udvidelsen "Live Server"), eller åbn filen direkte i en browser.
3. Rediger `build_site.py`, kør `python3 build_site.py`, og genindlæs.
