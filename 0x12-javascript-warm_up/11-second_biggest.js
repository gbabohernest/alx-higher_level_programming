#!/usr/bin/node

const args = process.argv.slice(2);

function secondBiggest (arr) {
  const arrLen = arr.length;
  if (arrLen < 2) {
    return (0);
  }

  let maxVal;
  let secondMaxVal;
  if (arr[0] > arr[1]) {
    maxVal = arr[0];
    secondMaxVal = arr[1];
  } else {
    maxVal = arr[1];
    secondMaxVal = arr[0];
  }

  for (let i = 2; i < arrLen; i++) {
    if (arr[i] > maxVal) {
      secondMaxVal = maxVal;
      maxVal = arr[i];
    } else if (arr[i] > secondMaxVal && arr[i] !== maxVal) {
      secondMaxVal = arr[i];
    }
  }
  return (secondMaxVal);
}

console.log(secondBiggest(args));
