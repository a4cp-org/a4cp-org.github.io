---
aliases:
  - /old_nodes/894
title: "Paper(s) with impact (P. Prosser)"
draft: false
---

I've been asked to write an article "Old CP article with impact" so I am going to write from a personal
viewpoint, i.e. an old CP article that had an impact on me.

A long time ago (1989) in a University far, far away (Strathclyde) ... before the internet, before Google, when
researchers would visit the Library once a month, to explore strange new conference proceedings,
seek out new journal articles, to boldly go to the librarians' desk and ask that these findings be photocopied and
that they would please phone the said researcher when the copies have been done and the researcher will then walk
back to the library, wait in line, pay and pick up the copies. You know, having done all that, you sure as hell read
the paper!

1989 was pretty early days for CP. Most often I had to discover for myself what was important. Some papers were
obviously important. Papers by E.C. Freuder were obviously important, as was Mackworth's paper on arc consistency,
Haralick and Elliot's paper on forward checking, and anything and everything by Rina Dechter. But there were
some papers that really stuck out. One was by John Gaschnig, an IJCAI 1977 paper on backjumping ... one page!
One page to describe bkmark, perform an empirical study and review relevant literature! I've looked at my
notes (about 25 years old now) and I wrote more than John did! It took me ages to understand the algorithm.
Maybe if he had written one more page?

1989 I went to IJCAI in Detroit. On a table, out side of a work shop, was a pile of technical reports "CSC-88-005:
CONSTRAINT SATISFACTION ALGORITHMS" by Bernard A. Nadel. There was a note and an honesty jar: take a copy and
give me a dollar. I didn't have a dollar, but I took one. The report is bound, with a cutout in
the glossy cover so you can read the title. It's not A4. It's almost square. And yes, this is the man previously
know as Nudel! The report's 52 pages long. It starts with a beautifully simple explanation of chronological
backtracking (BT), it gives the algorithm, a one page trace over n-queens, with the search tree drawn.
It then builds on this to get BJ (Gaschnig's backjumping), and again shows the search tree in comparison
to BT. It then moves onto BM (boy, was I pleased to read that and make sure I really did understand
Gaschnig's one pager!). Then on to arc consistency with the most beautiful page of drawings to show it
working. Partial arc consistency, full arc consistency, AC1, AC3, hybrid tree search (I didn't make it up),
nine full arc consistency hybrids, more beautiful drawings that look like sheet music with embedded
chess boards, up and down arrows, shading, more trees and traces, beautiful beautiful pages.
And tables of results, results that I could reproduce! And at the end of the paper 12 bullet points
"of possible directions for future research."

The paper not only sketched out a research agenda for me, it made me feel confident in what I was doing,
that I was not alone. It set a standard of presentation, one that I have not yet equalled. The paper was
published in Computational Intelligence Volume 5, Issue 3, and you can down load it, but it isn't the same
work of art as the tech report, the "unplugged" version, where Bernard wrote as much as he wanted in the way
that he pleased.

When I was writing up my PhD thesis I spent some time thinking about why I thought some papers were better
than others. So I went back and re-read those papers, in particular papers by Gene Freuder. And then it gradually
hit me that scientific writing can be good literature! I liked Gene's papers because I actually enjoyed
reading them! And I liked Bernard's paper because it looks like art. How crazy is that?

I know what you want to know. Did Bernard get his dollar? When I got back to
Glasgow I sent $1 to Bernard A. Nadel at Wayne State University, with a short note. Later, I tried to make contact
via the Comp.AI newsgroup. I got a letter through the post weeks later, a printoff of my posting with
hand written across it Bernard's email address (I still have the letter). Yes, he sent me a letter with his email
address. We then corresponded off and on. He gave me encouragement and direction when I needed it most and I am
forever indebted to him.

[Patrick Prosser](http://www.dcs.gla.ac.uk/~pat/)  
November 2013

```
@article{Nadel89ConstraintSatisfaction,
  author    = {Bernard A. Nadel},
  title     = {Constraint satisfaction algorithms},
  journal   = {Computational Intelligence},
  volume    = {5},
  year      = {1989},
  pages     = {188-224}
}

@inproceedings{Gaschnig77AGeneralBacktrack,
  author    = {John Gaschnig},
  title     = {A General Backtrack Algorithm That Eliminates Most Redundant
               Tests},
  editor    = {R. Reddy},
  booktitle = {Proceedings of the 5th International Joint Conference on
               Artificial Intelligence. Cambridge, MA, August 1977},
  publisher = {William Kaufmann},
  year      = {1977},
  pages     = {457}
}
```

Content