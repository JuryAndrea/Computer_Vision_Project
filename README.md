# Computer Vision Project

## Project Overview

:warning: This repository was created for the CVPR course project. 

:no_entry_sign: It is not intended for reuse.

:heart: Special thanks to my team [Christian Altrichter](https://github.com/Altricch) and [Francesco Huber](https://github.com/Frakk0) for their contributions.

:white_check_mark: The Jupyter Notebook is self-explanatory and provides detailed explanations and comments within each cell.

## Table of Contents

- [Part 1](#part-1)
  - [Task 1.1](#task-11)
  - [Task 1.2](#task-12)
  - [Task 1.3](#task-13)
  - [Results](#results)
- [Part 2](#part-2)
  - [Task 2.1](#task-21)
  - [Task 2.2](#task-22)
  - [Task 2.3](#task-23)
  - [Results](#results-1)
- [Part 3](#part-3)
  - [Task 3.1](#task-31)
  - [Task 3.2](#task-32)
  - [Task 3.3](#task-33)
  - [Task 3.4](#task-34)
  - [Results](#results-2)
  - [Canonical Results](#canonical-results)
  - [Real Results](#real-results)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Part 1

### Task 1.1
The first task was to identify two sets of parallel lines using:
1. Canny Edge detection
2. Hough transform

### Task 1.2
We manually picked a subset of lines that were supposed to be parallel but were distorted, ensuring they were from the same plane and did not share the same vanishing points.

### Task 1.3
We computed the infinity line by applying the cross product between the two determined points at infinity.

### Results
Affine rectification was applied, preserving the area ratios to determine the size of the door.

## Part 2

### Task 2.1
We manually read the coordinates of the indicated points via Matplotlib.

### Task 2.2
We obtained the projection matrix by deconstructing the equation \( x = PX \) and solving a series of linear equations.

### Task 2.3
The RQ decomposition was applied to obtain the projection matrix components and camera center.

### Results
Projection matrix components for two images were determined.

## Part 3

### Task 3.1
We used the 8-Point-Algorithm to reconstruct the fundamental matrix \( F \).

### Task 3.2
Canonical camera pairs \( \hat{P} \) and \( \hat{P}' \) were composed, and 3D coordinates were estimated using linear triangulation.

### Task 3.3
A 3D homography was obtained by deconstructing the formula \( x' = Hx \).

### Task 3.4
Linear triangulation was applied on new points using the canonical camera pair.

### Results

#### Canonical Results
The canonical camera pair \( \hat{P} \) and \( \hat{P}' \) were used for 3D point estimation.

#### Real Results
The real camera pair \( P \) and \( P' \) were used for 3D point estimation.
