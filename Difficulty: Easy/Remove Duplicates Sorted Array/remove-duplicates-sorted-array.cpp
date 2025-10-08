class Solution {
  public:
    // Function to remove duplicates from the given array.
    vector<int> removeDuplicates(vector<int> &arr) {
        int n = arr.size();
        if (n <= 1){
            return arr;
        }
        int idx = 1; 
        
        for (int i = 1; i < n; i++){
            if (arr[i] != arr[i - 1]){
                arr[idx++] = arr[i];
            }
        }
        arr.resize(idx);
        return arr;
    }
};