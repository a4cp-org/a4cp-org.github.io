---
title: "Paper with Impact (M. Wallace)"
draft: false
---

In the 1970’s Artificial Intelligence was the new frontier. The research community divided into two camps: the “clean” ones, like me, who were wedded to logic, and the others for whom knowledge and inference was opaquely embedded in complex neural structures. For clean AI, the USA community used a language called Lisp, while the Europeans used Prolog: “Programmation en Logique”. Computer scientists were allowed to talk French in those days ;-)

Prolog was elegant – it still is – but unfortunately every program you wrote required an execution time that was often exponential in the number of clauses in the program. Despite its apparent simplicity, doing anything useful in Prolog required sophisticated programming.

An exciting extension to Prolog was introduced to handle logical negation. This was a “coroutining” mechanism that changed the execution in a way that enabled us to write more efficient programs. We could now write simple planners that outperformed the state-of-the-art!

In 1984 three European companies set up a research centre in Germany (ECRC) to compete with rival logic-based research centres in the USA and Japan. ECRC was a Prolog shop – from hardware and operating systems, to knowledge bases (nowadays called “big data”). The head of ECRC had a special interest in one particular group – the CHIP group, which included Pascal Van Hentenryck, Helmut Simonis and Nicolas Beldiceanu.

In 1986 I met an Australian girl and I was thrilled to go with her to Melbourne in 1987 for my first international logic programming conference. It changed my life! It was at this conference that Pascal presented a paper called “Forward Checking in Logic Programming”. I was still excited by coroutining, and my breath was taken away when he said that with forward checking combined with coroutining they got an order of magnitude speedup. Adding another amazing idea called “first-fail” they got two orders of magnitude!

One cute thing was that they could choose which predicates to turn into constraints. Indeed the history of constraint programming is a history of progress in controlling the combination of propagation, learning, and search heuristics, tuned to the problem at hand.

I confess, I believed these results would enable logic programming to become the de facto standard programming paradigm. It hasn’t, yet (though the end of Moore’s law has marked the beginning of a new era of parallelism which perfectly fits declarative programs). Nor did I choose the right camp in clean Artificial Intelligence ☹

However the combination of constraint propagation and declarative programming has gone on to rock the operations research community. It has inspired not only decades of innovative research, but also commercial and industry practice. As a researcher and through my involvement in Parc Technologies and now Opturion, it goes right on changing my life.

And the trip to Melbourne: I married my girlfriend and we’ve been living here for the last 10 years!

Mark Wallace  
June 2015

```
@inproceedings{VanHentenryck1987ForwardChecking,
  author    = {Pascal Van Hentenryck and
               Mehmet Dincbas},
  title     = {Forward Checking in Logic Programming},
  booktitle = {Logic Programming, Proceedings of the Fourth International Conference,
               Melbourne, Victoria, Australia, May 25-29, 1987 {(2} Volumes)},
  editor    = {Jean{-}Louis Lassez},
  isbn      = {0-262-12125-5},
  pages     = {229--256},
  publisher = {{MIT} Press},
  year      = {1987},
}
```

Content

Section

[current](/taxonomy/term/7)