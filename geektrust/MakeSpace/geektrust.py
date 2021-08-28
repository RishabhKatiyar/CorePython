from src.Validators.InputValidator import InputValidator
from src.Service.MakeSpaceService import MakeSpaceService
import sys 


def main():
    input_file = sys.argv[1]
    file = open(input_file, 'r')
    lines = file.readlines()
    
    makeSpaceService = MakeSpaceService()
    
    try:
        for line in lines:
            # Validate the incoming request
            _input = InputValidator(line)

            if _input.IsValid:
                response = makeSpaceService.ExecuteRequest(_input.Query)
                print(response)
            else:
                print("INCORRECT_INPUT")
        
    except Exception:
        pass


if __name__ == "__main__":
    main()
    
