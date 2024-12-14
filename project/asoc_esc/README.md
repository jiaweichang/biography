# Multi-Level Transfer Learning Using Incremental Granularities (mLTL-IG)

This repository contains the source code and related resources for the paper:

**"Multi-Level Transfer Learning Using Incremental Granularities for Environmental Sound Classification and Detection"**

Accepted by *Applied Soft Computing Journal* in Dec 2024.  
Authors: Jia-Wei Chang, Hao-Shang Ma, Zhong-Yun Hu  

---

## Overview

Environmental Sound Classification (ESC) tasks often face challenges related to limited computational resources on edge devices and data scarcity. This work introduces a novel **Multi-Level Transfer Learning Using Incremental Granularities (mLTL-IG)** framework, which:

- Enhances the performance of small pre-trained models.
- Utilizes multi-level granular audio features.
- Incorporates an **adaptive average pooling layer** for processing varying input sizes.
- Validates the framework using **ESC-50**, **ESC-10**, and a custom **Chainsaw Dataset**.

The proposed framework achieves up to **6.45% accuracy improvement on the ESC-50 dataset** and **8.6% improvement on the Chainsaw dataset**, demonstrating its effectiveness for resource-constrained devices.

---

## Features

- Multi-Level Transfer Learning (mLTL) across granular audio segments (1s, 3s, and 5s).
- Models supported:
  - LeNet-based adaptive model
  - ResNet-based adaptive model
  - MobileNet-based adaptive model
- Supports both **classification** and **detection** tasks for environmental sound datasets.
- Easily extendable for new datasets and models.

---

## Datasets
This repository supports the following datasets:

ESC-50 Dataset: A benchmark dataset for environmental sound classification.
ESC-10 Dataset: A subset of ESC-50 for simplified tasks.
Chainsaw Dataset: A custom dataset collected for chainsaw sound detection.

---

## Citation
If you use this code, please cite our paper:

@article{chang2024mltl,
  title={Multi-Level Transfer Learning Using Incremental Granularities for Environmental Sound Classification and Detection},
  author={Chang, Jia-Wei and Ma, Hao-Shang and Hu, Zhong-Yun},
  journal={Applied Soft Computing},
  year={2024},
}

