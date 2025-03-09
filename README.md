# Projector Light Show

This guide will help you set up the Projector Light Show project on a Windows machine. Follow the steps below to install the necessary libraries and tools.

## Prerequisites

- Windows 10 or later
- Python 3.6 or later

## Installation Steps

1. **Install Visual Studio 2022 Community Edition**

    Open a command prompt and run the following command to install Visual Studio 2022 Community Edition with the required components:

    ```sh
    winget install Microsoft.VisualStudio.2022.Community --silent --override "--wait --quiet --add ProductLang En-us --add Microsoft.VisualStudio.Workload.NativeDesktop --includeRecommended"
    ```

2. **Clone the Repository**

    Clone the project repository to your local machine:

    ```sh
    git clone https://github.com/yourusername/projector-light-show.git
    cd projector-light-show
    ```

3. **Create a Virtual Environment**

    Create and activate a virtual environment:

    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    ```

4. **Install Python Libraries**

    Install the required Python libraries declared in the `requirements.txt` file:

    ```sh
    pip install -r requirements.txt
    ```

    If there are additional Python files with library declarations, install them as well:

    ```sh
    pip install -r additional_requirements.txt
    ```

5. **Run the Project**

    After installing all the dependencies, you can run the project:

    ```sh
    python main.py
    ```

## Troubleshooting

- Ensure that all dependencies are correctly installed.
- Check for any missing libraries and install them using `pip`.

For further assistance, refer to the project's documentation or contact the project maintainers.
