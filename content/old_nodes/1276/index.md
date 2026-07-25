---
title: "Improving combinatorial optimization"
date: 2026-07-25T15:04:37+0200
draft: false
---

### Author

Geoffrey G Chu

### School

The University of Melbourne, Australia

### Supervisors

Peter J Stuckey

### Abstract

Combinatorial Optimization is an important area of computer science that has many theoretical and practical applications. In this thesis, we present important contributions to several different areas of combinatorial optimization, including nogood learning, symmetry breaking, dominance, relaxations and parallelization.

We develop a new nogood learning technique based on constraint projection that allows us to exploit subproblem dominances that arise when two different search paths lead to subproblems which are identical on the remaining unlabeled variables. On appropriate problems, this nogood learning technique provides orders of magnitude speedup compared to a base solver which does not learn nogoods.

We present a new symmetry breaking technique called SBDS-1UIP, which is an extension of Symmetry Breaking During Search (SBDS). SBDS-1UIP uses symmetric versions of the 1UIP nogoods derived by Lazy Clause Generation solvers to prune symmetric parts of the search space. We show that SBDS-1UIP can exploit at least as many symmetries as SBDS, and that it is strictly more powerful on some problems, allowing us to exploit types of symmetries that no previous general symmetry breaking technique is capable of exploiting.

We present two new general methods for exploiting almost symmetries (symmetries which are broken by a small number of constraints). The first is to treat almost symmetries as conditional symmetries and exploit them via conditional symmetry breaking constraints. The second is to modify SDBS-1UIP to handle almost symmetries. Both techniques are capable of producing exponential speedups on appropriate problems.

We examine three reasonably well known problems: the Minimization of Open Stacks Problem, the Talent Scheduling Problem (CSPLib prob039), and the Maximum Density Still Life Problem (CSPLib prob032). By applying various powerful techniques such as nogood learning, dynamic programming, dominance and relaxations, we are able to solve these problems many orders of magnitude faster than the previous state of the art.

We identify cache contention as a serious bottleneck that severely limit the amount of speedup achievable when parallelizing SAT and LCG solvers on multi-core systems. We alter the data structures used in the state of the art SAT solver MiniSat to be more cache aware, leading to a sequential SAT solver that is some 80% faster on average and a parallel SAT solver that is some 140% faster on average.

We examine an important issue in parallel search that has not been properly addressed in the literature. Many work stealing schemes used for load balancing completely ignore the branching heuristic, and instead try to maximize the granularity of the work stolen. This can result in many of the processors searching in unfruitful parts of the search tree. We analyze this problem and develop a new work stealing scheme called confidence based work stealing, which partitions the work based on how strong the branching heuristic is at each node. The new parallel algorithm produced near linear or super linear speedup on all the problems we tested.

### Graduated

Saturday, October 1, 2011 - 12:00

### Link to full text

[Melbourne University Institutional Repository](https://minerva-access.unimelb.edu.au/handle/11343/36679)