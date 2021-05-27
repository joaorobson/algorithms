#include <iostream>
#include <queue>

using namespace std;

class BT{
  private:
    struct Node{
      int info;
      Node *left, *right;
    };
  public:
    Node *root;
    BT(): root(nullptr){};

    void bfs(){
      queue<Node*> q;
      vector<int> v;
      q.push(root);
      while(not q.empty()){
        auto node = q.front();
        q.pop();
        if(node){
          v.push_back(node->info);
          q.push(node->left);
          q.push(node->right);

        }
      }
      for(int i = 0;i < v.size();i++){
        cout << v[i] << (i == v.size() - 1 ? "\n":" ");
      }
    }
    void insert(int n){
      Node *node = root, *prev = nullptr;
      while(node){
        prev = node;
        if(n == node->info)
          return;
        else if(n < node->info)
          node = node->left;
        else
          node = node->right;
      }
      node = new Node{n, nullptr, nullptr};

      if(!root)
        root = node;
      else if(node->info < prev->info)
        prev->left = node;
      else
        prev->right = node;
    }
};
 


int main(){
  int a,b,c;
  cin >> a;
  for(int i = 0;i < a;i++){
    cin >> b;
    BT tree;
    for(int k = 0;k < b;k++){
      cin >> c;
      tree.insert(c);
    }
    cout << "Case "<< i + 1 << ":" << endl;
    tree.bfs();
    cout << endl;
  }

}
