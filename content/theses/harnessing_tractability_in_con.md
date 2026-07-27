---
aliases:
  - /old_nodes/1278
title: "Harnessing Tractability in Constraint Satisfaction Problems"
date: 2026-07-25T15:04:37+0200
draft: false
---

### Author

Clément Carbonnel

### School

INP Toulouse

### Supervisors

Emmanuel Hebrard

Martin C. Cooper

### Abstract

The generality of CSP and its connections to logic, universal algebra and graph theory have drawn considerable attention from the complexity theory community. In particular, a rich theory has been developed to study how restricting the catalog of available relations affects the complexity of CSP. This line of research has produced a series of increasingly sophisticated polynomial-time algorithms that solve CSPs over a variety of constraint languages; unfortunately, this wealth of results on tractable subproblems of CSP has seen little to no practical use so far. This dissertation discusses the technical obstacles that prevent these theoretical results from being relevant to practical solving, and hints at possible approaches to overcome them.

First, most real-world CSP instances do not belong to a well-studied tractable class of CSP. However, some instances may be “nearly tractable” in an algorithmically exploitable sense. For instance, exhaustively branching on a few variables may produce residual instances that always belong to a known tractable class T. A set of variables with this property is called a "strong backdoor to T". In this thesis, we engage in a systematic investigation of the computational complexity of computing strong backdoors. We show that for any reasonable choice of class T this problem is NP-hard, but a more refined analysis using parameterized complexity allows us to identify certain classes for which this problem is nearly tractable (FPT for a relatively small parameter). Our results allow us to completely classify the parameterized complexity of strong backdoor detection for every tractable class studied in the literature.

Second, many tractable classes are defined by elusive algebraic properties and more often than not the complexity of testing for them is unknown - in some cases, even decidability is an issue. To address this issue, we present a universal algorithm that determines the complexity of any conservative constraint language in polynomial time. If the language turns out to be tractable, our algorithm also outputs valuable information on its algebraic structure. We complement this result with specialized, highly efficient polynomial-time algorithms for two well-known tractable classes.

Third and last, the definition of CSP used in most theoretical works ignores one of the most widely used feature of constraint solvers, global constraints. We focus on global constraints which are NP-hard to propagate and develop a full theory of "constraint kernelization", which provide novel algorithmic tools for propagator design. The notion of constraint kernelization is highly flexible; it can be used to create both complete and incomplete propagators with strong theoretical guarantees. We showcase our ideas by reporting promising experiments on an NP-hard global constraint implemented in Mistral.

### Graduated

Wednesday, December 7, 2016 - 12:00