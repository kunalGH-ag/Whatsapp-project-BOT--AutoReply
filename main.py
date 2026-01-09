import pyautogui
import time
import pyperclip
from google import genai

def last_message_from_kunal(chat_text: str) -> bool:
    lines = [line.strip() for line in chat_text.splitlines() if line.strip()]
    if not lines:
        return False

    last_line = lines[-1].lower()

    # Check sender name
    return "kunal" in last_line.split("]")[1]


client = genai.Client(api_key)

# Safety: move mouse to a corner to abort
#pyautogui.FAILSAFE = True

pyautogui.click(648,1052)
time.sleep(0.5)

count = 0
while True:
    #Click at starting position
    pyautogui.click(675, 223)
    time.sleep(0.2)

    if(count != 0):
        time.sleep(7)

    pyautogui.mouseDown(675,223)

    #Drag to select text
    pyautogui.moveTo(1878, 905, duration=0)
    time.sleep(0.2)

    pyautogui.mouseUp()

    #Copy selected text
    pyautogui.hotkey('ctrl', 'c')

    # Delay to ensure clipboard updates
    time.sleep(0.3)

    pyautogui.click(1878,906)
    time.sleep(0.3)

    #Getting copied text from clipboard
    copied_text = pyperclip.paste()

    count +=1
    if not last_message_from_kunal(copied_text):

        prompt = f"""
        You are a 22 year old male person named Kunal from Jaipur, India.
        You know Hindi and English and keep conversations light.
        Analyze the chat history and generate the next reply.
        Focus on the last 2 to 3 messages, but consider earlier content to curate response.
        Keep the reply short and don't use much puntuations.
        Give only the reply text.

        Chat history:
        {copied_text}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=prompt
        )
        #print(response.text)

        pyperclip.copy(response.text)
        time.sleep(0.3)

        pyautogui.click(914,970)
        time.sleep(0.3)

        pyautogui.hotkey("ctrl","v")
        time.sleep(0.8)

        pyautogui.press("enter")

        # print(response.text)
