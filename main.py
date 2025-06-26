import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import pygame

# Initialize Pygame mixer for sound
pygame.mixer.init()
win_sound = pygame.mixer.Sound("Resources/win.wav")
lose_sound = pygame.mixer.Sound("Resources/lose.wav")

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

# Variables
timer = 0
stateResult = False
startGame = False
gameOver = False
initialTime = 0
winScore = 5
scores = [0, 0]  # [AI, Player]
roundActive = False
delayStart = None
showAIMove = False
aiMoveImage = None
soundPlayed = False  # To ensure sound plays only once on result screen

while True:
    imgBG = cv2.imread("Resources/BG.png")
    success, img = cap.read()
    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]
    hands, img = detector.findHands(imgScaled)

    # Insert webcam into background
    imgBG[234:654, 795:1195] = imgScaled

    # Display score
    cv2.putText(imgBG, str(scores[0]), (410, 215),
                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215),
                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    # Game logic
    if startGame and not gameOver:
        if not roundActive:
            initialTime = time.time()
            roundActive = True
            stateResult = False

        countdown = 3 - int(time.time() - initialTime)
        if countdown >= 0:
            cv2.putText(imgBG, str(countdown), (605, 435),
                        cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
        else:
            if not stateResult:
                stateResult = True
                roundActive = False

                playerMove = None
                if hands:
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1  # Rock
                    elif fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2  # Paper
                    elif fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3  # Scissors

                aiMove = random.randint(1, 3)
                aiMoveImage = cv2.imread(f"Resources/{aiMove}.png", cv2.IMREAD_UNCHANGED)

                if playerMove:
                    # Determine winner
                    if (playerMove == 1 and aiMove == 3) or \
                       (playerMove == 2 and aiMove == 1) or \
                       (playerMove == 3 and aiMove == 2):
                        scores[1] += 1
                    elif (aiMove == 1 and playerMove == 3) or \
                         (aiMove == 2 and playerMove == 1) or \
                         (aiMove == 3 and playerMove == 2):
                        scores[0] += 1

                # Check for game over
                if scores[0] == winScore or scores[1] == winScore:
                    gameOver = True
                    delayStart = time.time()
                    soundPlayed = False  # Reset sound flag

    # Display AI move image persistently
    if aiMoveImage is not None:
        imgBG = cvzone.overlayPNG(imgBG, aiMoveImage, (149, 310))

    # Game Over Display
    if gameOver:
        if time.time() - delayStart > 0.5:
            if scores[1] == winScore:
                winnerImg = cv2.imread("Resources/PlayerWins.png")
                if not soundPlayed:
                    pygame.mixer.Sound.play(win_sound)
                    soundPlayed = True
            else:
                winnerImg = cv2.imread("Resources/AIWins.png")
                if not soundPlayed:
                    pygame.mixer.Sound.play(lose_sound)
                    soundPlayed = True

            winnerImg = cv2.resize(winnerImg, (1280, 720))
            cv2.imshow("BG", winnerImg)
        else:
            cv2.imshow("BG", imgBG)
    else:
        cv2.imshow("BG", imgBG)

    # Key bindings
    key = cv2.waitKey(1)
    if key == ord('s') and not gameOver:
        startGame = True
        roundActive = False
        scores = [0, 0]
        aiMoveImage = None
    elif key == ord('r'):
        gameOver = False
        startGame = False
        scores = [0, 0]
        stateResult = False
        roundActive = False
        soundPlayed = False
        aiMoveImage = None
    elif key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
