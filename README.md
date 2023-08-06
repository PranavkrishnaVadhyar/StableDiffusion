# Stable diffusion model

This script demonstrates the integration of the Banana Dev API with Firebase for image generation based on input prompts.

## Description

This script utilizes the Banana Dev API to generate images based on input prompts. It also uses Firebase to fetch the input prompt from the database.

## Prerequisites

Before running the script, ensure you have the following:

- `banana_dev` library
- `base64` library
- `PIL` (Python Imaging Library)
- `firebase_admin` library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YourUsername/YourRepository.git
   cd YourRepository
   ```

2. Install the required Python packages:

   ```bash
   pip install banana_dev pillow firebase_admin
   ```

3. Add your Firebase service account key JSON file to the project root and update the `cred` object in `database.py` with the correct path.

4. Update the `databaseURL` in the `firebase_admin.initialize_app` function in `database.py` with your Firebase database URL.

5. Obtain your Banana Dev API key (`api_key`) and model key (`model_key`) and update them in your main script.

## Usage

1. Run the main script `run.py`:

   ```bash
   python run.py
   ```

2. The script will fetch the input prompt from the Firebase database using the `database` module.

3. It will then call the Banana Dev API to generate an image based on the prompt and provided parameters.

4. The generated image will be saved as `output.jpg` in the current directory.

## Configuration

Adjust the `model_inputs` dictionary in the main script to customize the image generation parameters such as `num_inference_steps`, `guidance_scale`, `height`, `width`, and `seed`.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

This integration script was developed by [Your Name](https://github.com/PranavkrishnaVadhyar).


```
