# CSC420 – Assignment 4: Geometry, Homography & Tracking

Individual assignment for University of Toronto's CSC420 (Introduction to Image Understanding), covering RANSAC sample-count theory, projective camera geometry (vanishing points), homogeneous-coordinate line/point duality, and implementations of image-to-image homography estimation and Mean-Shift face tracking.

## Layout

- **`a4-writeup.tex` / `.pdf`** — the report (Part I theory + Part II implementation results), with the numbered figures (`4.*.png`, `5.*.png`).
- **`assignment4/`** — the implementation notebook and its inputs: three hallway photos (`hallway1/2/3.jpg`), a face-tracking video (`KylianMbappe.mp4`), OpenCV's bundled `haarcascade_frontalface_default.xml` (Viola-Jones detector), and a `README.txt`.
- **`pick_points.py`** — a standalone helper script (matplotlib `ginput`) for manually clicking corresponding points on an image, used to build the point correspondences fed into the homography fitting.
- **`assignment4.pdf`** — the assignment handout.

## Part I: Theoretical problems (`a4-writeup.tex`)

- **Q1 — RANSAC**: computes the number of iterations needed for 99.5% confidence fitting a homography ($s=4$ points, 70% inlier rate) → 20 iterations; notes an affine fit needs only $s=3$, so fewer iterations suffice.
- **Q2 — Camera models / vanishing points**: derives the vanishing point of a 3D line under a calibrated camera as $t\to\infty$, then shows that vanishing points of all lines lying on a common plane fall on a single line (the plane's horizon).
- **Q3 — Homogeneous coordinates**: proves the line-through-two-points and intersection-of-two-lines duality via the cross product ($l = p\times p'$, $p = l\times l'$).

## Part II: Implementation (`assignment4/a4_implementation.ipynb`)

- **Q4 — Homography estimation**: for three hallway-image pairs (Case A: same wall, similar position/different orientation; Cases B/C: same wall and floor, different camera position), manually picked point correspondences are used to fit a homography, decomposed into its scale/translation/shear components, then used to warp and merge the image pairs. Observes parallax appears only when camera *position* differs (not orientation), and that the right wall is closer to Lambertian than the floor.
- **Q5 — Mean-Shift tracking**: tracks a face across `KylianMbappe.mp4` using Mean-Shift on a color histogram, initialized from a Viola-Jones (Haar cascade) detection, and evaluates tracking quality via IoU against the detector's own boxes per frame (97.3% of frames >50% IoU in the baseline run). A second variation of the tracker is compared the same way (85.1% of frames >50% IoU). Notes Mean-Shift keeps tracking through frames where Viola-Jones fails to detect the face (partial occlusion/orientation change).

## Author

Zixuan Zeng
