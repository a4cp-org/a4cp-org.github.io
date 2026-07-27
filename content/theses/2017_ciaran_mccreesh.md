---
title: "Solving Hard Subgraph Problems in Parallel"
draft: false
aliases:
  - /old_nodes/1188
  - /theses/solving_hard_subgraph_problems
---

**Author:** Ciaran McCreesh  
**School:** School of Computing Science  
**Supervisors:** Patrick Prosser  
**Graduated:** July 25, 2017  
**Link to full text:** [Solving hard subgraph problems in parallel](http://theses.gla.ac.uk/8322/)  

### Abstract

This thesis improves the state of the art in exact, practical algorithms for finding subgraphs. We study maximum clique, subgraph isomorphism, and maximum common subgraph problems. These are widely applicable: within computing science, subgraph problems arise in document clustering, computer vision, the design of communication protocols, model checking, compiler code generation, malware detection, cryptography, and robotics; beyond, applications occur in biochemistry, electrical engineering, mathematics, law enforcement, fraud detection, fault diagnosis, manufacturing, and sociology. We therefore consider both the ``pure'' forms of these problems, and variants with labels and other domain-specific constraints.

Although subgraph-finding should theoretically be hard, the constraint-based search algorithms we discuss can easily solve real-world instances involving graphs with thousands of vertices, and millions of edges. We therefore ask: is it possible to generate ``really hard'' instances for these problems, and if so, what can we learn? By extending research into combinatorial phase transition phenomena, we develop a better understanding of branching heuristics, as well as highlighting a serious flaw in the design of graph database systems.

This thesis also demonstrates how to exploit two of the kinds of parallelism offered by current computer hardware. Bit parallelism allows us to carry out operations on whole sets of vertices in a single instruction---this is largely routine. Thread parallelism, to make use of the multiple cores offered by all modern processors, is more complex. We suggest three desirable performance characteristics that we would like when introducing thread parallelism: lack of risk (parallel cannot be exponentially slower than sequential), scalability (adding more processing cores cannot make runtimes worse), and reproducibility (the same instance on the same hardware will take roughly the same time every time it is run). We then detail the difficulties in guaranteeing these characteristics when using modern algorithmic techniques.

Besides ensuring that parallelism cannot make things worse, we also increase the likelihood of it making things better. We compare randomised work stealing to new tailored strategies, and perform experiments to identify the factors contributing to good speedups. We show that whilst load balancing is difficult, the primary factor influencing the results is the interaction between branching heuristics and parallelism. By using parallelism to explicitly offset the commitment made to weak early branching choices, we obtain parallel subgraph solvers which are substantially and consistently better than the best sequential algorithms.
