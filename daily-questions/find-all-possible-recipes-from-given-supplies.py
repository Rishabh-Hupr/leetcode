from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        '''
            https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
            Time: O(V+E)
            Space: O(V+E+n)
        '''
        adj = defaultdict()
        supplies = set(supplies)
        cooked = set()
        cooking = set()
        
        for i in range(len(recipes)):
            adj[recipes[i]] = list(ingredients[i])
        
        for recp in adj:
            if recp not in cooked:
                stk = [[recp, 0]]
                while stk:
                    elem, counter = stk[-1][0], stk[-1][1]
                    if elem not in cooked:
                        cooking.add(elem)
                        flag = True
                        while counter < len(adj[elem]):
                            ing = adj[elem][counter]
                            if ing in adj:
                                if ing in cooking:
                                    stk.pop()
                                    flag = False
                                    break
                                if ing not in cooked:
                                    stk.append([ing, 0])
                                    flag = False
                                    break
                            elif ing not in supplies:
                                stk.pop()
                                flag = False
                                break
                            counter += 1
                            stk[-1][1] = counter

                        if flag:
                            cooked.add(elem)
                            cooking.remove(elem)
                            stk.pop()
        return list(cooked)
