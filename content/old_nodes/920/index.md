---
title: "Paper with Impact (G. Pesant)"
draft: false
---

I've been offered the difficult job of writing the sequel to Patrick
Prosser's very entertaining yet insightful column on an old influential
paper. I don't think I can be as entertaining but hopefully I'll present a
complementary view of the same era, now far, far away…

My story takes place around the same time as Pat's, late 1990, as I was
about to embark on a Ph.D. after a few months spent in industry which
urged me back to graduate studies. It was a good company but my timing was
bad: all development had been temporarily halted because much
documentation on a government software contract was overdue, and guess who
had to help out even though not a single line of code was his… So back to
graduate school I went with a Master's degree in computational geometry in
my pocket and a recent interest in logic programming. As Pat pointed out,
these were pretty early days for CP and one often wandered alone on the
path to discovery. There weren't very many supervisors who were well
versed in the area. Mine was an expert in logic programming and he had
recently heard about CP (actually CLP, but more on this later). And the
very first paper he gave me to read (yes, made of real paper, not the
electronic kind) is the one I'll share with you.

It was definitely an influential paper personally because it got me
started in the research area that I've been exploring for almost 25 years.
But I suspect that it also had a wider impact since it was brought to a
large audience. This wasn't the most technical paper published in a very
specialized journal, though it did not shy away from theoretical
foundations, but a paper telling the readership of Communications of the
ACM about an exciting new field. Jacques Cohen, an early CP enthusiast,
published in the July 1990 issue a paper simply entitled "Constraint Logic
Programming Languages". It begins with a full-page illustration of famous
magician Harry Houdini bound and gagged in a box with swords being thrust
in every which way. What a great image! You will have guessed that the
swords are the constraints, and we are left worrying about poor Houdini
desperately looking for a solution. But he can work his magic from inside
the box, and if ever the swords prove too much for him, the reader is told
"Don't fret over the fate of our besieged character. In the world of
non-determinism and constraints, he will regain life once the killer sword
is withdrawn. Nonetheless, his destiny may remain uncertain until the
supply of swords is exhausted." I think today we can still relate to that
description of our field. (By the way I could very well have chosen
another paper in the same issue, written by Alain Colmerauer and
introducing Prolog III, the grandfather of constraint programming
languages.)

I think Pat would agree that he himself came from the planet CSP --- and I
was born on the not so distant planet CLP. Only later would the
respective middle letters be dropped to merge into what is now known as
CP. Back on CLP, constraint satisfaction arose naturally as an extension
of unification, at the heart of logic programming. It fixed the
non-declarativeness of arithmetic in Prolog and opened the door to
reasoning about new domains. The introduction of the CLP(X) schema, with
its most famous representative CLP(R), made that explicit. Finite
combinatorics were not as prominent as they are today in CP --- Cohen's
paper spoke of infinite trees, lists, and real closed fields. Of Borning's
groundbreaking work on constraints for GUIs. Of constraints appearing both
as input and output of a program. He talked of satisfaction completeness
for a constraint domain: the requirement that there exist an efficient
algorithm to decide whether a set of constraints admits a solution, and
implicitly that we apply it every time a constraint is added to that set.
Today we almost exclusively work with finite domain constraints and their
incomplete algorithms (the postponement of non-linear constraints in
CLP(R) is an early example of living with an incomplete solver). The
importance of simplification, canonical representation, and especially
incrementality had already been recognized for constraint solvers. All the
efforts into the design and implementation of constraint programming
languages that followed have been extremely important to bring that
technology outside of our community and make an impact on society.

Looking back, I think merging the two worlds of CSP and CLP made us
stronger as a community but, as can be expected, we also lost some of the
diversity, and people, in the field.

Jacques Cohen went on to serve as Editor-in-Chief of CACM (1992-1996). He
also served on my Ph.D jury.

[Gilles Pesant](http://www.professeurs.polymtl.ca/gilles.pesant/)  
May 2014

```
@article{Cohen90ConstraintLogicProgramming,
  author    = {Jacques Cohen},
  title     = {Constraint Logic Programming Languages},
  journal   = {Commun. ACM},
  volume    = {33},
  number    = {7},
  year      = {1990},
  pages     = {52-68}
}
```

[Link to electronic edition](http://dl.acm.org/citation.cfm?doid=79204.79209)

Content