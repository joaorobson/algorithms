#include <bits/stdc++.h>

using namespace std;

int minSwaps(string s, int n){
  pair<char, int> stringPos[n];

  for(int i = 0;i< n;i++){
    stringPos[i].first = s[i];
    stringPos[i].second = i;
  }

  sort(stringPos, stringPos + n);

      vector<bool> vis(n, false);

    // Initialize result
    int ans = 0;

    // Traverse array elements
    for (int i = 0; i < n; i++)
    {
        // already swapped and corrected or
        // already present at correct pos
        if (vis[i] || stringPos[i].second == i)
            continue;

        // find out the number of  node in
        // this cycle and add in ans
        int cycle_size = 0;
        int j = i;
        while (!vis[j])
        {
            vis[j] = 1;

            // move to next node
            j = stringPos[j].second;
            cycle_size++;
        }

        // Update answer by adding current cycle.
        if (cycle_size > 0)
        {
            ans += (cycle_size - 1);
        }
    }

    // Return result
    return ans;
}

int main(){
  int a, b, inv = 0;
  cin >> a;
  string s;
  while(a--){
    set<char> ss;
    cin >> b;
    cin >> s;
    for(auto l:s){
      ss.insert(l);
    }
    if(s.length() == 1 || ss.size() != s.length() || minSwaps(s, s.length()) != 1){
      cout << "There aren't the chance."<< endl;
    }
    else{
      cout << "There are the chance." << endl;

    }
  }

}
