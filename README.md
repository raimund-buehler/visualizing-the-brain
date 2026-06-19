# Visualizing the Brain

A beginner-friendly neuroscience outreach project for motivated students aged 13-14. The workshop introduces MRI and fMRI visualization with Python, using short guided notebooks that run in Google Colab.

The current workshop has two notebooks, each designed for about two hours. English and German versions are available.

## Open in Colab

### English

**Day One: From Brain Images to a First fMRI Comparison**

[![Open Day One in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raimund-buehler/visualizing-the-brain/blob/main/notebooks/day_one.ipynb)

**Day Two: Ask Your Own Brain Question**

[![Open Day Two in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raimund-buehler/visualizing-the-brain/blob/main/notebooks/day_two.ipynb)

### Deutsch

**Tag Eins: Von Gehirnbildern zu einem ersten fMRT-Vergleich**

[![Tag Eins in Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raimund-buehler/visualizing-the-brain/blob/main/notebooks/day_one_de.ipynb)

**Tag Zwei: Stellt eure eigene Gehirnfrage**

[![Tag Zwei in Colab öffnen](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raimund-buehler/visualizing-the-brain/blob/main/notebooks/day_two_de.ipynb)

## Notebook Overview

| Notebook | Language | Purpose |
| --- | --- | --- |
| `notebooks/day_one.ipynb` | English | Introduction to Jupyter, voxels, MRI/fMRI data shapes, slices, time series, plotting, and one guided first-level contrast. |
| `notebooks/day_one_de.ipynb` | German | German version of day one with the same structure and runnable code examples. |
| `notebooks/day_two.ipynb` | English | Guided notebook where students choose a contrast, make a prediction, run a first-level analysis, plot the result, and interpret it carefully. |
| `notebooks/day_two_de.ipynb` | German | German version of day two with the same structure and guided discussion prompts. |

## Learning Goals

By the end of the two notebooks, students should be able to:

- explain that brain images are arrays of numbers made from voxels,
- describe slices, 3D volumes, 4D fMRI data, and voxel time series,
- navigate anatomical and functional brain images with Nilearn plots,
- explain that fMRI reflects blood-oxygen-related signal changes, not thoughts directly,
- understand why task conditions need to be compared with contrasts,
- run a simple first-level fMRI contrast for one participant,
- interpret warm and cool colors in a contrast map,
- describe approximate brain locations using side, height, front/back position, and lobes,
- explain why some fMRI contrasts are easier to interpret than others.

The English and German notebooks are intended to match each other in structure. Code cells are runnable examples, and student work is guided through discussion prompts.

## Setup: Google Colab

1. Open Google Colab: <https://colab.research.google.com/>
2. Open one of the Colab links above, or upload one of the notebooks in `notebooks/`.
3. Run the first code cell to install the required packages.
4. Run each notebook cell from top to bottom.

Colab is recommended for the workshop because students do not need to install Python on their own computers.

## Setup: Local Use

Local setup is optional. It is useful for teachers, helpers, or students who already have Python installed.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. Start Jupyter:

   ```bash
   jupyter notebook
   ```

4. Open one of the notebooks in `notebooks/` and run it from top to bottom.

## Workshop Outline: 2 Days / 4 Hours

### Day 1: From Brain Images to a First fMRI Comparison

- Learn how to run a Jupyter notebook.
- Load an anatomical brain template.
- Inspect a brain image as a 3D array of numbers.
- Understand voxels, slices, volumes, and 4D fMRI data.
- Plot anatomical and functional images.
- Explore a voxel time series.
- Connect fMRI signal to task timing.
- Run one guided first-level contrast: right-hand button presses compared with left-hand button presses.
- Interpret the result using motor cortex, the homunculus, and contralaterality.

### Day 2: Ask Your Own Brain Question

- Choose a task contrast from the localizer experiment.
- Make a prediction before looking at the result.
- Fit a first-level model for one participant.
- Compute and plot the chosen contrast.
- Interpret warm and cool colors.
- Report approximate location, lobe, and possible function for the strongest clusters.
- Discuss why some contrasts are scientifically cleaner than others.
- Prepare a short group explanation of the analysis and its limits.

## Current Scope

This project does not include decoding, machine learning, advanced preprocessing, or full group-level fMRI analysis. The goal is to make basic MRI/fMRI visualization and first-level contrast analysis understandable, interactive, and safe for beginners.
