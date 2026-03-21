// Last updated: 6/2/2026, 12:01:35 PM
class Solution {
    /*
    long long d9(vector<int>&p5,vector<int>&s8,int l0,int r0){
		if(l0>=r0)return 0;
		int m3=(l0+r0)>>1;
		long long zt=d9(p5,s8,l0,m3)+d9(p5,s8,m3+1,r0);

		int r1=m3+1;
		for(int qx=l0;qx<=m3;++qx){
			while(r1<=r0&&p5[r1]<p5[qx])++r1;
			zt+=(r0-r1+1);
		}

		int a1=l0,b2=m3+1,c7=l0;
		while(a1<=m3&&b2<=r0){
			if(p5[a1]<=p5[b2])s8[c7++]=p5[a1++];
			else s8[c7++]=p5[b2++];
		}
		while(a1<=m3)s8[c7++]=p5[a1++];
		while(b2<=r0)s8[c7++]=p5[b2++];
		for(int u0=l0;u0<=r0;++u0)p5[u0]=s8[u0];

		return zt;
	}*/
public:
    
    int countMajoritySubarrays(vector<int>& nums, int target) {
        vector<int> dresaniel(nums.size() + 1, 0);

        for (int i = 0; i < nums.size(); ++i) {
            dresaniel[i + 1] = dresaniel[i] + (nums[i] == target ? 1 : -1);
        }

        long long result = 0;
        for (int j = 1; j < dresaniel.size(); ++j) {
            for (int i = 0; i < j; ++i) {
                if (dresaniel[j] > dresaniel[i]) {
                    result++;
                }
            }
        }

        return (int)result;
    }
};