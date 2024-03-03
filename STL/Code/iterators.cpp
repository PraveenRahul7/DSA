#include<bits/stdc++.h>
using namespace std;

void printContainer(auto v){
    for(auto ele:v){
        cout<<ele<<" ";
    }
    cout<<endl;
}

int main(){
    vector<pair<int,int>>v_pair = {{1,2}, {2,3}, {3,4}, {4,5}, {5,6},{6,7}};
    //declaring iterator:
    vector<pair<int,int>> :: iterator it; // iterator type should be of same type as the container that is getting iterated.

    for(it = v_pair.begin();it !=v_pair.end();++it){
        //cout<<(*it).first<<" "<<(*it).second<<endl; // it gives address and (*it) is actual value. In this case *it is a vector.
        cout<<it->first<<" "<<it->second<<endl;
    }

    // Range based loops and auto keyword

    //Range-based loops:
    vector<int>v = {1,2,3,4,5,6,7};
    for(int value:v){
        // here value is copy of contents in vector v. we might need to change the contents of the vector then we need to use reference. for(int &value:v){...}
        cout<<value<<" ";
    }
    cout<<endl;
    //printContainer(v);

    /*
    The auto keyword is used for automatic type inference, allowing the compiler to deduce the data type of a variable from its initializer. It was introduced in C++11 as part of the modernization of the language, providing more concise and readable code
    */
    //auto a = 1; // automatic type inference to int.
    for(auto i = v.begin(); i!=v.end();i++){
        cout<<(*i)<<" ";
    }
    cout<<endl;
    // auto keyword usage with range based loops.
    for(auto it:v){
        cout<<it<<" "; //we get values directly
    }
    cout<<endl;
    printContainer(v);

    return 0;
}