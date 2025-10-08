class Solution {
  public:
    bool isSorted(vector<int>& arr) {
        int n = arr.size();
        for (int i = 0; i < n; i++){
            for (int j = i + 1; j < n - 1 ; j++){
                if (arr[i] > arr[j]){
                    return false;
                }
            }
        }
        return true;
        
    }
};