class Solution {
public:
    // TC: O(NLOGN) SC: O(N)
    long long countOfSubstrings(string word, int k) {
        int n = word.size();
        unordered_map<char, vector<long long>> prefix_vowels;
        vector<long long> prefix_consonants(n + 1, 0);
        vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        long long ans = 0;

        for (char vowel : vowels) {
            prefix_vowels[vowel] = vector<long long>(n + 1, 0);
        }

        for (int i = 0; i < n; ++i) {
            char c = word[i];
            if (find(vowels.begin(), vowels.end(), c) != vowels.end()) {
                for (char vowel : vowels) {
                    if (c == vowel) {
                        prefix_vowels[c][i + 1] = prefix_vowels[c][i] + 1;
                    } else {
                        prefix_vowels[vowel][i + 1] = prefix_vowels[vowel][i];
                    }
                }
                prefix_consonants[i + 1] = prefix_consonants[i];
            } else {
                for (char vowel : vowels) {
                    prefix_vowels[vowel][i + 1] = prefix_vowels[vowel][i];
                }
                prefix_consonants[i + 1] = prefix_consonants[i] + 1;
            }
        }

        for (int i = 0; i < n; ++i) {
            int r_vowels = -1;
            int r_consonants_1 = upper_bound(prefix_consonants.begin() + i, prefix_consonants.end(), prefix_consonants[i] + k) - prefix_consonants.begin();
            int r_consonants_2 = lower_bound(prefix_consonants.begin() + i, prefix_consonants.end(), prefix_consonants[i] + k) - prefix_consonants.begin();
            
            for (char vowel : vowels) {
                r_vowels = max(r_vowels, (int)(lower_bound(prefix_vowels[vowel].begin() + i, prefix_vowels[vowel].end(), prefix_vowels[vowel][i] + 1) - prefix_vowels[vowel].begin()));
            }
            
            if (r_vowels < r_consonants_1) {
                ans += r_consonants_1 - max(r_vowels, r_consonants_2);
            }
        }
        
        return ans;
    }
};
