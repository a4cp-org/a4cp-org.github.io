---
aliases:
  - /old_nodes/972
title: "Efficient Propagators for Global Constraints"
date: 2026-07-25T15:04:43+0200
draft: false
---

### Author

Claude-Guy Quimper

### School

University of Waterloo

### Supervisors

Alejandro López-Ortiz

### Abstract

We study in this thesis three well known global constraints. The All-Different constraint restricts a set of variables to be assigned to distinct values. The global cardinality constraint (GCC) ensures that a value v is assigned to at least l\_v variables and to at most u\_v variables among a set of given variables where l\_v and u\_v are non-negative integers such that l\_v <= u\_v. The Inter-Distance constraint ensures that all variables, among a set of variables x\_1,..., x\_n, are pairwise distant from p, i.e. |x\_i - x\_j| >= p for all i != j. The All-Different constraint, the GCC, and the Inter-Distance constraint are largely used in scheduling problems. For instance, in scheduling problems where tasks with unit processing time compete for a single resource, we have an All-Different constraint on the starting time variables. When there are k resources, we have a GCC with l\_v = 0 and u\_v = k over all starting time variables. Finally, if tasks have processing time t and compete for a single resource, we have an Inter-Distance constraint with p = t over all starting time variables. We present new propagators for the \alldiff\ constraint, the \gcc, and the  
\interdistance\ constraint i.e., new filtering algorithms that reduce the search space according to these constraints. For a given consistency, our propagators outperform previous propagators both in practice and in theory. The gains in performance are achieved through judicious use of advanced data structures combined with novel results on the structural properties of the constraints.

### Graduated

Saturday, October 21, 2006 - 12:00