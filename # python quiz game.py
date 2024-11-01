# python quiz gameA

questions = (
    "What is an Accumulator (ACC)?",
    "What is an address bus?",
    "What is the Arithmetic Logic Unit (ALU)?",
    "What are Buses?",
    "What is Cache?"
)

options = (
    ("A. A special register to temporarily store the results of operations performed by the ALU.",
     "B. Carries the memory location address of the register the data is being carried to or from.",
     "C. A part of the CPU that performs arithmetic calculations and logical operations on data for the computer programs",
     "D. A physical set of parallel wires connecting and carrying groups of bits between several components of a computer.",
     "E. A small and fast but expensive memory in the CPU used to store instructions and data that are accessed regularly."),
     
    ("A. A small memory register.",
     "B. Carries the memory location address of the register.",
     "C. Performs arithmetic calculations and logical operations.",
     "D. Parallel wires connecting components.",
     "E. Fast memory storing instructions and data."),
     
    ("A. Temporarily stores ALU results.",
     "B. Address bus for carrying data.",
     "C. The CPU component performing calculations.",
     "D. Wires connecting computer components.",
     "E. CPU memory storing frequently accessed data."),
    
    ("A. Stores temporary results.",
     "B. Carries memory location addresses.",
     "C. Performs arithmetic and logic operations.",
     "D. Wires connecting components in a computer.",
     "E. Cache memory for frequently used instructions."),
    
    ("A. A temporary storage register.",
     "B. Carries address of data transfer.",
     "C. CPU performs calculations here.",
     "D. Physical wires carrying data.",
     "E. Fast storage for frequently accessed data."),
)

answers = ("A", "B", "C", "D", "E")  # Correct answers for each question
guesses = []
score = 0
question_num = 0

# Loop through each question
for question in questions:
    print(f"\nQuestion {question_num + 1}: {question}")
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter your answer (A, B, C, D, E): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print(f"The correct answer was: {answers[question_num]}")
    
    question_num += 1

# Display final score
print("\nQuiz completed!")
print(f"Your score is {score} out of {len(questions)}.")
