---
title: "Efficient Algorithms for Strong Local Consistencies and Adaptive Techniques in Constraint Satisfaction Problems"
draft: false
---

### Author

Anastasia Paparrizou

### School

University of Western Macedonia, Greece

### Supervisors

Kostas Stergiou

### Abstract

Constraint Programming (CP) is a successful technology for solving a wide range of problems in business and industry which require the satisfaction of a set of complex constraints. Examples include product configuration, resource allocation, transportation, and scheduling. As the simultaneous satisfaction of different constraints is intractable in general, problems can become very difficult to solve as their size increases. CP has thus developed various techniques to tackle this inherent problem. Enforcing a local consistency property is one of the most important such techniques. Bounds Consistency and Arc Consistency are the two most widely studied and used local consistencies in CP solvers. While there exist stronger local consistency (SLC) properties, their usage is limited due to their prohibitive cost.

In our research, we propose efficient filtering algorithms for enforcing SLCs for binary and non-binary problems that advance the existing algorithms (theoretically and practically). In addition, we have extended the recent algorithms from the family of Simple Tabular Reduction (STR) to achieve a higher-order local consistency property. Experiments demonstrate that these algorithms can significantly outperform various state-of-the-art (G)AC algorithms, even by orders of magnitude, and thus can become very useful additions to the propagation techniques that CP solvers currently apply. Additionally, we have introduced and defined a new strong Bounds Consistency, as well as a polynomial filtering algorithm based on this consistency for the important class of linear inequalities. Theoretical and experimental results demonstrate the potential of SLCs that reason on bounds.

Finally, since SLCs may still be too expensive to maintain during search in many problems, we have suggested ways to interleave them with weaker propagation methods such as GAC. We have proposed fully automated heuristics that can dynamically select the most appropriate filtering algorithm. Overall, this research proposes filtering algorithms and adaptive techniques that exploit the filtering power offered by SLCs in an efficient way, in order to increase the efficacy of CP solvers.

### Graduated

Tuesday, December 10, 2013 - 12:00

### Also published in

[AI Access monographs](http://www.cse.unsw.edu.au/~tw/anastasia.pdf)

### Notes

Honourable mention for the 2013 Artificial Intelligence Dissertation Award sponsored by ECCAI.