
#include <iostream>
using namespace std;
 
int main() {
   int t ;
   cin >> t ;
   while(t--){
        int k;
        cin >> k ;
        int  j = 0, res  = 0, a = 1;
    while (j < k){
        if ( a%3 != 0 && a%10 != 3 ){
            res = a ;
            j ++ ;
             }
        a ++ ;
        }
    cout << res  << endl ;

  }
  return 0;
}
