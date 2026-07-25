---
title: "Hybrid Optimization of Vehicle Routing Problems"
date: 2026-07-25T15:04:36+0200
draft: false
---

### Author

Edward Lam

### School

University of Melbourne

### Supervisors

Pascal Van Hentenryck

### Abstract

Vehicle routing problems are combinatorial optimization problems that aspire to design vehicle routes that minimize some measure of cost, such as the total distance traveled or the time at which the last vehicle returns to a depot, while adhering to various restrictions. Vehicle routing problems are of profound interest in both academia and industry because they are opportunities to study graph structures and algorithms, and because they underpin practical applications in a multitude of industries, but notably, the transportation and logistics industries. This dissertation presents two applications relevant to industry and develops a fully hybrid method for solving a classical vehicle routing problem.

The first application combines vehicle routing with crew scheduling. In industry, vehicle routing and crew scheduling are usually performed in stages due to the large search space of integrated models. The first stage finds minimal-cost vehicle routes with little consideration to crew constraints and objectives. The second stage schedules crews on the routes from the first stage. Disregarding crew constraints in the first stage can lead to suboptimality or even infeasibility of the overall problem in the second stage. To quantify the suboptimality of staged optimization models, two formulations of the integrated problem are developed. The first is an ordinary mixed integer programming model, and the second is a constraint programming model containing a linear relaxation global constraint that performs cost-based filtering. The two integrated models are solved using a branch-and-bound search and a highly specialized large neighborhood search. The large neighborhood search exploits the substructures linking the vehicle routing and crew scheduling elements of the problem, and when executed on the constraint programming model, is shown to perform significantly better than the other approaches.

The second application introduces a number of scheduling constraints to the Vehicle Routing Problem with Pickup and Delivery and Time Windows. The scheduling constraints arise from a lack of loading bays or equipment that unloads and loads incoming vehicles. These constraints limit the number of vehicles present or in service at any particular site by requiring the arrival of vehicles to be scheduled around the availabilities of a scarce resource. A mixed integer programming model, a constraint programming model and a sequential model are implemented for the problem but are shown to be inferior to a branch-and-price-and-check model, which hybridizes column generation and constraint programming with nogood learning.

This thesis concludes with a hybrid method, named Branch-and-Check with Explanations, that unifies linear programming, constraint programming and Boolean satisfiability. The method begins with a linear programming model that omits several critical constraints. The solver uses the linear programming model to find objective bounds and candidate solutions, which are checked by a constraint programming model for feasibility of the omitted constraints. A Boolean satisfiability model performs conflict analysis on infeasible candidate solutions to derive nogood cuts, which are placed into the linear programming model and the constraint programming model. The method is implemented in a proof-of-concept solver for the Vehicle Routing Problem with Time Windows and is shown to be competitive against a branch-and-cut model while avoiding the intricacies involved in developing the cutting planes and separation algorithms required in branch-and-cut.

### Graduated

Wednesday, April 17, 2019 - 12:00

### Link to full text

[Hybrid Optimization of Vehicle Routing Problems](https://minerva-access.unimelb.edu.au/handle/11343/220534)

### Also published in

[Joint Vehicle and Crew Routing and Scheduling](https://link.springer.com/chapter/10.1007/978-3-319-23219-5_45)

[A branch-and-price-and-check model for the vehicle routing problem with locatio…](https://link.springer.com/article/10.1007/s10601-016-9241-2)

[Branch-and-check with explanations for the Vehicle Routing Problem with Time Wi…](https://link.springer.com/chapter/10.1007/978-3-319-66158-2_37)

### Notes

The paper "A branch-and-price-and-check model for the vehicle routing problem with location congestion" was submitted to CPAIOR and accepted for journal fast-track. The thesis was awarded the Doctoral Research Award.