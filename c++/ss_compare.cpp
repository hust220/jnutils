/**
 * @file ss_compare.cpp
 * @brief Compare two RNA secondary structures
 * @author wj_hust08@163.com
 * @version 1.0
 * @date 2015-5-22
*/

#include <iostream>
#include <cstring>
#include <map>
#include <algorithm>
#include <iterator>
using namespace std;

map<int, int> get_pairs(string ss) {
	vector<int> parentheses;
	vector<int> brackets;
	map<int, int> pairs;
	for (int i = 0; i < ss.size(); i++) {
		if (ss[i] == '(') {
			parentheses.push_back(i);
		} else if (ss[i] == '[') {
			brackets.push_back(i);
		} else if (ss[i] == ')') {
			pairs[parentheses.back()] = i;
			parentheses.pop_back();
		} else if (ss[i] == ']') {
			pairs[brackets.back()] = i;
			brackets.pop_back();
		}
	}
	return pairs;
}

int main(int argc, char **argv) {
	map<int, int> pairs1 = get_pairs(argv[1]);
	map<int, int> pairs2 = get_pairs(argv[2]);
	int tp = count_if(begin(pairs1), end(pairs1), [&pairs2](const pair<int, int> &pair1) {
		return any_of(begin(pairs2), end(pairs2), [&pair1](const pair<int, int> &pair2) {
			return pair1.first == pair2.first && pair1.second == pair2.second;
		});
	});
	int fn = count_if(begin(pairs1), end(pairs1), [&pairs2](const pair<int, int> &pair1) {
		return none_of(begin(pairs2), end(pairs2), [&pair1](const pair<int, int> &pair2) {
			return pair1.first == pair2.first && pair1.second == pair2.second;
		});
	});
	int fp = count_if(begin(pairs2), end(pairs2), [&pairs1](const pair<int, int> &pair2) {
		return none_of(begin(pairs1), end(pairs1), [&pair2](const pair<int, int> &pair1) {
			return pair1.first == pair2.first && pair1.second == pair2.second;
		});
	});
	cout << "TP: " << tp << endl;
	cout << "FP: " << fp << endl;
	cout << "FN: " << fn << endl;
}




