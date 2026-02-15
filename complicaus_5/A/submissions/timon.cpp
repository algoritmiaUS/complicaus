#include <array>
#include <cstdio>
#include <iostream>
#include <limits>

constexpr int maxw = 700;
constexpr int SIZE = 2 * maxw + 1;
constexpr long double pi_over_2 = 1.570796326794896619231L;

template <class T> void f(T &lhs, T rhs) {
  if (lhs > rhs) lhs = rhs;
}

int main() {
  int R, C;
  std::cin >> R >> C;

	std::array<std::array<bool, maxw>, maxw> is_circ;
  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      char ch;
      std::cin >> ch;
      is_circ[r][c] = (ch == 'O');
    }
  }

  std::array<std::array<long double, SIZE>, SIZE> sp;
  for (int r = 0; r <= 2*R; ++r)
    sp[r].fill(std::numeric_limits<long double>::infinity());
  
  sp[0][0] = 0.0L;
  for (int r = 0; r <= 2*R; ++r) {
    for (int c = 0; c <= 2*C; ++c) {
      if (r%2 == 0 && c < 2*C)
        f(sp[r][c+1], sp[r][c] + 1.0L);
      if (c%2 == 0 && r < 2*R)
        f(sp[r+1][c], sp[r][c] + 1.0L);
      if (r < 2*R && c < 2*C && is_circ[r/2][c/2] && (r+c)%2 == 1)
        f(sp[r+1][c+1], sp[r][c] + pi_over_2);
    }
  }

  printf("%.10lf", 10*static_cast<double>(sp[2*R][2*C] / 2.0L));
}
