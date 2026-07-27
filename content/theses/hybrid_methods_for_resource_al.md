---
aliases:
  - /old_nodes/1057
title: "Hybrid Methods for Resource Allocation and Scheduling Problems in Deterministic and Stochastic Environments"
draft: false
---

### Author

Michele Lombardi

### School

University of Bologna

### Supervisors

Michela Milano

### Abstract

This work presents exact, hybrid algorithms for mixed resource Allocation and Scheduling problems; in general terms, those consist into assigning over time finite capacity resources to a set of precedence connected activities.

The proposed methods have broad applicability, but are mainly motivated by applications in the field of Embedded System Design. In particular, high-performance embedded computing recently witnessed the shift from single CPU platforms with application-specific accelerators to programmable Multi Processor Systems-on-Chip (MPSoCs). Those allow higher flexibility, real time performance and low energy consumption, but the programmer must be able to effectively exploit the platform parallelism. This raises interest in the development of algorithmic techniques to be embedded in CAD tools; in particular, given a specific application and platform, the objective if to perform optimal allocation of hardware resources and to compute an execution schedule.

On this regard, since embedded systems tend to run the same set of applications for their entire lifetime, off-line, exact optimization approaches are particularly appealing. Quite surprisingly, the use of exact algorithms has not been well investigated so far; this is in part motivated by the complexity of integrated allocation and scheduling, setting tough challenges for “pure” combinatorial methods. The use of hybrid CP/OR approaches presents the opportunity to exploit mutual advantages of different methods, while compensating for their weaknesses.

In this work, we consider in first instance an Allocation and Scheduling problem over the Cell BE processor by Sony, IBM and Toshiba; we propose three different solution methods, leveraging decomposition, cut generation and heuristic guided search. Next, we face Allocation and Scheduling of so-called Conditional Task Graphs, explicitly accounting for branches with outcome not known at design time; we extend the CP scheduling framework to effectively deal with the introduced stochastic elements. Finally, we address Allocation and Scheduling with uncertain, bounded execution times, via conflict based tree search; we introduce a simple and flexible time model to take into account duration variability and provide an efficient conflict detection method.
The proposed approaches achieve good results on practical size problems, thus demonstrating the use of exact approaches for system design is feasible. Furthermore, the developed techniques bring significant contributions to combinatorial optimization methods.

### Graduated

Thursday, April 1, 2010 - 12:00

### Notes

This work received a honorable mention at the CP Doctoral Research Award in 2011