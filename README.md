# Python Back-end Service for Whisper Transcription

This Python back-end service is developed to provide an efficient and scalable solution for audio transcription using the Whisper API. The service is containerized using Docker, making it ready for deployment on Google Cloud Platform (GCP). It includes a credit system for usage management and is accessible via an API.

## Features

- **Whisper API Integration**: Transcribes audio files using the Whisper API.
- **Credit System**: Features a credit system where users can generate single-use authentication codes, valid for a predetermined amount of audio transcription time.
- **API Access**: Allows for creating, reading, updating, and deleting authentication states, credit information, and transcript triggers.
- **File Handling**: Accepts .mp3 files up to 1 hour in length and outputs transcription in .txt format.
- **Cloud Storage**: Stores transcription files with unique IDs in a cloud database.
- **Scalable and Reliable**: Designed to perform smoothly under varying loads.

## Installation

Clone the Repository:

```bash
git clone [Repository URL]
```

Build Docker Container:

```bash
docker build -t whisper-transcription-service .
```

Run the Container:

```bash
docker run -d -p [desired_port]:80 whisper-transcription-service
```

## Usage

### Generating Authentication Code

Run the script provided to generate an authentication code valid for 1 hour of audio transcription.

### Transcribing Audio

Send a POST request to the service with the .mp3 file and the authentication code.

### Retrieving Transcription

Access the stored transcription using the unique ID provided.

## Database Integration

The service uses PostgreSQL for storing transcription files and their respective unique IDs.

## Testing

The service includes a suite of tests to ensure functionality and performance. Run the tests with the following command:

```bash
python -m unittest test.py
```

## Documentation

Detailed documentation is provided for implementation and API usage.

## Contributing

Contributions to the project are welcome. Please refer to the contributing guidelines before making a pull request.

## License

The project is licensed under the MIT License. Please review the license for any restrictions.
