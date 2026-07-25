---
title: "Outperforming state-of-the-art compilers in Unison"
date: 2026-07-25T15:04:30+0200
draft: false
---

[![Unison](/sites/default/files/unison-logo.png)](https://unison-code.github.io/)

Do you want to improve the quality of your code? Unison is a code generator for compilers with a radically new approach. Unison rethinks code generation using combinatorial optimization techniques. Unison is available on [Github](https://unison-code.github.io/) and is integrated with the regular LLVM toolchain.

A compiler is a program that transforms a source code from a high-level programming language into a lower level language (e.g., assembly language) to create an executable program. Compilers decompose code generation into multiple tasks (instruction selection, instruction scheduling, and register allocation) and solve each task in isolation with heuristics. Unison pursues a radically different route: it embraces and exploits the combinatorial, interdependent nature of code generation to drastically improve code quality. In Unison, the inter dependent code generation tasks are translated into a single combinatorial model that accurately reflects all inter dependencies. Solving the model with constraint programming, a modern combinatorial optimization technology, results in the desired high-quality assembly code.

Unison complements state-of-the-art compilers and is used by [Ericsson](https://www.ericsson.com/en/blog/2017/12/outperforming-state-of-the-art-compilers-in-unison).