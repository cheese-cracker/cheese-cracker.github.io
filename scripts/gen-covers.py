#!/usr/bin/env python3
"""Seeded Delaunay-triangulation cover art, one SVG per slug. No deps.

Same motif as the site's live Voronoi field, baked at og:image size so posts
without a photo still get a social card. Deterministic: slug -> same art.
"""
import math, sys, pathlib

W, H = 1200, 630
BG, EDGE, DOT = "#1d1e20", "#7aa2f7", "#9ece6a"


def rng(seed):
    h = 2166136261
    for c in seed:
        h ^= ord(c); h = (h * 16777619) & 0xFFFFFFFF
    def nxt():
        nonlocal h
        h ^= (h >> 15); h = (h * 2246822507) & 0xFFFFFFFF
        h ^= (h >> 13); h = (h * 3266489909) & 0xFFFFFFFF
        h &= 0xFFFFFFFF
        return h / 0x100000000
    return nxt


def circumcircle(a, b, c):
    ax, ay = a; bx, by = b; cx, cy = c
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if abs(d) < 1e-12:
        return None
    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
    return (ux, uy), math.dist((ux, uy), a)


def delaunay(pts):
    """Bowyer-Watson."""
    st = [(-4 * W, -4 * H), (4 * W, -4 * H), (0, 4 * H)]
    tris = [tuple(st)]
    for p in pts:
        bad = []
        for t in tris:
            cc = circumcircle(*t)
            if cc and math.dist(cc[0], p) <= cc[1]:
                bad.append(t)
        edges = {}
        for t in bad:
            for e in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
                k = tuple(sorted(e))
                edges[k] = edges.get(k, 0) + 1
        tris = [t for t in tris if t not in bad]
        for (u, v), n in edges.items():
            if n == 1:
                tris.append((u, v, p))
    return [t for t in tris if not any(v in st for v in t)]


def cover(slug, out):
    r = rng(slug)
    pts = [(r() * W, r() * H) for _ in range(46)]
    tris = delaunay(pts)
    seen, lines = set(), []
    for t in tris:
        for a, b in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
            k = tuple(sorted((a, b)))
            if k in seen:
                continue
            seen.add(k)
            lines.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/>')
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4"/>' for x, y in pts)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
        f'<rect width="{W}" height="{H}" fill="{BG}"/>'
        f'<g stroke="{EDGE}" stroke-width="1.2" stroke-opacity=".45" fill="none">{"".join(lines)}</g>'
        f'<g fill="{DOT}" fill-opacity=".75">{dots}</g>'
        f'</svg>'
    )
    pathlib.Path(out).write_text(svg)
    return len(tris)


if __name__ == "__main__":
    for slug in sys.argv[1:]:
        n = cover(slug, f"static/covers/{slug}.svg")
        print(f"{slug:20} {n} triangles -> static/covers/{slug}.svg")
