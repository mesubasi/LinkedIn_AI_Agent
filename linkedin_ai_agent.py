import pdfplumber
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("BROWSER_DRIVER_PATH")
cv = os.getenv("CV_PATH")


def extract_pdf_text(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join([page.extract_text() or "" for page in pdf.pages])
    return text.strip()


cv_text = extract_pdf_text(cv)

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path=f"{path}",
    )
)

initial_actions = [
    {"open_tab": {"url": "https://www.linkedin.com/feed/"}},
]


async def main():
    try:
        agent = Agent(
            task=(
                f"""Search and apply for jobs on LinkedIn continuously until the user stops. The steps should be as follows:
                1. Log in to LinkedIn. Verify that you are logged in with username and password.
                2. On the home page or in the navigation bar, find the 'İş İlanları' tab and click on it.
                3. Search for 'Yazılım Geliştirici' jobs in İstanbul, Türkiye and press the "Arama Yap" button or Enter.
                4. Study each advertisement by reading the titles and short descriptions.
                5. Read the description of the advertisement and compare it with the content of the CV. CV: {cv_text}
                If the requirements of the advertisement match the skills and experience on your CV, apply.
                6. Skip listings where the "Uygula" button appears.
                7. If the advertisement offers an 'Kolay Başvuru' option and matches your CV, apply immediately.
                8. Choose the appropriate salary range according to the level of the position (e.g. lower salary range for Junior positions).
                9. Answer the application questions automatically: multiple choice, short answer and yes/no questions as appropriate. Skip already filled questions.
                10. Find and click the 'Next' button at each step. Then find and click on the 'İncele' button. If the 'Başvuruyu Gönder' button appears, complete the application. If it says “Application submitted”, click the “Bitti” button or "X" button to close the window.
                11. Keep applying to apply for different and CV-compatible postings until the user stops.
                """
            ),
            llm=ChatOpenAI(model="gpt-4o"),
            browser=browser,
            initial_actions=initial_actions,
            save_conversation_path="logs/conversation",
        )

        result = await agent.run(max_steps=500)
        print(result)
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        input("Press Enter to close the browser...")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
