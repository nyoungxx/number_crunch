import os

def process_file(file_name):
    total_sum = 0
    count = 0
    min_value = float('inf')
    max_value = float('-inf')
    error_log = []
    
    try:
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total_sum += number
                    count += 1
                    min_value = min(min_value, number)
                    max_value = max(max_value, number)
                except ValueError:
                    error_log.append(f"Invalid entry skipped: {line.strip()}")
                    
        if count == 0:
            raise ValueError("No valid numbers found in the file.")
        
        average = total_sum / count
        
        with open("report.txt", 'w') as report:
            report.write("Report:\n")
            report.write("-------\n")
            report.write(f"Count: {count}\n")
            report.write(f"Sum: {total_sum}\n")
            report.write(f"Average: {average}\n")
            report.write(f"Minimum: {min_value}\n")
            report.write(f"Maximum: {max_value}\n")
        
        if error_log:
            with open("error_log.txt", 'w') as log:
                log.write("Errors encountered:\n")
                log.write("------------------\n")
                for error in error_log:
                    log.write(error + "\n")
        
    except FileNotFoundError:
        print("Error: File not found. Please check the file name and try again.")
        return False
    except ValueError as e:
        print(f"Error: {e}")
        return False
    finally:
        print("Processing complete. Check 'report.txt' for results.")
        if error_log:
            print("Some errors were encountered. Check 'error_log.txt'.")
    
    return True

if __name__ == "__main__":
    while True:
        file_name = input("Enter the name of the file containing numbers: ")
        if process_file(file_name):
            break
        retry = input("Would you like to try again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Exiting program.")
            break
