# Truth-Table-Generator

This is a very simple truth-table generator for 3 and 4-valued logics that I made for solving homework one evening when I was bored. It also can be used to check entailments, as long as your formula doesn't have too many variables.

It uses [lark-parser](https://github.com/lark-parser/lark) to parse the input formulas, which was very quick and easy to set up. After parsing the formula, the program will iterate over all possible assignments to the variables in the formula and recursively find the truth values of all connectives, and the entailment.

## Suported Logics

1. [**CPL**]() - Classical propositional logic, the boolean logic we all know and love.
2. [**K3**](https://en.wikipedia.org/wiki/Three-valued_logic#Logics)  - Kleen's 3-valued logic
3. [**B3**](https://en.wikipedia.org/wiki/Many-valued_logic#Bochvar's_internal_three-valued_logic_(also_known_as_Kleene's_weak_three-valued_logic)#Examples)  - Bochvar's internal 3-valued logic
4. [**LP**](https://en.wikipedia.org/wiki/Three-valued_logic#Logics)  - Priest's logic of paradox
5. [**L3**](https://en.wikipedia.org/wiki/Three-valued_logic#Logics)  - Lukasiewicz's 3-valued logic
6. [**RM3**](http://www.tptp.org/Seminars/RM3/LogicRM3.html) - R-mingle 3-valued logic
7. [**FDE**](https://en.wikipedia.org/wiki/Many-valued_logic#Bochvar's_internal_three-valued_logic_(also_known_as_Kleene's_weak_three-valued_logic)#Examples) - Belnap 4-valued logic, first degree entailment

## Dependancies

- python3
- lark-parser

## Instructions

To install the lark-parser dependancy:

```bash
$ pip install lark-parser
```

To run the program:

```bash
$ python3 ttable.py
```

## Syntax Reference

| **operator**   |                                                          |
|:--------------:|:--------------------------------------------------------:|
| `~p`           | not _p_                                                  |
| `p & q`        | _p_ and _q_                                              |
| `p \| q`       | _p_ or _q_                                               |
| `p -> q`       | _p_ implies _q_                                          |
| `p <-> q`      | _p_ is equivalent to _q_                                 |
| **atom**       |                                                          |
| `p`            | any sequence of **_lowercase_** characters is a variable |
| `1` or `T`     | _true_                                                   |
| `0` or `F`     | _false_                                                  |
| `I` or `U`     | _unspecified_ for 3-valued logic                         |
| `B`            | _both_ true and false for 4 valued logic                 |
| `N`            | _neither_ true nor false for 4 valued logic              |
| **entailment** |                                                          |
| `p \|= q`      | _p_ entails _q_ in classic propositional logic (CPL)     |
| `p \|=L q`     | _p_ entails _q_ in logic "L" (see above)                 |
| `\|= p`        | _p_ is a tautology in classical propositional logic      |
| `\|=L p`       | _p_ is a tautology in logic "L" (see above)              |

## Example

Checks if the entailment `¬p ∨ q ⊨ p → q` holds in [K3](https://en.wikipedia.org/wiki/Three-valued_logic#Logics).

```bash
> ~p | q |=K3 p -> q

  (~p | q) |=K3 (p -> q)
..........................
   10 1 0   1    0 1  0
   10 1 i   1    0 1  i
   10 1 1   1    0 1  1
   ii i 0   1    i i  0
   ii i i   1    i i  i
   ii 1 1   1    i 1  1
   01 0 0   1    1 0  0
   01 i i   1    1 i  i
   01 1 1   1    1 1  1

entailment always holds
```
