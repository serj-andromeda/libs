/**
Check whether x is in range [a; b] both limits inclusive. a could be null. In this case checking only if x is less or equals b
*/
function between (x, a, b) {
  if (a===null) {
    return x<=b;
  } else {
    return a<=x && x<=b;
  }
}

