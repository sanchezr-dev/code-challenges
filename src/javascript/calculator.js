/**
 * Code challenge: Create a calculator function
 *
 * Write a function that accepts three parameters.
 * The first parameter is an integer.
 * The second is one of the following mathematical operators: +, -, /, or *.
 * The third parameter will also be an integer.
 *
 * The function should perform a calculation and return the results.
 * For example, if the function is passed 6 and 4, it should return 24.
 */

function calculate(operandA, operator, operandB) {
  const expression = `${operandA} ${operator} ${operandB}`;
  return eval(expression);
}

function main() {
  let operandA = 6;
  let operandB = 4;
  let operator = "*";
  let result = calculate(operandA, operator, operandB);
  console.log(`${operandA} ${operator} ${operandB} = ${result}`);

  operandA = 3;
  operandB = 5;
  operator = "-";
  result = calculate(operandA, operator, operandB);
  console.log(`${operandA} ${operator} ${operandB} = ${result}`);
}

main();
