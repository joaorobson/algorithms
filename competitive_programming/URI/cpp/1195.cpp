#include <iostream>

using namespace std;


class BT{
  private:
    struct Node{
      int info;
      Node* left;
      Node* right;
    };
  public:
    Node* root;
    BT(): root(nullptr){}

    void insert(int a){
      Node *node = root, *prev = nullptr;

      while(node){
        prev = node;

        if (node->info == a)
          return;
        else if (a < node->info)
          node = node->left;
        else 
          node = node->right;
      }

      node = new Node {a, nullptr, nullptr};

      if (!root)
        root = node;
      else if (prev->info < a)
        prev->right = node;
      else
        prev->left = node;
    }

    void inorder(Node* node){
      if(node){
        inorder(node->left);
        cout << " " << node->info;
        inorder(node->right);
      }
    }
    void preorder(Node* node){
      if(node){
        cout << " " << node->info;
        preorder(node->left);
        preorder(node->right);
      }
    }
    void posorder(Node* node){
      if(node){
        posorder(node->left);
        posorder(node->right);
        cout << " " << node->info;
      }
    }
};

int main(){
  int a;
  cin >> a;
  for(int k = 1; k <= a;k++){
    int b, i;
    BT tree;
    cin >> b;
    while(b){
        cin >> i;
        tree.insert(i);
        b--;
    }
    cout << "Case " << k << ":" << endl;
    cout << "Pre.:";
    tree.preorder(tree.root);
    cout << "\nIn..:";
    tree.inorder(tree.root);
    cout << "\nPost:";
    tree.posorder(tree.root);
    cout << endl;
    cout << endl;

  }


}
