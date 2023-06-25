// main.cpp 
// checks the sorting algorithm
#include <chrono>
#include <iostream>
#include <random>
#include <vector>

#include "sorting.h"

void uniform(std::vector<int> &arr, std::random_device& rd){
  std::mt19937 gen(rd());
  std::uniform_int_distribution<> dis(0,INT32_MAX);

  for (int& x : arr) {
    x = dis(gen);
  }
}

void almost_sorted(std::vector<int> &arr, std::random_device& rd){
  std::mt19937 gen(rd());
  size_t n = arr.size();
  std::uniform_int_distribution<> dis(0,n);

  for (size_t i = 0; i < n; i++)
  {
    arr[i] = i;
  }

  for (size_t i = 0; i < n/20; i++)
  {
    size_t i1 = dis(gen);
    size_t i2 = dis(gen);
    arr[i1] = i2;
    arr[i2] = i1;
  }
}

void almost_reverse(std::vector<int> &arr, std::random_device& rd){
  std::mt19937 gen(rd());
  size_t n = arr.size();
  std::uniform_int_distribution<> dis(0,n);

  for (size_t i = 0; i < n; i++)
  {
    arr[i] = n-1-i;
  }

  for (size_t i = 0; i < n/20; i++)
  {
    size_t i1 = dis(gen);
    size_t i2 = dis(gen);
    arr[i1] = n-1-i2;
    arr[i2] = n-1-i1;
  }
}

bool issorted(const std::vector<int>& vec) {
  for (size_t i = 1; i < vec.size(); i++) {
    if (vec[i] < vec[i - 1]) {
      return false;
    }
  }
  return true;
}

int main() {
  size_t size = 1000000;
  std::vector<int> arr(size);
  std::random_device rd;

  int iter = 50;

  auto dists = {uniform, almost_sorted, almost_reverse};

  for (auto arrgen : dists){
    std::chrono::duration<double> avg(0);
    for (size_t i = 0; i < iter; i++)
    {
      arrgen(arr, rd);
      auto start = std::chrono::high_resolution_clock::now();
      sort(arr);
      auto end = std::chrono::high_resolution_clock::now();
      std::chrono::duration<double> diff = end - start;
      if(!issorted(arr)){
        std::cout << "0.0\n0.0\n0.0\n";
        return 0;
      }
      avg += diff;
    }
    std::cout << avg.count() / double(iter) << std::endl;
  }
  
  return 0;
}
