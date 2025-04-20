#include <stdio.h>
struct superhero{
    char name[20];
    int code;
    int kill[5];
    float avg;
};
float average(int kill[]){
    int s=0;
    for(int i=0;i<5;i++) s+=kill[i];
    return s/5.0;
}
void main(){
    int n,i,j;
    scanf("%d",&n);
    struct superhero hero[n];
    for(i=0;i<n;i++){
        scanf("%s",hero[i].name);
        scanf("%d",&hero[i].code);
        for(j=0;j<5;j++)
            scanf("%d",&hero[i].kill[j]);
        hero[i].avg=average(hero[i].kill);
    }
    for(i=0;i<n;i++)
        printf("%d %.1f\n",hero[i].code,hero[i].avg);
}