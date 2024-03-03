#include<bits/stdc++.h>
using namespace std;

int main(){
    pair<int, string>p;

    // initializing pairs
    p = {1,"hello"}; // direct initialization 
    cout<<p.first<<" "<<p.second<<endl;
    p = make_pair(7,"rahul"); // using make_pair function
    cout<<p.first<<" "<<p.second<<endl;

    // tie: unpacking pair values.
    int num;
    string name;
    tie(num, name) = p;
    cout<<num<<" "<<name<<endl;

    // usage with arrays
    int a[] = {1,2,3};
    int b[] = {2,3,4};
    pair<int,int> p_array[3];
    for(int i=0;i<3;i++){
        p_array[i].first = a[i];
        p_array[i].second = b[i];
    }
    for(int i=0;i<3;i++){
        cout<<p_array[i].first<<" "<<p_array[i].second<<endl;
    }
}