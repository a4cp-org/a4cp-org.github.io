---
title: "Success Stories"
date: 2026-07-25T15:04:29+0200
draft: false
aliases:
  - /cp/success-stories
---

In this section, the ACP collects *success stories* of using constraint based technology. We aim to make these stories appeal to a wide audience, so they are written for a general audience.

This section was started in September 2015. We will update it regularly, so make sure to come back regularly!

If you want to share your story (or know someone who has a story to share), please contact us by email at stories@a4cp.org.

---

[A CP solver designs a self-assembling protein](/cp/success-stories/a_cp_solver_designs_a_self-ass)

![The Ika4 protein (PDB 6g6q)](/sites/default/files/final_0.png)

Designing a stable and self-assembling protein requires to organize thousands of atoms in a favorable configuration in space.

Researchers at INRA, Toulouse (France) worked in collaboration with biochemists in Belgium and Japan and used constraint programming technology, embodied in the [toulbar2](http://www.inra.fr/mia/T/toulbar2/) solver, to optimize the intermolecular forces (captured by the Talaris14 force-field) of the full-atom representation of the targeted protein shape. Toulbar2 was able to identify a most stable molecular organization and to prove that no better organization exists.

Proteins are the main molecules of life. They govern much of how cells work, in humans, animals, plants, fungi and microbes. They are able to bind to other molecules, and to self assemble to build complex nano-structures. They can catalyze chemical reactions at ambient temperature and pressure while being biodegradable. Newly designed proteins have therefore a large potential for applications in medicine, green chemistry, biofuels, oil-based products recycling, ... Having the ability to design new tailored proteins is thus of prime importance for health but also to reduce our environmental footprint.

**Contact**: Thomas Schiex (thomas.schiex@inra.fr)

Proteins are linear molecules formed by bonding successives amino-acids. There are 20 natural amino-acids and each of them is defined by a constant part (identical in all amino acids) and a variable part that sticks out of the side of the constant part. The variable part is called the side-chain. It defines the specific physico-chemical properties of the amino acid and it is usually very flexible (robotic arms algorithms have been used to describe and predict these moves). The constant part is the part which is used to build up the protein, by repeated creation of so-called peptidic bonds between amino acids, defining a long chain called the backbone of the protein. The fundamental paradigm in structural biochemistry is that the structure of the protein (how it organizes various atoms in space) defines its function. To design a protein for a specific function, one starts therefore from a targeted shape of one or several interacting backbones. The aim is then to populate all the side-chains with those that will stabilize the backbone when it is in water, hoping that when the protein is created and exists in a cell, it will fold along this backbone shape. To achieve this and account for side-chain movements, the collection of 20 available side-chains is multiplied by considering a collection of possible positions (or conformations) for each side chain. In the end, one typically needs to consider that several hundreds of side-chains are possible at each position. A protein of length n therefore typically requires to explore a space of size 400^n. To choose the suitable amino acids, interatomic forces are modeled in a so-called force field (or score function) that captures interactions between atoms. The most usual force fields such as CHARM or AMBER are pairwise decomposable meaning that they decompose into a sum of functions involving at most two atoms or two positions. Ultimately, the problem of designing a new protein therefore reduces to a huge optimization problem with as many variables as there are amino acids to design, with few hundreds discrete values for each variable and unary and binary functions between variables, whose sum must be minimized. This is precisely a Cost Function Network (CFN) and finding its minimum cost (or energy) assignment is a Weighted Constraint Satisfaction Problem. Since Computational Protein Design (CPD) is NP-hard, as the WCSP, traditional approaches use Monte Carlo (Simulated annealing) methods to identify low energy solutions. These methods are very general but offer no finite time guarantee and have difficulties taking into account hard constraints. Based on enhanced constraint satisfaction and automated reasoning algorithms, the CFN solver [toulbar2](http://www.inra.fr/mia/T/toulbar2/) can solve these problems very efficiently. On these problems, toulbar2 was shown to outperform alternative exact solvers based on integer linear programming, quadratic programming, Partial Weighted Maximum Satisfiability or existing CPD-dedicated solvers (1). It was later shown to be able to prove that a highly specialized implementation of Simulated annealing targeted at Computational Protein Design is often unable to identify an optimal solution, with a gap to optimality that increases very rapidly as the problem gets harder. In the end, using CFN technology, it becomes possible to reliably get an optimal solution faster than with Simulated annealing. The capacity of toulbar2 to easily accept constraints in its input makes it also easier to integrate specific requirements on the protein to design (on its composition, charge...)

[![Ika Protein](/sites/default/files/ika4a_0.png)](https://www.linkedin.com/pulse/ai-designs-self-assembling-protein-thomas-schiex)
To see if these good properties were useful in the real world, we collaborated with biochemists in Belgium and Japan to design a new symmetric protein for real, ideally one that could self assemble from pieces. The design was done using a traditional approach and a CFN based approach. Although both approaches produced a protein that correctly folded in the targeted shape, only the CFN-based design could self assemble from smaller components. It is also more stable, resisting temperatures close to 90C°, or a pH close to 1. This protein, which appears on the journal cover of (3), could traverse your stomach undigested (see https://www.linkedin.com/pulse/ai-designs-self-assembling-protein-thomas-schiex).

We are now working on new targets with collaborators in medicine and green chemistry. But tackling CPD problems also requires new automated reasoning algorithms to answer new questions: how can I find a sequence of amino acids that would accept to fold in two alternative shapes (so-called conformational switches) or that should also absolutely avoid some extra shapes. Some of these problems are extremely challenging reasoning problems, at the second level of the polynomial hierarchy. They also raise questions in Machine Learning, the more obvious one being to learn how to design (or help automated reasoning solvers to design) new proteins from existing natural proteins.

(1) Allouche, D., André, I., Barbe, S., Davies, J., De Givry, S., Katsirelos, G., O'Sullivan, B., Prestwich, S., Schiex, T. and Traoré, S., 2014. Computational protein design as an optimization problem. Artificial Intelligence, 212, pp.59-79.

(2) Simoncini, D., Allouche, D., de Givry, S., Delmas, C., Barbe, S. and Schiex, T., 2015. Guaranteed discrete energy optimization on large protein design problems. Journal of chemical theory and computation, 11(12), pp.5980-5989.

(3) Noguchi, H., Addy, C., Simoncini, D., Wouters, S., Mylemans, B., Van Meervelt, L., Schiex, T., Zhang, K.Y., Tame, J.R.H. and Voet, A.R.D., 2019. Computational design of symmetrical eight-bladed β-propeller proteins. IUCrJ, 6(1).

[view](/cp/success-stories/a_cp_solver_designs_a_self-ass)

[From dreams to reality](/theses/from_dreams_to_reality)

[![Gecode](/sites/default/files/gecode_0.png)](https://www.gecode.org/)

You need to buy a new car and want to try out configurations to know what can be done or is affordable? It is now possible if your car dealer uses the SAP S/4HANA tool.

SAP builds its variant configuration engine in their S/4HANA platform on top of the constraint solver [Gecode](https://www.gecode.org/). The configuration engine’s role is to keep track of a range of values, how these are combined, and to ensure that only meaningful configurations are offered to users. To do so, it uses Gecode to ensure that combinations are valid and that no restrictions are violated.

* [More info on KTH website](https://www.kth.se/en/forskning/artiklar/at-core-of-software-leader-sap-s-product-an-open-source-code-developed-at-kth-1.867376)
* [More info on SAP blog](https://blogs.sap.com/2018/09/07/sap-leverages-gecode-an-award-winning-constraint-solver-in-s4hana-for-advanced-variant-configuration/)

[view](/theses/from_dreams_to_reality)

[CP Has Landed on the Comet](/cp/success-stories/cp_has_landed_on_the_comet)

On June 13th 2015, the robot-lab Philae woke up on the comet 67P/Churyumov-Gerasimenko to resume a series of experiments interrupted seven months ago. These experiments were scheduled using Constraint Programming, and researchers of the team [ROC](#authors) developed
propagation algorithms
to help the *Scientific Operations and Navigation Centre* (SONC) to efficiently achieve this task.
The Rosetta/Philae mission was launched in 2004 and it took more than ten years for the spacecraft, Rosetta, to reach its destination after a 6 billion kilometres long trip. On November 12th 2014, the lander module, Philae, was released and landed on the ground of the comet. Philae is fitted with ten instruments (see [Figure 1](#fig1)) to conduct the experiments elaborated by as many research teams across Europe. These experiments, should they be imaging (CIVA, ROLIS), sampling (SD2, COSAC, PTOLEMY) or other types of signal analysis, correspond to sequences of activities constrained by two extremely scarce resources:

* First, instruments were supplied in energy by the main battery alone, which barely held enough power to keep a low-energy light-bulb lit up during the three days of this first sequence.
* Second, all the data collected by the instruments were stored on a central mass-memory whose capacity is 6MB, that is, about as much as 4 floppy disks.

|  |  |  |
| --- | --- | --- |
|  | Philae Instruments, image copyright ESA/AOES Medialab |  |
|  | Figure 1. Philae's instruments (© ESA/AOES Medialab) |  |

The plans executed by Philae are modelled and solved using constraint programming technology.
Indeed, *Mission Operations Scheduling Tool* (MOST), the
toolkit used to schedule the lander's activities, was developed by a [CNES](https://cnes.fr/en) team based in Toulouse on top of IBM ILOG Scheduler (now IBM CP Optimizer).
This framework is very well suited to model the constraints related to instant energy usage of the instruments, using well-known algorithms to reason about cumulative resources.
Moreover, in order to model the more specific constraints related to data transfers,
several dedicated algorithms were developed by the Operations Research & Constraints group of the [LAAS-CNRS](https://www.laas.fr/public/en/roc/) lab.
This work was published by the Constraints journal [[Simonin et al. 15]](#simoninbib).
Notice that the activities of Rosetta, on the other hand, were handled by a separate team and the NASA largely contributed to MOST's equivalent *Rosetta Science Ground Segment Scheduling Component* (RSSC), which uses the priority-based scheduling module ASPEN [[Chien et al. 13]](#chienbib).

#### The Rosetta/Philae Mission

|  |  |  |
| --- | --- | --- |
|  | Rosetta's navcam image of 67P, copyright ESA/AOES Medialab |  |
|  | 67P Churyumov/Gerasimenko by Rosetta's navcam, on December 10th 2014 (© ESA/AOES Medialab) |  |

Comets are of particular interest because as witnesses of the early age of the solar system, and because that may be the source of a large part of the water in our oceans*[1](#fn1)* and perhaps at the origin of life on Earth.
The European Space Agency therefore launched an extremely ambitious project: The spacecraft Rosetta was set to meet the comet Churyumov-Gerasimenko and orbit it while making a series of observations and measures. Moreover, a robot module attached to Rosetta, Philae, was set to land on the surface of the comet in order to study the composition and properties of its kernel.
Because of the extremely long distance from Earth to Rosetta when it reached the comet (about 650 million kilometres) sending instructions takes about half an hour making it impractical and wasteful to send short terms commands. Long term plans, lasting several days, are therefore computed on the ground and sent to Rosetta which transmits them to the lander. New plans can then be uploaded, however only during visibility windows distant of several hours.
On November 12th 2014, Philae executed the first of these plans, starting with its release from Rosetta and followed by its descent toward the surface of the comet. During this phase, called SDL for *Separation-Descent-Landing* a number of activities took place (e.g. imaging from the downward facing camera ROLIS, or the magnetometer ROMAP).
The "touchdown" event triggered the second and main phase of the plan, the *First-Science-Sequence* (FSS).
This phase corresponds to the main battery autonomy period and is the only chance for Philae to proceed to the most energy demanding experiments.
As we know now, the data from the first experiments (such as CIVA, the panoramic camera) indicated that something went wrong. For instance, the data from SESAME, the acoustic/mechanical probing instruments, later showed that Philae bounced several times before reaching its final location on the comet.
It was anticipated that new plans, tailored to the parameters of the exact landing site, such as the visibility of the orbiter (to plan data transfers) or sunshine duration (to plan for imaging activities) or even the landscape.
Because of the unexpected turn of events, it was even more critical to upload new plans to Philae. However, because most of the actual landing site parameters were unknown, ESA's operatives took a very conservative approach, sending short and extremely safe sequences of activities, corresponding to plans computed for lower energy levels.
The last phase, LTS for *Long Term Science*, may start once the small solar panels of Philae receive enough energy to charge the secondary batteries, and a strong enough communication link is established with the lander.*[2](#fn2)*
In each phase, the plan executed by Philae were computed by the SONC in Toulouse. Then, they are encoded into machine-readable format by the *Lander Control Centre* (LCC) in Cologne and then sent to Rosetta via ESA's *European Space Operations Centre* (ESOC) and one of ESA's Deep Space Antennas in New Norcia, Cabreros or Malargüe. Finally they are transmitted from the orbiter to Philae.

#### Scheduling under Energy and Memory Constraints

Scheduling the experiments and activities of Philae can be seen as a *Resource-constrained multi-project scheduling problem* (RCMPSP), however, with additional specific features. Each experiment corresponds to a project, i.e., a sequence of activities themselves decomposed into tasks with precedence constraints. Besides a duration, each task is defined by two other fundamental characteristics: its demand in energy and a data production rate. These two quantities correspond to the usage of two resources, respectively, the instant power delivered by the battery and the memory available in the instruments and in the on-board computer.
The first type of resource, standing for the instant power usage, can be easily modelled using standard constraints for cumulative resources (`IloDiscreteResource` in IBM ILOG Scheduler). The instant power usage is in fact limited on three levels. First, there is threshold for the total instant power usage on the main battery, involving every task. Second, each task is associated to a converter, and each converter has its own threshold. Third, the tasks of a given converter are on a given power line, which also has a threshold. The constraint model therefore involves a hierarchy of cumulative resource constraints with different capacities, and each task requires the resource corresponding to its line, converter, and of course the main battery.
The second type of resource stands for memory available to store the data before its transfer to Rosetta and then to Earth.
Each experiment produces data on its own memory. This data will then transferred
back to Earth through the orbiter acting as a relay.
All transfers are managed by the *Command and Data Management System* (CDMS) following a
greedy policy. First, priorities are assigned off-line to experiments.
Then, on-line, data are systematically transferred from the
experiment of highest priority with available data to a central mass-memory,
then sent to the orbiter when it is in *visibility*,
i.e., above the horizon of the comet with respect to Philae.
This transfer policy may lead to data loss when
an experiment produces more data than its memory can store
and its priority is not high enough to allow a transfer to the mass-memory.
This was modelled within the previous release of MOST
using `Reservoir` constraints:
Data production tasks fill the reservoir, while multiple
pre-defined data transfer tasks of variable duration
empty it.
However, this modeling choice has several drawbacks and it
quickly became apparent that it was the critical aspect of the
problem to tackle in order to find better solutions faster.
In particular, transfer activities are neither known in advance nor controllable since they are triggered by the CDMS following a purely reactive policy. This approach therefore requires making simplifying assumption about data transfer, yielding an inaccurate and inefficient model.

#### A Global Constraint for Data Transfers

Instead data transfers can be altogether encapsulated into
a global constraint. The decision variables
are start times of data-producing tasks (data production rate and duration are known in advance)
and the priority permutation.
This allows to very quickly checking the satisfiability
of a schedule with respect to data transfer. Moreover, one can compute
bounds allowing to filter out the domains of the variables standing
for start time of the data-producing tasks.
The CDMS transfers data by blocks of 256 bytes. Its policy is relatively simple and can be described as follows:

Repeat (in parallel):
:   * Scan experiments by order of priority until
      one with at least one block of data on its memory is found.
      In that case, transfer one block from this experiment to the mass memory
      unless the mass memory is full.
    * If the orbiter is visible, and there is at least one block of data
      on the mass memory, then transfer one block from the mass memory to the orbiter

Given a set of priorities for the instruments and start times for data-producing activities, it is therefore possible to unroll this procedure in order to check whether data might be lost if this schedule is chosen.
However, when an instrument has high priority but produce less data than can be transferred to the mass-memory, the source of the transfer can rapidly change, from that instrument to another instrument with lower priority. An important step was to approximate this behaviour by a *bandwidth sharing* model. It can be shown that this model is very accurate, in fact the error in memory usage for a given instrument is at most 3 blocks of 256 bites in practice. Moreover, it is the basis of efficient checking and propagation algorithms, since the number of steps required to compute data transfers and memory usage with this method depends only in the number of data-producing activities. [Figure 3](#fig3) shows the schedule of three experiments as well as the resulting data transfers and memory usage.

|  |  |  |
| --- | --- | --- |
|  | Philae's data transfers |  |
|  | Figure 3. Illustration of the data transfers onboard Philae. |  |

#### Impact on the Mission

This approach reduces the solving time dramatically: from hours in some cases
to seconds in all scenarios considered so far by the SONC. Being able to compute and verify plans in a reasonable amount of time was extremely important to SONC operatives, and not only because reactivity of the software is always important to the users.
Indeed, if the plan sent to Philae when the operation started was given a relatively comfortable period (once the landing site was chosen) to be computed, other usages of MOST were under tighter time constraints. First, in order to choose the landing site, for instance,
several scenarios, corresponding to the different values for the parameters of visibility, sunshine period, etc. had to be solved in a short period.
Second, once on the comet, new updated plans, better optimised for the characteristics of the actual landing site and of the situation of Philae are computed under a lot of pressure and time efficiency is of great importance.
Moreover, the dedicated algorithms not only helped reducing the computation time, it also allowed a much more accurate verification of the transfers and therefore gave a better guarantee against data loss than the previous approach.

---

[Simonin et al. 15] G. Simonin, C. Artigues, E. Hebrard, P. Lopez.   
Scheduling scientific experiments for comet exploration.   
Constraints 20(1), 77-99, 2015[↩](#ref3 "Jump back to citation in the text.")   
  
[Chien et al. 13] S. Chien, G. Rabideau, D. Tran, F. Nespoli, D. Frew, H. Metselaar, F. Nespoli, D. Frew, H. Metselaar, M. Fernandez, M. Kueppers, L. O'Rourke.   
Scheduling science campaigns for the Rosetta mission: A preliminary report.   
In Proceedings of the International Workshop on Planning and Scheduling for Space (IWPSS). Moffett Field, CA, March 2013[↩](#ref2 "Jump back to citation in the text.")   
  
*1. Rosetta's findings actually show that the water contained in the comets 67P is not of the same type usually found in our oceans.
[↩](#ref1 "Jump back to footnote 1 in the text.")*
*2. At the time of writing, the first condition is met, however not yet the second because of the sublimation of the comet's ice making it difficult for Rosetta to orbit at close enough range.[↩](#ref4 "Jump back to footnote 2 in the text.")*
*Gilles Simonin, Christian Artigues, Emmanuel Hebrard, Pierre Lopez and Pauline Ballereau, of the Operations Research & Constraints group [(ROC)](https://www.laas.fr/public/en/roc).[↩](#back "Jump back to the text.")*

[view](/cp/success-stories/cp_has_landed_on_the_comet)

[Outperforming state-of-the-art compilers in Unison](/theses/outperforming_state-of-the-art)

[![Unison](/sites/default/files/unison-logo.png)](https://unison-code.github.io/)

Do you want to improve the quality of your code? Unison is a code generator for compilers with a radically new approach. Unison rethinks code generation using combinatorial optimization techniques. Unison is available on [Github](https://unison-code.github.io/) and is integrated with the regular LLVM toolchain.

A compiler is a program that transforms a source code from a high-level programming language into a lower level language (e.g., assembly language) to create an executable program. Compilers decompose code generation into multiple tasks (instruction selection, instruction scheduling, and register allocation) and solve each task in isolation with heuristics. Unison pursues a radically different route: it embraces and exploits the combinatorial, interdependent nature of code generation to drastically improve code quality. In Unison, the inter dependent code generation tasks are translated into a single combinatorial model that accurately reflects all inter dependencies. Solving the model with constraint programming, a modern combinatorial optimization technology, results in the desired high-quality assembly code.

Unison complements state-of-the-art compilers and is used by [Ericsson](https://www.ericsson.com/en/blog/2017/12/outperforming-state-of-the-art-compilers-in-unison).

[view](/theses/outperforming_state-of-the-art)