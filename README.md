# Password Cracker

This Python script is designed to crack hashed passwords using various hashing algorithms such as MD5, SHA-1, SHA-256, and SHA-512. It reads hashed passwords from a file (`passwords.txt`) and attempts to match them with a supplied hash value using the selected algorithm.

## Features

- Supports cracking passwords hashed with MD5, SHA-1, SHA-256, and SHA-512 algorithms.
- User-friendly interface for selecting the hash algorithm and providing the hash to crack.
- Outputs the cracked password if found in the wordlist; otherwise, indicates if the password cannot be cracked with the provided list.

## Usage

1. Clone the repository:
git clone https://github.com/saksham342/passwordCracker.git

2. Navigate to the repository directory:
cd password-cracker

3. Run the script:
python password_cracker.py

4. Follow the prompts to enter the hashed password and select the algorithm.

## Requirements

- Python 3.x
- hashlib module (built-in in Python)

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request.

## Disclaimer

This tool is intended for educational purposes and ethical hacking in controlled environments. Use responsibly and comply with applicable laws and regulations.
