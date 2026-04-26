class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let res = {}

        // for(let key of strs){
        //     const sorted = key.split("").sort().join();

        //     if(!res[sorted]){
        //         res[sorted] = []
        //     }
        //     res[sorted].push(key)
        // }

        // return Object.values(res)

        //2.Optimal sol

        for(let str of strs){
            let count = new Array(26).fill(0);

            for(let char of str){
                count[char.charCodeAt(0)-'a'.charCodeAt(0)]+=1
            }

            let key = count.join(',')

            if(!res[key]){
                res[key] = [] 
            }

            res[key].push(str)
        }

        return Object.values(res)
    }
}
