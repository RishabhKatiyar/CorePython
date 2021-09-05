import sys 
from src.Validators.InputValidator import InputValidator
from src.Services.Ally import Ally


def main():
    input_file = sys.argv[1]
    file = open(input_file, 'r')
    lines = file.readlines()
    result = []
    result_set = set()

    for line in lines:
        input = InputValidator(line)
        if input.IsValid:
            if Ally.IsAlly(kingdom = input.Kingdom):
                if not input.Kingdom.Name in result_set:
                    result_set.add(input.Kingdom.Name)
                    result.append(input.Kingdom.Name)
            
    if len(result) < 3:
        print("NONE")        
    else:
        print("SPACE", end = " ")
        for items in result:
            print(items, end = " ")


if __name__ == "__main__":
    main()
    
