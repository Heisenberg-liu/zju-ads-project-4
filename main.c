#include <stdio.h>
#include <stdlib.h>
#include <math.h>

const long long MOD= 1000000007;


int main()
{
    int n,m;
    scanf("%d %d",&n,&m);
    long long *record=malloc(sizeof(long long)*n);
    long long bucket_DP[100005]={0};
    long long bucket_allcase[100005]={0};
    long long *DP=malloc(sizeof(long long)*n);   //DP[i]等于以ai结尾的beautiful子序列，DP[i]=ai附近大小的值的所有子序列可能数量+离ai比较远的数字的DP的和 
    long long sum_DP_all=0;    //此前的DP的和 
    long long power=1;
    for(int i=0;i<n;i++)
    {
        DP[i]=0;
        scanf("%lld",&record[i]);     
        int lower_ground=record[i]-m;
        int upper_ground=record[i]+m;
        if(lower_ground<0) lower_ground=0;
        if(upper_ground>=100000) upper_ground=100000;
        long long sum_DP_near=0;   //ai周围部分的DP和 
        long long sum_case=0;     //ai周围部分的子序列可能情况的和 
        for(int k=lower_ground;k<=upper_ground;k++)
        {
            sum_case=(sum_case+bucket_allcase[k])%MOD;
            sum_DP_near=(sum_DP_near+bucket_DP[k])%MOD;
        }
        bucket_allcase[record[i]]=(bucket_allcase[record[i]]+power)%MOD;   //值为record的数字的所有子序列可能性都被加进了bucket里面去 
        DP[i]=(sum_DP_all-sum_DP_near+sum_case+MOD)%MOD;  //这里采用的是已知所有DP的和减去附近的DP得到其他部分的DP的和，后面出现的数字不会被计入，保证了情况不重复 
        bucket_DP[record[i]]=(bucket_DP[record[i]]+DP[i])%MOD;
        sum_DP_all=(sum_DP_all+DP[i])%MOD;
        power=(power*2)%MOD;
    }
    printf("%lld",sum_DP_all%MOD); //把所有以ai结尾的数字beautiful序列加起来即可 
}