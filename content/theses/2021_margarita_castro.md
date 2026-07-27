---
title: "Optimization Methods Based on Decision Diagrams for Constraint Programming, AI Planning, and Mathematical Programming"
draft: false
aliases:
  - /old_nodes/1392
  - /theses/optimization_methods_based_on_
---

**Author:** Margarita Castro  
**School:** University of Toronto  
**Supervisors:** J. Christopher Beck, Andre A. Cire  
**Graduated:** March 01, 2021  
**Link to full text:** [Optimization Methods Based on Decision Diagrams for Constraint Programming, AI …](https://www.proquest.com/docview/2507182586?pq-origsite=gscholar&fromopenview=true)  

### Abstract

Decision diagrams (DDs) are graphical structures that can be used to solve discrete optimization problems by representing the set of feasible solutions as paths in a graph. This graphical encoding of the feasibility set can represent complex combinatorial structures and is the foundation of several novel optimization techniques. Due to their flexibility, DDs have become an attractive optimization tool for researchers in different fields, including operations research and computer science.

This dissertation investigates new techniques to use DDs in conjunction with existing discrete optimization approaches based on constraint programming (CP), artificial intelligence (AI), and integer programming (IP). The central thesis of this dissertation is that DDs are effective tools to capture complex combinatorial structures of discrete optimization problems that are not fully exploited by general-purpose solvers. Thus, combinations of DDs with existing technologies can achieve state-of-the-art performance on challenging optimization problems.

Throughout this work, we address this thesis by developing novel DD procedures that leverage methodologies from different optimization fields to solve discrete optimization problems. Our first project employs Lagrangian duality to strengthen DD bounds for pickup-and-delivery problems. The second project explores new ways to generate admissible heuristics for AI planning tasks by combining DD relaxations with AI planning techniques. This work also studies the relationship between DD heuristics and existing admissible heuristics in the community. Lastly, we propose a novel combinatorial lifting procedure and two cutting plane approaches based on DDs for general-form binary optimization problems. We show theoretical guarantees for our lifting procedure (e.g., conditions to obtain facet defining inequalities) and provide a thorough theoretical analysis of our two cutting plane procedures.

We apply our DD techniques to different problems, extending the usability of DDs in the field. Our first work extends the literature of DDs for sequencing problems by considering capacity constraints and proposing a DD construction procedure based on this restriction. We also present two DD encodings for delete-free AI planning and analyze the properties of both representations. Our last project introduces a new DD network flow formulation and proposes a novel DD encoding for second-order cone inequalities.
