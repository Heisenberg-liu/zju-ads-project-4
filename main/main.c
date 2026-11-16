#include <stdio.h>
#include <stdlib.h>


const long long MOD= 1000000007;


int main()
{
    int n,m;
    scanf("%d %d",&n,&m);
    long long record;
    long long bucket_DP[100005]={0};
    long long bucket_allcase[100005]={0};
    long long DP;   //DP[i]等于以ai结尾的beautiful子序列，DP[i]=ai附近大小的值的所有子序列可能数量+离ai比较远的数字的DP的和 
    long long sum_DP_all=0;    //此前的DP的和 
    long long power=1;
    for(int i=0;i<n;i++)  //查询采用先来后到的模式，先出现的数字不会把后面出现的数字的可能子序列计入
    {
        DP=0;
        scanf("%lld",&record);     
        int lower_ground=record-m;
        int upper_ground=record+m;
        if(lower_ground<0) lower_ground=0;
        if(upper_ground>=100000) upper_ground=100000;
        long long sum_DP_near=0;   //ai周围部分的DP和 
        long long sum_case=0;     //ai周围部分的子序列可能情况的和 
        for(int k=lower_ground;k<=upper_ground;k++)
        {
            sum_case=(sum_case+bucket_allcase[k])%MOD;
            sum_DP_near=(sum_DP_near+bucket_DP[k])%MOD;
        }
        bucket_allcase[record]=(bucket_allcase[record]+power)%MOD;   //值为record的数字的所有子序列可能性都被加进了bucket里面去 
        DP=(sum_DP_all-sum_DP_near+sum_case+MOD)%MOD;  //这里采用的是已知所有DP的和减去附近的DP得到其他部分的DP的和，后面出现的数字不会被计入，保证了情况不重复 
        bucket_DP[record]=(bucket_DP[record]+DP)%MOD;
        sum_DP_all=(sum_DP_all+DP)%MOD;
        power=(power*2)%MOD;
    }
    printf("%lld",sum_DP_all%MOD); //把所有以ai结尾的数字beautiful序列加起来即可 
}