# Shuddhify

**Shuddhify** is a web application designed to promote respectful and positive online communication by detecting offensive language in real-time. Built with a combination of natural language processing and machine learning techniques, Shuddhify uses a fine-tuned BERT (Bidirectional Encoder Representations from Transformers) model to identify offensive or inappropriate content in user messages.

## Key Features

1. **Real-Time Offensive Language Detection**:
   - Shuddhify monitors messages in real-time, processing each one for offensive content.
   - Messages identified as offensive trigger a series of responses to encourage the user to communicate respectfully.

2. **User Penalty System**:
   - **Warning**: On the first offense, the app issues a gentle warning, informing the user about the inappropriate language.
   - **Temporary Freeze**: If offensive language persists, Shuddhify temporarily restricts the user from using the app, issuing a 5-minute freeze period.
   - **Blocking**: On continued violation of respectful language standards, the app blocks the user from the chat, ensuring a respectful environment for all users.

3. **Admin-Free Data Handling**:
   - Shuddhify only logs information when offensive language is detected. For regular messages, no data is stored, ensuring privacy and efficiency.

4. **User-Friendly Interface**:
   - The application provides a clean, intuitive chat interface with responsive feedback, allowing users to easily understand and adjust their language if necessary.

5. **Integration and Accessibility**:
   - The application is developed using Flask, making it lightweight, flexible, and easy to deploy on a server. Shuddhify’s front end is built with HTML, CSS, and JavaScript, ensuring cross-device compatibility and responsiveness.

## Technical Overview

- **Machine Learning**: Shuddhify employs a BERT-based model fine-tuned for offensive language detection, trained on labeled datasets to ensure high accuracy.
- **Flask API**: The backend is powered by Flask, handling requests between the front end and the machine learning model.
- **Data Privacy**: Designed with privacy in mind, Shuddhify only stores information related to detected offensive language.
- **Penalty Management**: Tracks user offenses by IP address and applies incremental penalties based on usage patterns.

## Use Case

Shuddhify is ideal for chat applications, forums, and any digital space where respectful communication is crucial. By enforcing a respectful language policy and issuing real-time feedback, Shuddhify fosters a welcoming and positive environment, empowering users to engage responsibly online.

## Summary

In essence, Shuddhify is more than just a content filter—it’s a digital assistant that encourages and maintains civility in online interactions, creating a safer, more respectful digital space.

## Installation

To run Shuddhify locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/shuddhify.git
   cd shuddhify
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000` to see Shuddhify in action.

## Contributing

Contributions are welcome! If you'd like to help improve Shuddhify, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

### Notes:
- Make sure to replace `https://github.com/your-username/shuddhify.git` with the actual URL of your GitHub repository.
- Adjust the installation instructions as needed based on your project's specific setup or requirements.
- You can add sections for **FAQs**, **Troubleshooting**, or any other relevant information depending on your audience.

Feel free to modify the content as per your project’s specifics! Let me know if you need further assistance.
