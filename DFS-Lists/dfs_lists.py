class Solution:

        def dfs_lists(self, lists, idx_list, result):

                # if current index list is equal to size of lists print and stop (base case recursion)
                if idx_list == len(lists):
                        print(result)
                        return

                # append all element list from lists, do recursion and remove last element
                for index in range(0, len(lists[idx_list])):
                        result.append(lists[idx_list][index])
                        self.dfs_lists(lists, idx_list + 1, result)
                        result.pop()


# Testing the code
if __name__ == '__main__' :

        s = Solution()

        # sample data
        arr = [["A", "BC"], ["DEF", "GHIJ", "LMNO"], ["P"]]
      
        s.dfs_lists(arr, 0, [])
        '''
        ['A', 'DEF', 'P']
        ['A', 'GHIJ', 'P']
        ['A', 'LMNO', 'P']
        ['BC', 'DEF', 'P']
        ['BC', 'GHIJ', 'P']
        ['BC', 'LMNO', 'P']
         '''
