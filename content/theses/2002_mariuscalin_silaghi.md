---
title: "Asynchronously solving problems with privacy requirements"
draft: false
aliases:
  - /old_nodes/1299
  - /theses/asynchronously_solving_problem
---

**Author:** Marius-Calin Silaghi  
**School:** Swiss Federal Institute of Technology (EPFL)  
**Supervisors:** Boi Faltings  
**Graduated:** January 06, 2002  
**Link to full text:** [Asynchronously solving problems with privacy requirements](https://cs.fit.edu/~msilaghi/teza/)  

### Abstract

Asynchronous search techniques for distributed satisfaction problems are among the scientific challenges of Distributed Artificial Intelligence. They are useful in applications like negotiations (Generalized English Auctions), distributed meeting scheduling with private constraints, distributed
configuration with secret know-how.
Asynchronous search also has an important theoretic value, defining generic techniques whose
properties, once proven, apply to a large number of not only distributed but also centralized old
and new algorithms. A convincing example is the technique I propose for using backtracking
nogoods in consistency (Section 7.3.1), technique that can be straightforwardly applied to classic
centralized versions of backtracking (as I show in Section 5.2) with improvements of efficiency.
Despite the continuous effort of the last ten years, several important issues remained open
until now. This thesis describes several advances that allow the agents to get more opportunities
to communicate. It also proposes new frameworks for distributed constraint satisfaction, and
strategies for agents. The main focus is on asynchronous complete search with polynomial space
requirements in the size of the global problem, where the global problem is distributed naturally.
Among the main contributions I mention:

* Local consistency is a technique bringing gains that are exponential in the size of the problem, by deposing an effort that is exponential in the size of the used predicates (constraints).
  The effort can therefore be polynomial in the size of the global problem. Exponential gain
  with polynomial cost made local consistency the most important technique in constraint
  satisfaction where it was shown that any opportunity must be used for exploiting it (consistency maintenance). I generalize the concept of centralized consistency maintenance in a
  way that makes it applicable to asynchronous techniques. This is the first technique allowing
  for consistency maintenance in asynchronous search and is very efficient (Chapter 7).
* I noticed that the use of CSPs techniques for numeric problems over IR was possible by
  something that can be described as: letting the domain splits have existential meaning rather
  than the universal meaning in classical backtracking. Existing asynchronous search protocols
  supported only proposals with universal quantifiers (e.g. require(∀x ∈ {1})). I modify
  and generalize existing asynchronous search protocols to support proposals with existential
  quantifiers (e.g. require(∃x ∈ {[1.5, 105
  ] ∪ {0, 1}})). This efficient technique is the first
  to allow a proper use of intervals in proposals and is a first step I took for extending
  the applicability of asynchronous search to Numeric CSPs. Since this idea came when I
  tried to integrate in ABT an aggregation technique described in (Silaghi et al. 2000c),
  the first protocol with the desired property is called Asynchronous Aggregation Search (see
  Chapter 9).
* Existing algorithms enforced a static priority on agents. This is a drawback. It entangles
  agents to verify conflicts in Generalized English Auctions (Chapter 17), for defending themselves from unfair competition. One only knew to remove that constraint at the expense of
  requiring an unbounded computer memory (e.g. RAM). This is infeasible and leads to unwarranted protocols. I designed the first solving protocol that allows the needed dynamic
  reordering and still has a guaranteed termination with polynomially bounded computer
  space requirements. Moreover, the designed technique is very general as it can introduce all
  important reordering heuristics used for efficiency in centralized techniques (see Chapter 10).
* Besides the aforementioned reordering technique, I propose a suite of other techniques for dynamic reordering with other types of heuristics and still offering guaranteed termination with
  polynomial space requirements: Reordering with increasing delay restarts (Section 10.3.1),
  and Finite number of reorderings. These two techniques are simple but allow only simplistic
  reordering heuristics. Dynamic Partial Order is discussed in Section 10.4.
* Proposals with existential quantifiers are not sufficient for enabling application of search
  to numeric problems. The remaining requirement is that proposals must not be binding.
  Actually, one of the powerful and general available centralized techniques for solving numeric
  problems is the one proposed in Section 5.2.3.2. Domains are split recursively, and the
  same constraints are recursively reverified until complete satisfaction or an acceptable
  resolution is obtained.
* Asynchronous techniques requested an agent only once its proposal. The proposals were
  therefore necessarily binding. This is incompatible with the practice required for numeric
  problems, as mentioned at the previous item. After understanding this problem, I proposed a modeling technique called Replica-based search. Several replicas of the same agent
  are asked proposals at different levels of abstractions. As a result, proposals of the
  replicas are not binding. They can be refused by subsequent replicas (e.g. After an
  agent sends require(∃x ∈ {[1.5, 105
  ] ∪ {0, 1}}), it can be more restrictive in a subsequent
  replica, require(∃x ∈ {[15, 1000]}), and later can even abandon completely its proposal,
  require(x 6∈ {[1.5, 105
  ] ∪ {0, 1}})). This technique, described in Chapter 13 closes the sequence of ideas required for developing asynchronous techniques for numeric problems over
  IR.
* One of the main motivations for distributed algorithms is the enforcement of privacy. A
  framework for modeling and quantifying privacy loss and a theoretic comparison on the
  power of different protocols in saving privacy are proposed in Chapter 16.
* Hewlett-Packard, learning that the ink-jet printer is a competitor for their main product, the
  laser printer, decided to also develop ink-jet printers in parallel. With the same principle in
  mind, I developed and analyzed an expensive secure protocol (SCSPS), proposed in Chapter 15. I also developed and analyzed a set of cryptographic protocols for both discrete and
  numeric distributed satisfaction problems (Annex B). For the work described in Annex B,
  another important contribution is the discovery of the feebleness of that type of techniques,
  the “S-attacks”. The obtained cryptographic protocols have some drawbacks such that a
  trade-off remains between the competing techniques. Secure protocols and distributed algorithms will continue to coexist for a while, as laser printers and ink-jet printers.
* Several distributed optimization techniques have been developed so far. Those techniques
  are not general and abstract enough for allowing extensions like consistency maintenance and
  reordering. The notion of cost was unclear. I introduce the notion of cost in nogoods,
  obtaining a general stand-alone communication atom. In Chapter 14 I describe a
  generalization of all the existing distributed satisfaction and optimization techniques. This
  generalization allows the introduction of consistency maintenance, reordering, etc. in distributed optimization.
* Negotiations are defined by the fact that the participants yield from their constraints to
  reach common solutions. This is technically called: constraint relaxation. No relaxation
  technique existed for private problems. I propose such a technique for private constraints
  (Section 17.10). A classical dualism for CSPs defines a standard transfer between privacy on
  constraints and privacy on domains (see Section 3.5.2 and Chapter 18). We have also defined
  a primal version of this technique.
