#!/usr/bin/node

const args = process.argv.slice(2);

function secondBiggest (arr) {
  const arrLen = arr.length;
  if (arrLen < 2) {
    return (0);
  }

  let maxVal;
  let secondMaxVal;
  if (parseInt(arr[0]) > parseInt(arr[1])) {
    maxVal = arr[0];
    secondMaxVal = arr[1];
  } else {
    maxVal = arr[1];
    secondMaxVal = arr[0];
  }

  for (let i = 2; i < arrLen; i++) {
    if (parseInt(arr[i]) > parseInt(maxVal)) {
      secondMaxVal = maxVal;
      maxVal = arr[i];
    } else if (parseInt(arr[i]) > parseInt(secondMaxVal) && parseInt(arr[i]) !== parseInt(maxVal)) {
      secondMaxVal = arr[i];
    }
  }
  return (parseInt(secondMaxVal));
}

console.log(secondBiggest(args));
