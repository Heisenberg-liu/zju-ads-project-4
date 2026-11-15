#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int n,m;
    scanf("%d %d",&n,&m);
    int *record=malloc(sizeof(int)*n);
    int bucket_DP[100005]={0};
    int bucket_allcase[100005]={0};
    int *DP=malloc(sizeof(int)*n);   //DP[i]等于以ai结尾的beautiful子序列，DP[i]=i序号以前所有的beautiful序列+ai正负m以内的所有DP的值（用bucket[]存储）
    for(int i=0;i<n;i++)
    {
        DP[i]=0;
        scanf("%d",&record[i]);
        bucket_allcase[record[i]]+=pow(2,i);
    }
    int sum_DP_all=0;
    for(int i=0;i<n;i++)
    {
        int lower_ground=record[i]-m;
        int upper_ground=record[i]+m;
        if(lower_ground<0) lower_ground=0;
        if(upper_ground>=100000) upper_ground=100000;
        int sum_DP_near=0;   
        int sum_case=0;
        for(int k=lower_ground;k<=upper_ground;k++)
        {
            sum_case+=bucket_allcase[k];
            sum_DP_near+=bucket_DP[k];
            
        }
        DP[i]=sum_DP_all-sum_DP_near+sum_case;
        bucket_DP[i]+=DP[i];
        sum_DP_all+=DP[i];
    }
    printf("%d",sum_DP_all);
}