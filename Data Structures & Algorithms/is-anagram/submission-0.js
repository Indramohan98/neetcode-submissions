class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length) return false

        // let sortedS = s.split("").sort().join()
        // let sortedT = t.split("").sort().join()

        // return sortedS == sortedT

        let setS = {}
        let setT = {}

        for(let i=0; i<s.length; i++){
            setS[s[i]] = (setS[s[i]] || 0) + 1
            setT[t[i]] = (setT[t[i]] || 0) + 1
        }

        for(let key in setS){
            if(setS[key] != setT[key]){
                return false
            }
        }

        return true
    }
}
