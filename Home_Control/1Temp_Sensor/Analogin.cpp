#include <fstream>
#include "Analogin.h"

using namespace std;

Analogin::Analogin(){
}

Analogin::Analogin(unsigned int n){
  number = n;
}

void Analogin::setNumber(unsigned int n){
  number = n;
}

int Analogin::readAdcSample(){
  string line = "/sys/bus/iio/devices/iio:device" + to_string(number)+"/in_voltage" + to_string(number) + "_raw";
  int results;
  fstream fs;
  fs.open(line.c_str(),fstream::in);
  fs >> results;
  fs.close();
  return results;
} 

Analogin::~Analogin(){
}
