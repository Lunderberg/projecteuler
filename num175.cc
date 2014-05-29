#include <iostream>

using namespace std;

int gcd(int a, int b){
  if (b==0){
    return a;
  } else {
    return gcd(b, a%b);
  }
}

struct frac{
  frac(int x,int y){
    num = x;
    denom = y;
  }
  int num;
  int denom;
  bool operator==(frac other){
    return num==other.num && denom==other.denom;
  }
  bool operator!=(frac other){
    return !(num==other.num && denom==other.denom);
  }
  frac reciprocal(){
    return frac(denom,num);
  }
};

frac next(frac x){
  int y = 2*(x.num/x.denom)+1;
  return frac(x.denom,y*x.denom-x.num);
}

int main(){
  frac x(1,1);
  //frac wanted(13,17);
  frac wanted(13717421,109739369);
  long long int i=1;
  while(x.reciprocal()!=wanted){
    if (!(i%int(1e0))){
      cout << "Checking " << i << " "
	   << x.num << "/" << x.denom << endl;
    }
    x = next(x);
    i++;
  }
  cout << i << " " << x.num << "/" << x.denom << endl;
}
