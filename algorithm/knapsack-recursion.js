/*

Dynamic Programming --> AI, ML


*knapsack problem*

first element = value;
second element = weight;

input:

time - Recursion O(2^N); 


DP - O(N * M)(DP)
*/

function knapsack(items, cap) {
  if (!items.length) return [];

  const maxValue = [-Infinity, []]; // index

  /// weight <= cap
  // value > :)
  //val, weight
  recursionHelper(items, cap, maxValue, [0, 0, []], 0);

  console.log(maxValue);
}

const items = [
  [465, 100],
  [400, 85],
  [255, 55],
  [350, 45],
  [650, 130],
  [1000, 190],
  [455, 100],
  [100, 25],
  [1200, 190],
  [320, 65],
  [750, 100],
  [50, 45],
  [550, 65],
  [100, 50],
  [600, 70],
  [240, 40],
];

const cap = 200;
//[1500, [3, 12, 14]]
knapsack(items, cap);

function recursionHelper(items, cap, maxValue, currentStatus, curIdx) {
  // end clause

  // curIdx > items.length
  if (curIdx === items.length && cap >= currentStatus[1]) {
    if (maxValue[0] < currentStatus[0]) {
      maxValue[0] = currentStatus[0];
      maxValue[1] = currentStatus[2];
    }
    return;
  }

  if (curIdx >= items.length || currentStatus[1] > cap) return;

  const curVal = items[curIdx][0];
  const curWeight = items[curIdx][1];

  /// call recursion ---> selecting current item or not selecting current item
  /*
      maxValue = [6, [0, 2]]; 
      cap = 10
      currentStatus=[6,8,[0,2]]

                0       1     2      3
      items = [[1,2], [4,3], [5,6], [6,7]];
                  ^
      output: [10, [1,3]];
  */

  recursionHelper(
    items,
    cap,
    maxValue,
    [
      currentStatus[0] + curVal,
      currentStatus[1] + curWeight,
      [...currentStatus[2], curIdx],
    ],
    curIdx + 1
  ); /// choose
  recursionHelper(
    items,
    cap,
    maxValue,
    [currentStatus[0], currentStatus[1], [...currentStatus[2]]],
    curIdx + 1
  ); /// not choose
  return;
}