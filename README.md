# RL Implementations

## What is it?

This repo contains a set of notebooks to reproduce reinforcement learning algorithms. 


## Overview
This repo mostly serves (self-)educational purposes. thererfore, the notebooks are mostly self-contained and only general helper functions are outsourced, such that all relevant code is in one place. The models are built using Keras and TensorFlow. The repo is build with TensorFlow 2, however since I was experimenting with TF2 and Keras for the first time, the earlier notebooks might contain some TF1 looking code.

In the process from (paper) --> (implementation) --> (production-grade code) these notebooks lie in the middle. They don't explain the theory in detail (there are plenty of blogs, papers and books one can consult on that subject) but are also not optimized for efficiency and scalability, such that the step from theory to implementation is easy to follow. Heavily optimized code can sometimes obscure the underlying principles of the algorithm which makes it harder to understand it.

The following algorithms are implemented at the moment:

- Vanilla Policy Gradient
- Deep Q-Learning
- Proximal Policy Optimisation

## Installation
The code in the notebooks relies on TensorFlow 2. To install all dependencies run:

```bash
pip install -r requirements.txt
```