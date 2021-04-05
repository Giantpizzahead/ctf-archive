#include <iostream>
#include <string>
using namespace std;

int main(int argc, const char* argv[]) {
	if (argc != 2) {
		cout << "Usage: do stuff" << endl;
		return 1;
	} else {
		string pass = argv[1];
		string possible = "picoCTF{AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH}";
		if (pass.size() != possible.size()) {
			cout << "Invalid length" << endl;
			return 1;
		}
		int sum1 = 0, sum2 = 0;
		for (int i = 0; i < pass.size(); i++) {
			sum1 += pass[i] * (i+1);
		}
		for (int i = 0; i < possible.size(); i++) {
			sum2 += possible[i] * (i+1);
		}
		if (sum1 != sum2) {
			cout << "Invalid password" << endl;
			return 1;
		} else {
			cout << "Success" << endl;
			return 0;
		}
	}
}