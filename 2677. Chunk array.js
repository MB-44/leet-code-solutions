var chunk = function(arr, size) {
    if (size == 1){
        return arr.map(num => [num]); 
    }

    const len = arr.length;
    let chunkedArr = [];
    let left = 0;

    for (let i=size; i < (len + size); i+=size){
        let chunk = arr.slice(left, i);
        chunkedArr.push(chunk);
        left = i
    }
    return chunkedArr;

};


const arr = [1,2,3];
let func = chunk(arr,1);
console.log(func)