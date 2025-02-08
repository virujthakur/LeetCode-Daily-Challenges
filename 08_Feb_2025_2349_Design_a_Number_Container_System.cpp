class NumberContainers {
public:
    unordered_map<int,int> IndexToNumber;
    unordered_map<int, set<int>> NumberToIndices;
    NumberContainers() {
        
    }
    
    // TC: O(LOGN) SC: O(N)
    void change(int index, int number) {
        if (IndexToNumber[index]!= 0)
        {
            int oldNumber = IndexToNumber[index];
            NumberToIndices[oldNumber].erase(index);
        }

        NumberToIndices[number].insert(index);
        IndexToNumber[index] = number;
    }
    
    //TC: O(1) SC: O(N)
    int find(int number) {
        if(NumberToIndices[number].size() > 0)
        {
            return *NumberToIndices[number].begin();
        }
        else
        {
            return -1;
        }
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
