#include <bits/stdc++.h>


using namespace std;

struct word{
  string text;
  int length;

};

bool compare(word a, word b){
  return a.length > b.length;
}

int main(){

   int a, i = 0;
   string s;
    word w;
   cin >> a;
    cin.ignore();
     vector<vector<word>> v(a + 4, vector<word>(0));
   while(a--){
     getline(cin, s);
     stringstream ss(s);
     while(getline(ss, s, ' ')){ 
       w.text = s;
       w.length = s.length();
       v[i].push_back(w); 
     }
     i++;
   }
    int c;
   for(int i = 0; i< v.size();i++){
     c = 0;
     stable_sort(v[i].begin(), v[i].end(), compare);
     for(auto k:v[i]){
       cout << k.text << ((c + 1) < v[i].size() ?  " ":"\n");
        c++;
     }
   }

}
