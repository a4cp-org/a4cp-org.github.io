---
title: "Decision Diagrams for Optimization"
draft: false
---

### Author

Andre Augusto Cire

### School

Carnegie Mellon University

### Supervisors

John Hooker

Willem-Jan van Hoeve

### Abstract

Decision diagrams are compact graphical representations of Boolean functions originally introduced for applications in circuit design, simulation, and formal verification. Recently, they have been considered for a variety of purposes in optimization and operations research. These include facet enumeration in integer programming, maximum flow computation in large-scale networks, solution counting in combinatorics, and learning in genetic programming techniques.

In this dissertation we develop new methodologies based on decision diagrams to tackle discrete optimization problems. A decision diagram is viewed here as a graphical representation of the feasible solution set of a discrete problem. Since such diagrams may grow exponentially large in general, we work with the concept of approximate decision diagrams, first introduced by Andersen et al (2007). An approximate decision diagram is a graph of limited size that represents instead an over-approximation or under-approximation of the feasible solution set. Thus, it can be used to obtain either bounds on the optimal solution value or primal solutions to the problem. As our first contribution, we provide a modeling framework based on dynamic programming that can be used to specify how to build a decision diagram of a discrete optimization problem and how to approximate it, which facilitates the encoding process of a problem to a diagram representation. We then present a branching scheme that exploits the recursive structure of an approximate diagram, establishing a novel generic solver for discrete optimization problems. Computational results in classical optimization problems show that more instances can be solved in less computation time using our approach than mathematical programming techniques. In particular, we were able to reduce the known optimality gap of benchmark instances of the maximum cut problem.

In our second contribution, we focus on the application of approximate diagram to sequencing and scheduling problems. We show that, besides the computation of bounds, approximate decision diagram can be used to deduce non-trivial constraints of a problem, such as precedence relations between jobs in scheduling applications. We also demonstrate that such inference can be incorporated into state-of-the-art solvers and speed-up the optimization process by orders of magnitude.

Finally, we propose new parallelization strategies that exploits the recursive structure of an approximate diagram. These strategies decouple a problem in a naturally loose fashion and allow for more effective load balancing heuristics when considering hundreds of computer cores.

### Graduated

Friday, August 8, 2014 - 12:00