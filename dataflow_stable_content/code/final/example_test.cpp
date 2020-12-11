// 67d7842dbbe25473c3c32b93c0da8047785f30d78e8a024de1b57352245f9689
#include <iostream>
#include <stdlib.h>
#include "example.h"

void example(strm_t &in1, strm_t &in2, strm_t &out);

int main()
{
  // Declare streams
  strm_t in1, in2, out;
  value_t valDataCtrl;

  valDataCtrl.data = 0;
  valDataCtrl.keep = 0xF;
  valDataCtrl.strb = 0;
  valDataCtrl.user = 0;
  valDataCtrl.last = 0;
  valDataCtrl.id = 0;
  valDataCtrl.dest = 0;

  // Write data into a and b
  for (int i = 0; i < 10; i++)
  {
	int a = rand() % 10;
	valDataCtrl.data = a;
    in1.write(valDataCtrl);
    int b = rand() % 10;
    valDataCtrl.data = b;
    in2.write(valDataCtrl);
    std::cout << "a = " << a << ", b = " << b << std::endl;
  }

  example(in1, in2, out);
  
  value_t sum = out.read();
  
  std::cout << "sum = " << sum.data << std::endl;
  
  return 0;
}
