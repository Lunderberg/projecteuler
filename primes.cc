#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

vector<long long> primes;
long long maxchecked;

bool checknext(){
  long long val = maxchecked+1;
  double maxchecking = sqrt(val);
  bool isprime = true;
  for(vector<long long>::iterator prime = primes.begin(); prime != primes.end(); prime++){
    if(val % (*prime) == 0){
      isprime = false;
      break;
    } else if ( (*prime) > maxchecking) {
      break;
    }
  }
  if (isprime){
    primes.push_back(val);
  }
  maxchecked = val;
  return isprime;
}

void advanceto(long long val){
  while (maxchecked <= val){
    checknext();
  }
}

long long findnextprime(){
  while(!checknext()){}
  return primes.back();
}

vector<long long> primefactors(long long val){
  vector<long long> factors;
  long long remainder = val;
  for(vector<long long>::iterator prime = primes.begin(); prime != primes.end(); prime++){
    while( remainder % (*prime) == 0){
      factors.push_back(*prime);
      remainder /= *prime;
    }
    if (remainder==1){
      break;
    }
  }
  while(remainder!=1){
    long long prime = findnextprime();
    while(remainder % (prime) == 0){
      factors.push_back(prime);
      remainder /= prime;
    }
  }
  return factors;
}

long long highestprimefactor(long long val){
  for(int i=2; i<val; i++){
    while (val % i == 0){
      val /= i;
    }
  }
  return val;
}

int main(){
  primes.push_back(2);
  maxchecked = 2;
  vector<long long> factors = primefactors(600851475143);
  for(vector<long long>::iterator fact = factors.begin(); fact != factors.end(); fact++){
    cout << *fact << "\t";
  }
  cout << endl;
  //advanceto(1000000);
  cout << highestprimefactor(600851475143) << endl;
}
