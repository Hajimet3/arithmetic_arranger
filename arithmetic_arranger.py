def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    first_operands = []
    second_operands = []
    operators = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must contain two operands and an operator."

        operand1, operator, operand2 = parts
     
        #Check for valid operator
        if operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        #Check if operand is not digit
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'
        #Check no more than 4 digits
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        first_operands.append(operand1)
        second_operands.append(operand2)
        operators.append(operator)

        #Calculate Result

        if operator == '+':
            result = str(int(operand1) + int(operand2))
        elif operator == '-':
            result = str(int(operand1) - int(operand2))
        results.append(result)

        #Setting up format
        line1 = ""
        line2 = ""
        line3 = ""
        line4 = ""

    #Loop for the result
    for i in range(len(problems)):
        operand1 = first_operands[i]
        operator = operators[i]
        operand2 = second_operands[i]
        result = results[i]

        width = max(len(operand1), len(operand2)) + 2

        line1 += operand1.rjust(width) + "    "
        line2 += operator + " " + operand2.rjust(width - 2) + "    "
        line3 += "-" * width + "    "
        if show_answers:
            line4 += result.rjust(width) + "    "
    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    if show_answers:
        arranged_problems += "\n" + line4.rstrip()
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))