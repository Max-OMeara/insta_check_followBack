# Instagram Not Following Back Checker

## Project Overview

The Instagram Not Following Back Checker is a Python application designed to help users identify which Instagram accounts they are following that are not following them back. This tool processes JSON files downloaded from Meta (Instagram) and runs locally, ensuring your account's security by avoiding the need to share your username or password.

## Purpose

This project was created to provide a secure method for checking follow-back status without exposing personal credentials. It avoids the risks associated with using third-party services and helps users manage their Instagram connections more effectively.

## Features

- **Local Processing:** Analyzes Instagram follow and follower data locally without requiring credentials.
- **User Identification:** Identifies users you are following who do not follow you back.
- **Simple Output:** Displays the list of non-reciprocal followers and their total count.

## Technologies Used

- **Python:** The core programming language used to develop the application.
- **JSON:** Data format used for storing and processing Instagram follow and follower information.
- **os and json:** Standard Python libraries used for file handling and parsing JSON data.

## File Structure

- `follow_check.py`: The main script containing the logic to process JSON files and identify non-reciprocal followers.
- `following.json`: JSON file containing data on users you are following.
- `followers.json`: JSON file containing data on users who follow you.

## Installation

To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/instagram-follow-checker.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd instagram-follow-checker
   ```

3. **Install dependencies:**
   Ensure you have Python installed. This project does not require additional Python libraries beyond the standard library.

4. **Download JSON Files from Meta:**
   Follow these instructions to download your data (This may take a day or two to send depending on the file size):
   Source: https://help.instagram.com/181231772500920
   - Go to your instagram profile page.
   - Click the 3 bars at the top right.
   - Click `Accounts Center`.
   - Click `Your information and permissions`.
   - Click `Download your information` > `Download or transfer information`.
   - Click `Some of your information`.
   - Scroll until you find `Followers and following`, select it and click `Next`.
   - Choose your preference of getting the information.
   - Select the profile and date range (choose `All time`).
   - MAKE SURE FILES ARE IN `JSON` FORMAT.
   - `Media Quality` does not matter in our case so any will suffice.
   - Click `Create files`.
   - You will be alerted on how long it will take for the files to be sent.
     
   If you choose `Download to device`
   - Once you recieve the email, click the link.
   - The data is stored in `Accounts Center` which can be accessed by using the previous steps but click `Download` instead of `Download or transfer information`.
   - Save the downloaded files to the same directory as your script and extract them from the zip file.

   If you choose `Transfer to destination`
   - Once you recieve the email, the files should have been sent to the destination.

6. **Run the application:**
   ```bash
   python follow_check.py
   ```

## How to Use

1. **Ensure JSON Files Are in Place:**
   Confirm that `following.json` and `followers.json` are in the `connections/follower_and_following/` directory.

2. **Execute the Script:**
   Run the script to analyze your follow and follower data.

3. **Review Results:**
   The script will output the list of users you follow who do not follow you back, along with the total count.

## Possible Future Plans
  - Enhanced Data Visualization: Add graphical representations of follow-back statistics.
  - Additional Metrics: Include metrics such as engagement rates or mutual followers.
  - User Interface: Develop a GUI for easier interaction and data management.

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

## Acknowledgments

This project was created to practice Python programming and to securely manage Instagram follow data. It provides a valuable tool for users seeking to maintain their Instagram connections without compromising their account security.

---

Feel free to adjust the content as needed and replace placeholders with your actual repository URL and any additional details specific to your project.
