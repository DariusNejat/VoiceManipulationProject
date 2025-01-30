# Voice Manipulation Project
its project for computiantonal linguestic class that help me manipulate voice.

## Overview
This project explores voice manipulation techniques, inspired by our university learnings from Praat. The primary goal is to manipulate audio files (e.g., reverse segments, change pitch, and alter voice parameters) to determine how much we can change a voice while keeping it recognizable to humans.

[voice picture goes here]

---

## Features
- **Voice Segmentation**: Split audio files into segments for processing.
- **Reverse Segments**: Reverse specific parts of audio files.
- **Silent Segments**: Silent specific parts of audio files.
- **Pitch Manipulation**: Adjust the pitch of voices. (for future developement)
- **Additional Voice Alterations**: Apply other voice parameter modifications. (future developement)
- **Voice Concatanation**: Merge audio files segement into 1 single audio.

---

## Installation
### **Project Structure**
- `data/`: Contains audio files in formats like `.mp3` and `.wav`.
- `libraries/`: Each classmate contributes a library for a specific manipulation (e.g., segmentation, reversing, pitch).
- `README.md`: This guide.
- `requirements.txt`: (Will be added as dependencies are determined.)

### **Steps**
1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/VoiceManipulationProject.git
   cd VoiceManipulationProject
   ```

2. Install Python (version 3.10 or higher recommended):
   - [Download Python](https://www.python.org/downloads/) if it is not already installed.

3. Install Required Dependencies:
   - For now, install basic dependencies:
     ```bash
     pip install numpy librosa soundfile
     ```
   - Additional dependencies will be added to `requirements.txt` as the project progresses.

---

## Usage
### **Beta Version (Terminal Commands)**
Run the script from the terminal:
```bash
python main.py --file data/sample.wav --action reverse --segment 0-10
```

[voice manipulation result goes here]

### **Future Plans**
- Develop a **React-based web interface**.
- Create a standalone executable (.exe) for ease of use.

---

## Development Guide
### **Coding Standards**
- **Function-Based Programming**:
  - Each classmate is responsible for creating a separate library for specific manipulations:
    - Example:
      - `libraries/segmentation.py`: Handles voice segmentation.
      - `libraries/reverser.py`: Reverses segments.
      - `libraries/pitch.py`: Adjusts pitch.
  - Combine all libraries using a central `__init__.py`.
  - keep in mind the data structure you want to pass to each function in the flow,be it all voice or array of segments, or single segment and do loop over it is all upto your decision.
  - you can even merge all functions in 1 library or have multi libraries and pipeline as our suggestion.

### **Workflow**
1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/VoiceManipulationProject.git
   ```
2. Create Your Branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit Changes:
   ```bash
   git add .
   git commit -m "Description of what you did"
   git push origin feature-name
   ```
4. Submit a Pull Request (PR): Request to merge your changes into the main branch.

---

## Examples
### Input Audio
- A simple `.wav` file of someone saying "hello."

### Manipulated Audio
- The word "hello" reversed into "olleh."

[example waveform image or audio manipulation showcase goes here]

---

## Contributing
### Contribution Workflow
1. **Branch Naming**:
   - Use `feature-[name]` for new features.
   - Use `bugfix-[name]` for fixing issues.

2. **Pull Requests**:
   - Each feature should be tested before merging.
   - Use GitHub Issues to report bugs or request features.

---

## License
This project is licensed under the **Apache License 2.0**.  
All credits must go to:
- **Project Team**:
  - [Mohammad Hossein (darius) Bayat](https://www.linkedin.com/in/mohammad-hosein-bayat/)
  - [Shahrzad Ziaei]
  - Name3
  - Name4
  - Name5
  - Name6
  - Name7

### **Apache License 2.0**
You are free to use, modify, and distribute this project, but you must credit the original authors.  
For the full license text, see the [LICENSE](./LICENSE) file.

---

## Contact Information
- **Project Lead**: [My LinkedIn Profile](https://www.linkedin.com/in/mohammad-hosein-bayat/)

---
