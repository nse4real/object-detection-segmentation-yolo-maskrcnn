\# Modern Object Detection \& Segmentation

\### YOLOv8 vs Mask R-CNN — Architectural Comparison



\## Overview

This project explores modern computer vision approaches for \*\*object detection\*\* and \*\*instance segmentation\*\*, using pre-trained models to focus on \*\*architectural understanding rather than model training\*\*.



The work compares:

\- \*\*YOLOv8\*\* (single-stage detection and segmentation)

\- \*\*Mask R-CNN\*\* (two-stage instance segmentation)



The emphasis is on:

\- Output structures

\- Computational trade-offs

\- Memory and performance implications

\- Practical constraints on modest GPU hardware



---



\## Objectives

\- Run state-of-the-art detection and segmentation models on real images

\- Inspect and compare model outputs programmatically

\- Understand architectural differences between:

&nbsp; - Classification

&nbsp; - Detection

&nbsp; - Segmentation

\- Contrast \*\*single-stage\*\* vs \*\*two-stage\*\* segmentation pipelines



---



\## Models Used



\### YOLOv8 (Ultralytics)

\- Detection: bounding boxes, class labels, confidence scores

\- Segmentation: per-object pixel masks over the image grid

\- Single forward pass with Non-Max Suppression (NMS)



\### Mask R-CNN (Torchvision)

\- Two-stage pipeline:

&nbsp; 1. Region Proposal Network (RPN)

&nbsp; 2. RoI Align + classification, box regression, and mask heads

\- Predicts \*\*per-region masks\*\* rather than global image masks



---



\## Key Architectural Insights

\- \*\*Detection requires NMS\*\* because multiple overlapping boxes are predicted per object

\- \*\*Segmentation scales poorly with image resolution\*\* due to per-pixel masks

\- YOLO prioritises throughput and simplicity

\- Mask R-CNN prioritises structured reasoning and per-object processing

\- GPU memory constraints strongly influence model and input choices



---



\## Project Structure

```text

scripts/

&nbsp; inspect\_yolo.py

&nbsp; inspect\_seg.py

&nbsp; run\_mask\_rcnn\_cpu.py

data/

&nbsp; sample\_images/

docs/

outputs/ (ignored in git)

