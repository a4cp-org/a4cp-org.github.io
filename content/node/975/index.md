---
title: "Set Constraints for Local Search"
date: 2026-07-25T15:04:45+0200
draft: false
---

### Author

Magnus Ågren (now Magnus Rattfeldt)

### School

Uppsala University

### Supervisors

Pierre Flener

Justin Pearson

### Abstract

Combinatorial problems are ubiquitous in our society and solving such problems efficiently is often crucial. One technique for solving combinatorial problems is constraint-based local search. Its compositional nature together with its efficiency on large problem instances have made this technique particularly attractive. In this thesis we contribute to simplifying the solving of combinatorial problems using constraint-based local search.

To provide higher-level modelling options, we introduce set variables and set constraints in local search by extending relevant local search concepts. We also propose a general scheme to follow in order to define what we call natural and balanced constraint measures, and accordingly define such measures for over a dozen set constraints. However, defining such measures for a new constraint is time-consuming and error-prone. To relieve the user from this, we provide generic measures for any set constraint modelled in monadic existential second-order logic. We also theoretically relate these measures to our proposed general scheme, and discuss implementation issues such as incremental algorithms and their worst-case complexities.

To enable higher-level search algorithms, we introduce constraint-directed neighbourhoods in local search by proposing new constraint primitives for representing such neighbourhoods. Based on a constraint, possibly modelled in monadic existential second-order logic, these primitives return neighbourhoods with moves that are known in advance to achieve a decrease (or preservation, or increase) of the constraint measures, without the need to iterate over any other moves.

We also present a framework for constraint-based local search where one can model and solve combinatorial problems with set variables and set constraints, use any set constraint modelled in monadic existential second-order logic, as well as use constraint-directed neighbourhoods. Experimental results on three real-life problems show the usefulness in practice of our theoretical results: our running times are comparable to the current state-of-the-art approaches to solving the considered problems.

### Graduated

Friday, January 18, 2008 - 12:00

### Link to full text

[Set Constraints for Local Search](http://urn.kb.se/resolve?urn=urn%3Anbn%3Ase%3Auu%3Adiva-8373)