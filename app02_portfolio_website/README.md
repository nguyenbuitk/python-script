# Portfolio Website

This is a personal portfolio website built with Streamlit, displaying a biography, photo, and a list of Python projects. Each project includes a title, description, image, and a link to the source code. 

## Features

- **Biography and Photo**: Displays a personal biography and photo.
- **Project Portfolio**: Showcases various Python projects with descriptions, images, and links.
- **Contact Feature**: Uses `sendmail.py` to send emails directly from the app.

## Project Structure

- **main.py**: The primary Streamlit app that displays the portfolio website.
- **Contact_Us.py**: Handles the contact form functionality.
- **sendmail.py**: Contains the function for sending emails.
- **test.py**: Used for testing various components in the app.

## Setup Instructions

### Prerequisites

- **Python 3.x**
- **Streamlit**: Install Streamlit using the following command:
  ```bash
  pip install streamlit
  ```
- **Pandas**: Required for reading and displaying project data.
  ```bash
  pip install pandas
  ```

### Getting Started

1. **Clone the repository** (if applicable) or place the files in a project directory.
2. **Ensure required images and `data.csv` are present** in their respective directories:
   - Place project images in an `images` folder within the project directory.
   - Ensure `data.csv` is in the project directory and contains project details, including `title`, `description`, `image`, and `url` columns.

3. **Set Up Email Configuration** (Optional):
   - The `sendmail.py` script uses Gmail SMTP for sending emails. Update `username` and `password` with your credentials to use this feature. 

### Running the Application

To start the portfolio website, use the following command:

```bash
streamlit run main.py
```

This will launch the Streamlit app, which you can view in your browser at `http://localhost:8501`.

### Example Usage

- The application will display the biography and image in one section.
- Below, projects are presented in two columns, each showing a title, description, image, and link.
- The contact form allows users to send messages directly to the configured email address.

## Security Note

**Important**: Avoid storing sensitive information, like email credentials, directly in the code. Consider using environment variables for these values.

