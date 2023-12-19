# Google TPU

## notes

- VLIW, XLA for the compiler
- tpu v2: Scalar Unit + Vector Unit + Matrix Multiply Unit + Transpose / Permute Unit + Interconnect + HBM, from "HC32 PPT"
- Why 128x128? 平衡的选择, 详细见 paper

- www.doc.ic.ac.uk/~wl/teachlocal/cuscomp/notes/cc07notes.pdf
  Systolic array example

## tpu

- search "TPU" or "google" in [hot_chips.md](./hot_chips.md)

- https://cloud.google.com/tpu?hl=en
- https://cloud.google.com/tpu/docs

- https://cloud.google.com/tpu/docs/v5p-training
  Cloud TPU v5p training

- https://cloud.google.com/tpu/docs/system-architecture-tpu-vm
  TPU v1, v2, v3, v4, v5e arch & tpu papers

- https://cloud.google.com/blog/products/ai-machine-learning/introducing-cloud-tpu-v5p-and-ai-hypercomputer
  Enabling next-generation AI workloads: Announcing TPU v5p and AI Hypercomputer
  December 7, 2023

- https://cloud.google.com/tpu/docs/multislice-introduction
- https://cloud.google.com/blog/products/compute/using-cloud-tpu-multislice-to-scale-ai-workloads
  How to scale AI training to up to tens of thousands of Cloud TPU chips with Multislice
  September 1, 2023

- https://dl.acm.org/doi/10.1145/3579371.3589350
  2023-06-17
  TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings
  Pay attention to references

- https://www.nextplatform.com/2022/10/11/deep-dive-on-googles-exascale-tpuv4-ai-systems/
  2022/10/11
  Deep Dive On Google’s Exascale TPUv4 AI Systems
  TPUv4i on nextplatform

- https://ieeexplore.ieee.org/document/9499913/
  6/2021
  Ten Lessons From Three Generations Shaped Google’s TPUv4i : Industrial Product

- https://www.nextplatform.com/2021/02/16/what-chip-startups-can-learn-from-googles-tpu-design-team/
  2021/02/16
  What Chip Startups Can Learn from Google’s TPU Design Team
  Analysis of the “TPUv2 and TPUv3”

- https://ieeexplore.ieee.org/document/9351692
  09 February 2021
  The Design Process for Google's Training Chips: TPUv2 and TPUv3

- https://www.hc32.hotchips.org/assets/program/conference/day2/HotChips2020_ML_Training_Google_Norrie_Patil.v01.pdf
  2020
  Google’s Training Chips Revealed: TPUv2 and TPUv3
  HC32 PPT

- https://dl.acm.org/doi/10.1145/3360307
  July 2020
  tpu v1 & tpu v2 & tpu v3
  A domain-specific supercomputer for training deep neural networks

- https://link.springer.com/10.1007/978-3-031-01761-2
  2019
  The Datacenter as a Computer: Designing Warehouse-Scale Machines, Third Edition

- http://arxiv.org/abs/1704.04760
  2017-04-16
  In-Datacenter Performance Analysis of a Tensor Processing Unit
  tpu v1

## XLA optimizations for TPU

- https://dl.acm.org/doi/10.1145/3567955.3567959
  2022-12-19
  Overlap Communication with Dependent Computation via Decomposition in Large Deep Learning Models
  OverlapIO

- http://arxiv.org/abs/2211.05102
  2022-11-09
  Efficiently Scaling Transformer Inference

- http://arxiv.org/abs/2105.04663
  2021-12-23
  GSPMD: General and Scalable Parallelization for ML Computation Graphs

- http://arxiv.org/abs/2102.13267
  2021-02-25
  LazyTensor: combining eager execution with domain-specific compilers
  XLA + torch

- http://arxiv.org/abs/2006.16668
  2020-06-30
  GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding

- http://arxiv.org/abs/2004.13336
  2020-04-28
  Automatic Cross-Replica Sharding of Weight Update in Data-Parallel Training
  for mlperf v0.6
