# Gesture-Based Rock-Paper-Scissors Game

Experience the classic game of Rock-Paper-Scissors reimagined with real-time hand gesture recognition, AI logic, dynamic visuals, and audio effects. Built using Python and powerful computer vision libraries.

---

## 🎮 Live Gameplay Preview

> Rock ✊ | Paper ✋ | Scissors ✌️ — Just show your move to the camera and play against AI!

---

## 🚀 Features

* Real-time **hand gesture recognition** using webcam input
* Accurate detection of Rock, Paper, and Scissors using finger landmarks
* Automated **AI opponent** with random move generation
* Countdown timer before each round for fair play
* Dynamic **score tracking** and win condition logic (first to 5 wins)
* Visually appealing UI with custom overlays and move animations
* Sound effects for game outcome using TTS audio
* Game state management including **reset and replay options**

---

## 🧠 Technologies & Libraries Used

| Library     | Purpose                                                         |
| ----------- | --------------------------------------------------------------- |
| `OpenCV`    | Video capture, image display, text overlays, frame manipulation |
| `cvzone`    | Simplified OpenCV operations, PNG overlays, hand tracking       |
| `MediaPipe` | Hand landmark detection (via `HandTrackingModule`)              |
| `gTTS`      | Generate text-to-speech audio for voice-based effects           |
| `playsound` | Play audio files (TTS output)                                   |
| `pygame`    | Mixer used for win/lose sound effects                           |
| `random`    | Generate AI's move logic                                        |
| `time`      | Countdown timer & round control                                 |

---

## 📸 Screenshots

[PlayerWins](https://github.com/user-attachments/assets/4efee600-9ffe-4317-b1d3-8b9aaa44b412)
![AIWins](https://github.com/user-attachments/assets/0e6e85b8-405f-42bf-8edd-8cd645f8e8b3)

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/gesture-rps-game.git
cd gesture-rps-game

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

Ensure you have a working webcam and audio support on your machine.

---

## 📁 Resources Folder Structure

```
Resources/
├── BG.png                 # Game background
├── 1.png / 2.png / 3.png  # Rock, Paper, Scissors images
├── PlayerWins.png         # Player victory screen
├── AIWins.png             # AI victory screen
├── win.wav / lose.wav     # Game result sound effects
```

---

## 🎯 Game Rules

* Rock beats Scissors
* Scissors beats Paper
* Paper beats Rock
* First to 5 points wins the game

Use hand gestures:

* ✊ Rock: All fingers down
* ✋ Paper: All fingers up
* ✌️ Scissors: Only index and middle finger up

---

## 📚 Learnings

* Building gesture-controlled systems using MediaPipe and cvzone
* Designing real-time interactive experiences
* Integrating vision, audio, and UI logic in Python
* Handling game states, sound triggers, and responsive feedback

---

## 🙌 Acknowledgements

Huge thanks to the open-source community and developers behind OpenCV, cvzone, MediaPipe, and Pygame.

---

## 💡 Future Improvements

* Add multiplayer support
* Deploy as a desktop app or web app with webcam access
* Add leaderboard and difficulty levels

---

## 👨‍💻 Author

Built with 🔥 by Yash
Let’s connect: www.linkedin.com/in/yash-srivastava-46a02a28b

---

## 🏷️ Tags

`#OpenCV` `#GestureRecognition` `#cvzone` `#PythonProjects` `#AI` `#HumanComputerInteraction`
