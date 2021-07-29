#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h>

using namespace std; 

class Maximize{
    
    int length;
    int n_distinct;
    map<int,int> hashMap = {};
    vector<int> maxVector;
    int *arr;
    
    public:
    Maximize(int length, int n_distinct, int** array){
        this->length = length;
        this->n_distinct = n_distinct;
        this->arr = *array;
        createMap();
        createMaxList();
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
    void createMaxList(){
        for (auto item : hashMap){
            maxVector.push_back(item.first * item.second);
        }
		sort(maxVector.begin(), maxVector.end(), greater<int>());
    }
    int compute(){
        int res = 0, tmp = 0;
        for(auto item: maxVector){
            if(n_distinct==0){
				break;
			}
			tmp = res + item;
			if(tmp > res){
				res = tmp;
				n_distinct -= 1;
			}else{
				break;
			}
        }
        return(res);
    } 
};

int main()
{
	int n_testCases = 0;
	cin >> n_testCases;

	for (int i = 0; i < n_testCases; i++){
		int length = 0;
		cin >> length;		
		int n_distinct = 0;
		cin >> n_distinct;
		int *arr = new int[length];
		for(int i = 0; i < length; i++){
			cin >> *(arr + i);
		}
		
		Maximize obj(length, n_distinct, &arr);
		cout << obj.compute() << endl;
	}
    return 0;
}