int* twoSum(int* nums, int numssize, int target, int* returnsize) {
    for (int i = 0; i < numssize; i++) {
        for (int j = i + 1; j < numssize; j++) {
            if (nums[j] == target - nums[i]) {
                int* result = malloc(sizeof(int) * 2);
                result[0] = i;
                result[1] = j;
                *returnsize = 2;
                return result;
            }
        }
    }
    *returnsize = 0;
    return malloc(sizeof(int) * 0);
}