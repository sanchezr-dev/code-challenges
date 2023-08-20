/**
 * Code challenge: POSTFIX Calculator
 *
 * e.g.
 * >> assert solution ("8 2 *") == 8 * 2
 */

function calculatePostfix(postfixExpression) {
  const splittedExpression = postfixExpression.split(" ");
  const stack = [];

  splittedExpression.forEach((value) => {
    if (!isNaN(value)) {
      stack.push(value);
    } else {
      const operator = value;
      const rightOperand = stack.pop();
      const leftOperand = stack.pop();
      const expression = `(${leftOperand} ${operator} ${rightOperand})`;
      stack.push(expression);
    }
  });

  const evalExpression = stack.pop();
  console.log(evalExpression);
  return eval(evalExpression);
}

function main() {
  let postfixExpression = "8 2 *";
  let result = calculatePostfix(postfixExpression);
  console.log(`Expression: ${postfixExpression} | Result: ${result}`);

  postfixExpression = "7 2 - 2 *";
  result = calculatePostfix(postfixExpression);
  console.log(`Expression: ${postfixExpression} | Result: ${result}`);

  postfixExpression = "35 7 / 5 -";
  result = calculatePostfix(postfixExpression);
  console.log(`Expression: ${postfixExpression} | Result: ${result}`);

  postfixExpression = "3 2 8 + 9 - *";
  result = calculatePostfix(postfixExpression);
  console.log(`Expression: ${postfixExpression} | Result: ${result}`);
}

main();
