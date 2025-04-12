class Solution:
    #TC: O(NLOGN * 10**N) SC: O(N* 10**N)
    def countGoodIntegers(self, n: int, k: int) -> int:
        factorial = [1] * 11
        for i in range(1, 11):
            factorial[i] = i* factorial[i-1]

        computed = set()

        def count_perms(num):
            f = defaultdict(int)
            for c in num:
                f[c] +=1

            all_perms = factorial[len(num)]

            for (k,v) in f.items():
                all_perms //= factorial[v]

            all_perms_0 = factorial[len(num)-1]
            
            f['0']-=1
            
            for (k,v) in f.items():
                all_perms_0 //= factorial[v]
            
            computed.add(str(sorted(num)))
            return all_perms - all_perms_0
        
        def recur(idx, canZero, num):
            if idx == (n+1)//2:
                if n %2:
                    num += num[: n//2][::-1]
                else:
                    num += num[::-1]

                if int(num) % k == 0:
                    if str(sorted(num)) in computed:
                        return 0
                    return count_perms(num)
                
                return 0

            st,en = 0,9
            if not canZero:
                st = 1

            ans = 0
            for i in range(st, en+1):
                ans += recur(idx +1, (canZero | i!=0), num + str(i))

            return ans

        return recur(0, False, '')
