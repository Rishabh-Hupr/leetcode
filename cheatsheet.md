# Interview Lessons

---

# Variable Naming (Interview Standard)

## Common Short Names

ans        # final answer
res        # result list
n, m       # sizes
i, j, k    # indices
l, r       # two pointers
mid        # binary search middle
dp         # dynamic programming table
memo       # memoization cache
adj        # adjacency list (graph connections)
vis        # visited set
nei        # neighbor node
dirs       # directions (grid movement offsets)
pq         # priority queue
heap       # heap structure
cnt        # counter
freq       # frequency map
cur        # current value
prev       # previous value

Rule:
- Used many times → short name
- Used few times → clarity > shortness
- Never overly verbose

---

# 30-Second Pattern Checklist

Ask immediately:

1. Contiguous? → Sliding Window / Prefix Sum  
   (Contiguous = continuous elements, no gaps)

2. Optimal substructure? → DP  
   (Big answer built from smaller answers)

3. Connections / paths? → Graph (BFS/DFS)  
   (Nodes connected like network)

4. Minimize max / maximize min? → Binary Search on Answer  
   (Answer has monotonic behavior)

5. Top-K / priority? → Heap  
   (Need smallest/largest repeatedly)

6. Intervals? → Greedy / Sorting  
   (Ranges like meeting times)

7. Next greater / smaller? → Monotonic Stack  
   (Monotonic = always increasing or always decreasing)

Classify before solving.  
Meaning: Decide the problem category first. Don’t jump to code.

---

# SDE1 vs SDE2 Thinking

## SDE1
- Correct solution
- Clean implementation
- Basic complexity awareness

## SDE2
- Discuss tradeoffs
- Mention alternative approaches
- Constraint-driven reasoning
- Edge cases unprompted
- Optimization awareness
- Clean structure before coding

Upgrade move:
Always explain WHY approach is chosen.

---

# What Shows Experience

- Restate problem clearly
- State brute force first
- Reject brute force with reasoning
- Mention time/space complexity naturally
- Handle edge cases early
- Clean variable discipline
- No panic when debugging

Signal:
Calm thinking > fast typing.

---

# What To Do When Stuck

1. Think brute force first.
2. Check constraints (n size? values large?).
3. Try sorting.
4. Try sliding window.
5. Try binary search on answer.
6. Reduce problem size (k=1? small example?).
7. Draw small input and simulate manually.
8. Reverse the problem (validate X instead of compute X).
9. Think in categories (DP? Graph? Greedy?).

Never go silent.
Always speak your thinking process.

---

# Problem Solving Mental Loop

When blank, cycle through:

- Brute force?
- Sort?
- Two pointers?
- Sliding window?
- Binary search?
- Prefix sum?
- Hashing?
- Heap?
- Graph?
- DP?

One pattern usually fits.

---

# Important Concept Notes

Monotonic:
Something that only increases or only decreases (never changes direction).

Binary Search on Answer:
If answer X works, then all larger (or smaller) values also work.
This predictable pattern allows binary search.

Sliding Window:
Move two pointers while maintaining a condition on a continuous segment.

Greedy:
Make the best local choice each step, hoping it gives global best result.

DP (Dynamic Programming):
Store results of smaller subproblems to avoid recomputation.

---

# Coding Structure Template

1. Restate problem
2. Analyze constraints
3. Discuss brute force
4. Derive optimized approach
5. State complexity
6. Code cleanly
7. Check edge cases

---

# Core Archetypes To Master

1. Sliding Window
2. Two Pointers
3. Binary Search on Answer
4. Prefix Sum
5. Hash + Counting
6. Monotonic Stack
7. Heap / Top-K
8. Graph Traversal
9. Dynamic Programming
10. Greedy / Intervals

Master these → covers most interview problems.