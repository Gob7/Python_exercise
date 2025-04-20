#include <stdio.h>
int produce(int age, int day){
    if (day==1) return 1;
    day--;
    if (age>=3) return 0;
    age++;
    return produce(age,day)+2*produce(1,day);
}
void main(){
    int t,n,i,x;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        int ans=0;
        for(i=0;i<n;i++){
            scanf("%d",&x);
            ans+=produce(x,7);
        }
        printf("%d\n",ans);
    }
}