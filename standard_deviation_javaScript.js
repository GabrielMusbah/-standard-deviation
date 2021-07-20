function standardDeviation (list){

    let listSplit = list.split(" ");

    let listInt = listSplit.map(Number);

    let average = listInt.reduce((sum, value) => sum += value, 0) / listInt.length;

    let listMinusAverage = listInt.map(num => {
        return num - average;
    });

    let listSquared = listMinusAverage.map(num => {
        return num ** 2;
    });

    let sumList = listSquared.reduce((sum, value) => sum += value, 0);

    let sumListDividedRageList = sumList / (listInt.length - 1);

    let standardDeviation = Math.sqrt(sumListDividedRageList);

    return standardDeviation
}


let list = "1 2 3 4 5 6 7 8 9 10";

let result = standardDeviation(list)

console.log(result.toFixed(4))
