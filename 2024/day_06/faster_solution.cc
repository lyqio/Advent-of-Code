#include <bits/stdc++.h>
using namespace std;

pair<int, int> switch_direction(pair<int, int> direction) { if (direction == make_pair(-1, 0)) {
    direction = make_pair(0, 1);
  }
  else if (direction == make_pair(0, 1)) {
    direction = make_pair(1, 0);
  }
  else if (direction == make_pair(1, 0)) {
    direction = make_pair(0, -1);
  }
  else {
    direction = make_pair(-1, 0);
  }

  return direction;
}

int part_1(vector<string> lns) {
  pair<int, int> direction = make_pair(-1, 0);
  pair<int, int> position;

  for (int i = 0; i < lns.size(); i++) {
    for (int q = 0; q < lns[0].size(); q++) {
      if (lns[i][q] == '^') {
        position = make_pair(i, q);
      }
    }
  }

  bool has_moved = false;
  set<tuple<int, int, pair<int, int>>> turning_points;
  set<tuple<int, int>> known_coords;

  while (position.first >= 0 && position.first < lns.size() && position.second >= 0 && position.second < lns.size()) {
    if (!(lns[position.first][position.second] == '#')) {
      has_moved = true;
      known_coords.emplace(make_tuple(position.first, position.second));
      position.first += direction.first;
      position.second += direction.second;
    }
    else {
      if (find(turning_points.begin(), turning_points.end(), make_tuple(position.first, position.second, direction)) != turning_points.end()) {
        return -1;
      }

      has_moved = false;
      turning_points.emplace(make_tuple(position.first, position.second, direction));
      position.first -= direction.first;
      position.second -= direction.second;
      direction = switch_direction(direction);
    }
  }

  return known_coords.size();
}

int run_row(vector<string> lns, int i) {
    if (i >= lns.size()) {
      return 0;
    }

    int cnt = 0;
    for (int q = 0; q < lns.size(); q++) {
      if (lns[i][q] == '.') {
        lns[i][q] = '#';
        if (part_1(lns) == -1) {
          cnt += 1;
        }

        lns[i][q] = '.';
      }
    }

    return cnt;
}

int part_2(vector<string> lns) {
  int cnt = 0;
  
  for (int i = 0; i < lns.size(); i++) {
    vector<future<int>> vec;
    for (int c = 0; c < thread::hardware_concurrency(); c++) {
      future<int> t1 = async(&run_row, lns, i);
      vec.push_back(move(t1));
      i++;
    }
  
    for (int r = 0; r < vec.size(); r++) {
      cnt += vec[r].get();
    }
  }

  return cnt;
}

int main() {
  vector<string> lns;
  string line;
  while (getline(cin, line)) {
    lns.push_back(line);
  }

  cout << part_2(lns) << '\n';
}
