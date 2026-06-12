# Visualizing the Brain

A beginner-friendly neuroscience outreach project for a small group of motivated students aged 13-14. The first milestone is an accessible introduction to MRI, fMRI, voxels, and basic brain visualization using Python.

The project starts in Google Colab and should also run locally when the required Python packages are installed.

## Open in Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raimund-buehler/visualizing-the-brain/blob/main/notebooks/day_one.ipynb)

## Learning Goals

By the end of this first notebook, students should be able to:

- Explain the basic idea of MRI as a way to make pictures of the inside of the body.
- Explain that fMRI measures changes related to blood oxygen, not thoughts directly.
- Recognize that a brain image is made of many tiny 3D blocks called voxels.
- Load a standard brain template with Python.
- Visualize brain slices from different directions.
- Explore how brain slices change when moving through x, y, and z coordinates.

## Setup: Google Colab

1. Open Google Colab: <https://colab.research.google.com/>
2. Upload or open `notebooks/day_one.ipynb`.
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

4. Open `notebooks/day_one.ipynb` and run it from top to bottom.

## Workshop Outline: 3 Days / 12 Hours

### Day 1: What Is Brain Imaging?

- Welcome and project overview.
- What is MRI?
- What is fMRI?
- First look at a standard brain template.
- Hands-on activity: viewing brain slices.

### Day 2: Exploring the Brain in 3D

- Review: images, slices, and voxels.
- Explore x, y, and z coordinates.
- Use a clickable viewer to move through the brain.
- Student challenge: find symmetrical slices and describe changes.

### Day 3: From Pictures to Questions

- Discuss what brain images can and cannot tell us.
- Compare anatomy and activity at a simple conceptual level.
- Reflection: why fMRI is not mind reading.
- Group discussion: what could we visualize next?

## Current Scope

This project does not include decoding, machine learning, or advanced fMRI preprocessing yet. The first goal is to make brain visualization understandable, interesting, and safe for beginners.
