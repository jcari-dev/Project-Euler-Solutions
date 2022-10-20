let array = [...Array(21).keys()];
array.shift();

let y = 1;
let divided = false;
let divide;

while (divided === false) {
  divide = array.map((x) => y % x === 0);

  if (!divide.includes(false)) {
    console.log(y);
    divided = true;
  } else {
    y++;
  }
}
