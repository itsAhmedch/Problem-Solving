function countRepeats(str) {
    let r = 0;
    for (let i = 1; i < str.length; i++)  (str[i] === str[i - 1]) ?r++:0
    return r;
}
