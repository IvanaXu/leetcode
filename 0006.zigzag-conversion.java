class Solution {
    public String convert(String s, int numRows) {
        if ("".equals(s) || numRows <= 1) {
            return s;
        }
        char ca[] = s.toCharArray();
        char result[] = new char[ca.length];
        int resIndex = 0;
         // 每行下标间隔
        int inc = 2 * (numRows -1);
        int index ;
        int n = numRows -1;
        for (int i=0;i<numRows && i < ca.length;i++) {
            index = i;
            // 首行和最后一行两列之间没有中间元素
            if(i % n == 0) {
                while (index < ca.length) {
                    result[resIndex++] = ca[index];
                    index +=inc;
                }
            } else {
                // 直接输入每行第一个元素
                result[resIndex++] = ca[index];
                while (index < ca.length) {
                    // 获取右列下标索引
                    int right = index + inc;
                    // 两列中间元素下标为右边列 - (行号*2)
                    int left = right - 2 * i;
                    if (left < ca.length) {
                        result[resIndex++] = ca[left];
                    }
                    if (right < ca.length) {
                        result[resIndex++] = ca[right];
                    }
                    index = right;
                }
            }
        }
        return String.valueOf(result);
    }
}
