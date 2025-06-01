import java.util.*;

class Solution {
    public List<Integer> findPeaks(int[] mountain) {
        List<Integer> res = new ArrayList<>();
        for(int i = 1; i<  mountain.length - 1; i++){
            if(mountain[i-1] < mountain[i] && mountain[i] > mountain[i+1])
                res.add(i); 
        }

        return res;
        
    }
    public static void main(String[] args) {
        int[] mountain = {1, 3, 2, 4, 1, 0, 5, 3};
        Solution sol = new Solution();
        List<Integer> peaks = sol.findPeaks(mountain);
        System.out.println("Peak indices: " + peaks);
    }
}
