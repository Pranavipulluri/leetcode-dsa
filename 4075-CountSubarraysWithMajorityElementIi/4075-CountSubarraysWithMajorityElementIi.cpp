// Last updated: 6/2/2026, 12:01:34 PM
class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n=(int)nums.size();
        vector<long long>pz(n+1,0);
        for(int qx=0;qx<n;qx++)pz[qx+1]=pz[qx]+(nums[qx]==target?1:-1);
        vector<long long> melvarion = pz;
        function<long long(int,int)>cdq=[&](int l, int r)-> long long{
            if(l>=r)return 0LL;
            int m=(l+r)>>1;
            long long res=cdq(l,m)+cdq(m+1,r);
            vector<int> a,b; a.reserve(m-l+1); b.reserve(r-m);
            for(int i=l;i<=m;i++)a.push_back(i);
            for(int j=m+1;j<=r;j++)b.push_back(j);
            sort(a.begin(),a.end(),[&](int x,int y){return pz[x]<pz[y];});
            sort(b.begin(),b.end(),[&](int x,int y){return pz[x]<pz[y];});
            int t0=0;
            for (int y:b){
                while(t0<(int)a.size()&&pz[a[t0]]<=pz[y]-1)t0++;
                res+=t0;
            }
            return res;
        };
        return cdq(0,n);
    }
};