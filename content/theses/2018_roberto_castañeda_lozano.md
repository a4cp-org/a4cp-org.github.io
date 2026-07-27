---
title: "Constraint-Based Register Allocation and Instruction Scheduling"
draft: false
aliases:
  - /old_nodes/1265
  - /theses/constraint-based_register_allo
---

**Author:** Roberto Castañeda Lozano  
**School:** KTH Royal Institute of Technology, Sweden  
**Supervisors:** Christian Schulte, Mats Carlsson, Ingo Sander  
**Graduated:** September 03, 2018  
**Link to full text:** [Open Access in DiVA database](http://urn.kb.se/resolve?urn=urn%3Anbn%3Ase%3Akth%3Adiva-232192)  

### Abstract

Register allocation (mapping variables to processor registers or memory) and instruction scheduling (reordering instructions to improve latency or throughput) are central compiler problems. This dissertation proposes a combinatorial optimization approach to these problems that delivers optimal solutions according to a model, captures trade-offs between conflicting decisions, accommodates processor-specific features, and handles different optimization criteria.

The use of constraint programming and a novel program representation enables a compact model of register allocation and instruction scheduling. The model captures the complete set of global register allocation subproblems (spilling, assignment, live range splitting, coalescing, load-store optimization, multi-allocation, register packing, and rematerialization) as well as additional subproblems that handle processor-specific features beyond the usual scope of conventional compilers.

The approach is implemented in Unison, an open-source tool used in industry and research that complements the state-of-the-art LLVM compiler. Unison applies general and problem-specific constraint solving methods to scale to medium-sized functions, solving functions of up to 647 instructions optimally and improving functions of up to 874 instructions. The approach is evaluated experimentally using different processors (Hexagon, ARM and MIPS), benchmark suites (MediaBench and SPEC CPU2006), and optimization criteria (speed and code size reduction). The results show that Unison generates code of slightly to significantly better quality than LLVM, depending on the characteristics of the targeted processor (1% to 9.3% mean estimated speedup; 0.8% to 3.9% mean code size reduction). Additional experiments for Hexagon show that its estimated speedup has a strong monotonic relationship to the actual execution speedup, resulting in a mean speedup of 5.4% across MediaBench applications.

The approach contributed by this dissertation is the first of its kind that is practical (it captures the complete set of subproblems, scales to medium-sized functions, and generates executable code) and effective (it generates better code than the LLVM compiler, fulfilling the promise of combinatorial optimization). It can be applied to trade compilation time for code quality beyond the usual optimization levels, explore and exploit processor-specific features, and identify improvement opportunities in conventional compilers.
