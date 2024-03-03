#include<bits/stdc++.h>
using namespace std;

void printVec(vector<int>v){
    cout<<"size: "<<v.size();
    for(int i=0;i<v.size();i++){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}

int main(){
    // dynamic sized arrays
    vector<int>v;
    int n; //can take any number of values
    cin>>n;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        v.push_back(x); // add values to end of the vector. TC - O(1)
    }
    printVec(v);

    // Vector constructors.
    vector<int>v_1(10); // declares a vector of size 10 having 0 values.
    vector<int>v_2(10,1); // declares a vector of size 10 and all elements will have value = 1.

    v.pop_back(); // removes last value of the vector - O(1) 

    // copying vector
    vector<int>v2 = v; // O(n)
    // Copying vector is expensive operation as it takes O(n). If we want to make in-place changes to vector pass it as reference using &.

}