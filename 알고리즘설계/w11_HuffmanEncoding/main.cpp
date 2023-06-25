#include <iostream>
#include <map>
#include <algorithm>
#include <cstring>
#include <queue>

using namespace std;

struct nodetype {
	char symbols;
	int frequency;
	nodetype* left;
	nodetype* right;
};

void generateHuffmanCodes(nodetype* root, string code, map<char, string>& codes) {
	if (!root) return;
	if (root->symbols) codes[root->symbols] = code;
	generateHuffmanCodes(root->left, code + "0", codes);
	generateHuffmanCodes(root->right, code + "1", codes);
}

struct comp{
	bool operator()(const nodetype* l, const nodetype* r) const {
		return l->frequency > r->frequency;
	}
};

void buildHuffmanTree(string s) {
	int i = 0;
	priority_queue<nodetype*, vector<nodetype*>, comp> PQ;
	nodetype* r;
	
	map<char, int> freq;
	for (char c : s) {
		freq[c]++;
	}

	for (auto& pair : freq) {
		r = new nodetype { pair.first, pair.second };
		PQ.push(r);
	}

	int n = PQ.size();

	for (i = 1; i < n; i++) {
		nodetype* p = PQ.top();
		PQ.pop();
		nodetype* q = PQ.top();
		PQ.pop();
		r = new nodetype;
		r->symbols = '\0';
		r->left = p;
		r->right = q;
		r->frequency = p->frequency + q->frequency;
		PQ.push(r);
	}

	nodetype* root = PQ.top();

	map<char, string> huffmanCode;
	generateHuffmanCodes(root, "", huffmanCode);

	cout << "Huffman code table:" << endl;
	for (auto pair : huffmanCode) {
		cout << pair.first << ":" << pair.second << endl;
	}

	string encode;
	for (char bi : s) {
		encode += huffmanCode[bi];
	}

	cout << "Input string: " << s << endl;
	cout << "Encoded string: " << encode << endl;

}

int main() {
	string s = "this is a test string";
	buildHuffmanTree(s);
}