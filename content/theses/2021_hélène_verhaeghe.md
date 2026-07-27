---
title: "The extensional constraint"
draft: false
aliases:
  - /old_nodes/1372
  - /theses/the_extensional_constraint
---

**Author:** Hélène Verhaeghe  
**School:** UCLouvain, Louvain-la-Neuve, Belgium  
**Supervisors:** Prof. Pierre Schaus, Prof. Christophe Lecoutre  
**Graduated:** August 31, 2021  

### Abstract

Extensional constraints are crucial in Constraint Programming. They represent allowed combinations of values for a subset of variables (the scope of the constraint) using extensional representation forms such as tables (lists of tuples of constraint solutions) or MDDs (layered acyclic directed graphs where each path represents a constraint solution). Such extensional forms allow the modelization of virtually any kind of constraints.
This type of constraint is among the first ones available in constraint solvers. A lot of progress has been made since the original design of the first propagator of table constraints: advanced use of supports, simple tabular reduction, bitwise computations, reseting opperations, table compression, and MDDs. The most recent algorithm prior to this thesis is Compact-Table. It advantageously uses a data structure called reversible sparse bitsets to speed up the computations.
The work in this thesis initiates with Compact-Table. The goal is to extend it to handle other kinds of extensional representation. The first addressed representation is about compressed tables, i.e. tables containing tuples wich do not only contain single values but also simple unary (∗, != v, ≤ v, ≥ v, ∈ S, !∈ S) or binary (= x + v, != x + v, ≤ x + v, ≥ x + v) restrictions. One such compressed tuple allows representing several classical ones. This led to the CT ∗ and CT bs algorithms, handling respectively short and basic smart tables. The second addressed issue concerns negative tables, i.e. tables listing forbidden combinations of values. This results in the CT neg and CT ∗ neg algorithms, handling respectively negative and negative short tables. The third and last adaptation addresses diagram structures, i.e. graphs such as MDDs or other layered graphical structure. This led to the CD and CD bs algorithms, handling respectively diagrams and basic smart diagrams.
Being able to use such diversity of representation helps to counter-balance the main drawback of classical table representations, which is their potentially exponential growth in size. Compressed tables, negative tables, and diagrams help reduce the memory consumption (storage size) required to store an equivalent representation.
