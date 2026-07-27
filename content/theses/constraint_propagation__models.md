---
aliases:
  - /old_nodes/968
title: "Constraint Propagation – Models, Techniques, Implementation"
date: 2026-07-25T15:04:46+0200
draft: false
---

### Author

Guido Tack

### School

Saarland University, Germany

### Supervisors

Gert Smolka

Christian Schulte

### Abstract

This dissertation presents the design of a propagation-based constraint solver. The design is based on models that span several levels of abstraction, ranging from a mathematical foundation, to a high-level implementation architecture, to concrete data structures and algorithms. This principled design approach results in a well-understood, correct, modular, and efficient implementation.

The core of the developed architecture is the propagation kernel. It provides the propagation infrastructure and is thus crucial for correctness and efficiency of the solver. Based on a mathematical model as well as a careful design of the employed algorithms and data structures, the presented architecture results in an efficient and domain-independent kernel. Constraints are realized by propagators, and implementing a propagator is a challenging, error-prone, and time-consuming task. A practically useful solver must however provide a comprehensive propagator library. This dissertation introduces two techniques for automatically deriving correct and efficient propagators. Views generalize variables and are used to derive propagators from existing propagators. For constraints over set variables, propagators are derived from formal constraint specifications.

The presented techniques are the basis of Gecode, a production-quality, highly efficient, and widely deployed constraint solver. Gecode is the empirical evidence for success and relevance of the principled design approach of this dissertation.

### Graduated

Thursday, January 29, 2009 - 12:00

### Also published in

[Generating Propagators for Finite Set Constraints](http://dx.doi.org/10.1007/11889205_41)

[View-based Propagator Derivation](http://dx.doi.org/10.1007/s10601-012-9133-z)