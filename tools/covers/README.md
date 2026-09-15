# Cover sources

Regenerate after a palette change (values are inlined; match `assets/css/extended/custom.css`).

- `ch3d-lift.html` → `static/plots/compgeom/ch3d-lift-cover.png` (after DesignMentor's CHVD-3D):
  `google-chrome-stable --headless=new --use-angle=swiftshader --enable-unsafe-swiftshader --window-size=3200,1800 --virtual-time-budget=20000 --screenshot=out2x.png file://$PWD/ch3d-lift.html && magick out2x.png -resize 50% ../../static/plots/compgeom/ch3d-lift-cover.png`
- `poe-isoquant-isocost.svg` → `static/plots/poe-isoquant-isocost-cover.png`:
  `google-chrome-stable --headless=new --window-size=1600,900 --screenshot=../../static/plots/poe-isoquant-isocost-cover.png file://$PWD/poe-isoquant-isocost.svg`
