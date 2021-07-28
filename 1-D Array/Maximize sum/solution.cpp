#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h>

using std::cout; using std::cin;
using std::endl; using std::string;
using std::map; using std::copy;
using std::vector;

using namespace std; 

class Maximize{
    
    int length = 0;
    int n_distinct = 0;
    
    map<int,int> hashMap = {};
    
    vector<int> maxVector;
    
    int array[100000] = {0};
    int *arr = array;
    
    public:
    Maximize(int length, int n_distinct, int** array){
        this->length = length;
        this->n_distinct = n_distinct;
        this->arr = *array;
        printData();
        createMap();
        printMap();
        createMaxList();
        sortVector();
        printVector();

    }
    void printData(){
        cout << "Length : "<< length << "\nN Distinct: "<< n_distinct << "\n";
        cout << "Array: ";
        for(int i=0; i < length; i++){
            cout << *(arr+i) << " ";
        }
    }
    void createMap(){
        for(int i = 0; i < length; i++){
            if ( hashMap.find(*(arr+i)) == hashMap.end() ) {
              hashMap[*(arr+i)] = 1;
            } else {
              hashMap[*(arr+i)] += 1;
            }
        }
    }
    void printMap(){
        cout << "\n\nHashMap:\n[\n ";
        for (auto item : hashMap){
            cout << "\t" << item.first << ": " << item.second << "\n";
        }
        cout << "]\n";
    }
    void createMaxList(){
        for (auto item : hashMap){
            maxVector.push_back(item.first * item.second);
        }
    }
    void printVector(){
        cout << "\nSorted maxVector:\n";
        for(auto item : maxVector){
            cout << item << " ";
        }
    }
    void sortVector(){
        sort(maxVector.begin(), maxVector.end(), greater<int>());
    }
    int compute(){
        int res = 0;
        for(auto item: maxVector){
            if(n_distinct>0){
                res += item;
                n_distinct -= 1;
            }
        }
        return(res);
    }
    
};

int main()
{
    int length = 0;
    cout << "\nEnter the length of array: ";
    cin >> length;
    
    int n_distinct = 0;
    cout << "\nEnter the number of distinct digits to maximize sum on: ";
    cin >> n_distinct;

    cout << "\nEnter the items in the array: ";
    
    int array[100000] = {0};
    int *arr = array;
    for(int i = 0; i < length; i++){
        cin >> *(arr + i);
    }
    
    Maximize obj(length, n_distinct, &arr);
    cout << "\nResult: " << obj.compute();
    return 0;
}
