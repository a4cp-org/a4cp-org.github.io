---
aliases:
  - /old_nodes/985
title: "Representations in Constraint Programming"
date: 2026-07-25T15:04:45+0200
draft: false
---

### Author

Christopher Jefferson

### School

University of York

### Abstract

One important choice in modelling is what variables will be used to represent the states of the problem. This choice is often optimised to try to take advantage of the global constraints in the solver being used. This concentration on global constraints has allowed the performance of models to improve as more and better global constraints are designed and implemented. However, this obsession with global constraints has lead to a lack of study of the variables, independent of the particular set of constraints implemented by a given solver.

The results of this thesis provide a strong basis on which to build systems which can automatically choose the appropriate variables to represent the high- level variables in a given problem.

This thesis presents a framework to compare the different sets of variables which represent a given problem, independent of how the constraints are imple- mented. This provides a number of powerful and useful results and allows a number of useful results to be proved. These include how a common set represen- tation performs as well as the theoretically best possible representation on a large set of common set and multisets constraints. Further, many families of constraints on sets and multisets which include the cardinality constraint are shown to have no tractable implementation. This provides a limit on how well representations can perform.
This framework for describing representations is also used to show how a close examination of the variables can allow more efficient implementations and better understanding of common concepts in constraint programming, including connecting multiple models of the same problem and breaking symmetry.

### Graduated

Saturday, June 30, 2007 - 12:00