// Last updated: 6/2/2026, 12:01:25 PM
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n=(int)nums.size();
        if (n==0) return 0;
        int w0= 1, p = 0;
        deque<int> g1;
        for (int q= 0; q < n; ++q) {
            if (q && nums[q- 1] > nums[q])
                g1.push_back(q - 1);
            while (true) {
                while (!g1.empty() && g1.front() < p)
                    g1.pop_front();
                bool ok=false;
                if (g1.empty()) {
                    ok=true;
                }
                else if ((int)g1.size()>=2) {
                    ok =false;
                }
                else {
                    int h= g1.front();
                    bool rA= (h==p)||(nums[h-1]<=nums[h + 1]);
                    bool rB = (h +1 ==q)||(nums[h] <=nums[h + 2]);
                    ok= rA||rB;
                }
                if (ok) break;
                ++p;
            }
            w0=max(w0,q- p + 1);
        }
        return w0;
    }
};